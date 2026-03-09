# Nigerian Fintech Reviews Sentiment Annotation Guidelines

## 📌 Project Overview
This project involves **manual sentiment annotation** of 572 user reviews** collected from Nigerian fintech apps (Opay, Moniepoint, Palmpay, Kuda)**. The purpose of this annotation is to create a high-quality labeled dataset for **sentiment analysis and NLP projects**.  

**Dataset Language:** English  
**Number of Records:** 572  

---

## 🎯 Objective
- Classify each review into **one of three sentiment categories**:
  1. **Positive** ✅ – Review expresses satisfaction, praise, or favorable experience.
  2. **Neutral** ⚪ – Review expresses a neutral or factual statement without strong sentiment.
  3. **Negative** ❌ – Review expresses dissatisfaction, criticism, or negative experience.

---

## 🛠 Annotation Tool
- **Label Studio** (via Docker)
- Each record in the dataset was reviewed manually and assigned one of the three sentiment labels based on **actual content**.

---

## ✍ Annotation Guidelines
1. **Read the full review content** carefully before labeling.  
2. Assign **one label per review**:
   - Positive: Users express happiness, satisfaction, or positive experiences.  
   - Neutral: Users are merely describing or reporting without expressing a strong opinion.  
   - Negative: Users express complaints, frustration, or dissatisfaction.  
3. Ignore the **numerical app rating**; focus on the **text content**.  
4. Remove emojis or extra whitespace in text if present; focus on meaning.  
5. If a review is ambiguous, assign **Neutral**.  

---

## 📋 Quality Assurance Rules
- Ensure **no record is unlabeled**.  
- Remove **duplicate records** before finalizing the dataset.  
- Consistency check: Reviews with similar content should have **the same sentiment label**.  
- Final dataset has **572 labeled records**.  

---

## ⚙️ Data Storage
- Labeled dataset is stored in **CSV format** (`fintech_reviews_labeled.csv`) with columns:
  1. `reviewId` – Unique ID of the review  
  2. `content` – Text of the user review  
  3. `app_name` – App the review belongs to  
  4. `at` – Timestamp of the review  
  5. `sentiment_label` – Final label: Positive, Neutral, Negative  

---

## ✅ Notes
- This dataset can be used for **training sentiment classification models**, NLP research, and other fintech analytics projects.  
- Following this guideline ensures **high-quality, consistent labeling** suitable for machine learning pipelines.  