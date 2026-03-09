import pandas as pd
import re
import os

# ==================== CONFIG ====================
INPUT_FILE  = './data/raw/fintech_reviews_raw_032026.csv'           # ← adjust filename if needed
OUTPUT_FILE = './data/cleaned/fintech_reviews_cleaned.csv'
TEXT_COLUMN = 'content'                                       # ← change if your column is named differently

MIN_LENGTH_AFTER_CLEAN = 3   # drop only extremely short / empty after cleaning

# ===============================================

def remove_emojis(text):
    if not isinstance(text, str):
        return ""
    # Wide range of emojis and symbols
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001F900-\U0001F9FF"
        "\U0001FA70-\U0001FAFF"
        "\U00002600-\U000026FF"
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


def clean_text(text):
    if not isinstance(text, str):
        return ""
    
    # 1. Remove emojis first
    text = remove_emojis(text)
    
    # 2. Remove URLs, mentions, hashtags
    text = re.sub(r'http\S+|www\.\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    
    # 3. Remove excessive / unusual special characters
    # Keep: letters, numbers, space, ! ? . , ; : ' " - … (horizontal ellipsis)
    # Remove most other symbols: *, ^, ~, |, \, {, }, [, ], etc.
    allowed = r'a-zA-Z0-9\s!\?\.,;:\'\"\\-\u2026'
    text = re.sub(f'[^{allowed}]', '', text)
    
    # 4. Normalize whitespace (including newlines, tabs → single space)
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


# ==================== MAIN ====================
print("Loading raw data...")
df = pd.read_csv(INPUT_FILE)

original_rows = len(df)
print(f"Original rows: {original_rows:,}")

# ── Basic structural cleaning ───────────────────────────────────────
df = df.drop_duplicates(subset=[TEXT_COLUMN])           # exact duplicates on original text
df = df.dropna(subset=[TEXT_COLUMN])
df = df[df[TEXT_COLUMN].str.strip() != '']

print(f"After drop duplicates + na + empty: {len(df):,}")

# ── Apply text cleaning ──────────────────────────────────────────────
print("Cleaning text (emojis, urls, symbols, whitespace)...")
df['cleaned_content'] = df[TEXT_COLUMN].apply(clean_text)

# ── Final safety filter: drop only near-empty after cleaning ────────
df = df[df['cleaned_content'].str.strip() != '']
df = df[df['cleaned_content'].str.len() >= MIN_LENGTH_AFTER_CLEAN]

print(f"Final rows after cleaning: {len(df):,}")
print(f"Rows removed overall: {original_rows - len(df):,} ({(original_rows - len(df)) / original_rows * 100:.1f}%)")

# Optional: save both versions side by side (very useful for annotation & debugging)
df = df[[TEXT_COLUMN, 'cleaned_content'] + 
        [c for c in df.columns if c not in [TEXT_COLUMN, 'cleaned_content']]]

df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')
print(f"\nSaved to: {OUTPUT_FILE}")
print("→ Ready to import 'cleaned_content' (or both columns) into Label Studio")