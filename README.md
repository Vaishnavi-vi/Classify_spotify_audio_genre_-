# 🎵 Classify Audio Genre using Machine Learning

This project focuses on building machine learning models to classify audio samples into different music genres using extracted audio features. We compare the performance of four different classification algorithms: **Logistic Regression**, **Decision Tree**, **Random Forest**, and **XGBoost**.

---

## 📌 Problem Statement

Predict the **genre** of an audio sample using extracted audio features.This is a **multi-class classification** task with genres like rock, pop, classical, etc.

---

## 🎯 Objective

- Preprocess audio data and extract relevant features
- Train and compare multiple classification models
- Evaluate their performance using accuracy, precision, recall, and F1-score

---

## 🗃️ Dataset

- Source: Spotify Audio Genre
- Contains labeled audio files categorized by genre

---

## 🛠️ Tools & Libraries

- Python
- NumPy, Pandas, Matplotlib, Seaborn
- Scikit-learn
- imbalanced-learn
- XGBoost

---

## 🧠 Models Compared

| Model              | Precision  | 
|--------------------|----------  |
| Logistic Regression| 28.7%      | 
| Decision Tree      | 47.65%     | 
| Random Forest      | 47.65%     |
| XGBoost            | **47.91%** | 
| ANN                | 39.52%     |

✅ *XGBoost achieved the highest precision score.*

---

## 📊 Evaluation Metrics

- **Accuracy** – Overall correctness
- **Precision** – Correct positive predictions / total positive predictions

---

## 🌐 Streamlit App

🖥️ **Live Demo**: streamlit.py (streamlit run .\streamlit.py)

---

