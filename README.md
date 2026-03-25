# 🍽️ Predicting Food Demand at the KU Mensa

This project focuses on building a machine learning model to predict daily food demand at the KU Mensa.  
Accurate demand forecasting helps reduce food waste, improve planning, and support more efficient kitchen operations.

The project was developed as part of the **Data Lab course** at KU Eichstätt–Ingolstadt.

---

## 📌 Overview

Predicting food demand in a university canteen is a challenging task due to:
- highly variable dish names  
- seasonal and weekly consumption patterns  
- inconsistent historical data formats  

We use historical data (2014–2023) to train models that estimate the number of portions sold per dish.

Our approach combines:
- time-based features  
- rolling statistics  
- semantic embeddings of dish names  
- clustering techniques  

---

## 📊 Results

Our best model (**XGBoost**) achieved:

- **MAE:** 31.57  
- **R²:** 0.67  

These results demonstrate strong predictive performance using only historical data — without relying on manual estimates from Mensa staff :contentReference[oaicite:0]{index=0}.

Although the model does not yet outperform human planning (baseline MAE ≈ 14.66), it provides a **fully automated and scalable solution**.

---

## ⚙️ Methodology

### 🧹 Data Processing
- Combined multiple Excel files into a single dataset  
- Cleaned inconsistent formats and merged tables  
- Focused on main dishes (**Essen 1–5**)  
- Removed COVID years (2020–2021) due to abnormal patterns :contentReference[oaicite:1]{index=1}  

### 🧠 Feature Engineering
- Time-based features (weekday, month, year)  
- Rolling averages (7-day, 30-day)  
- Daily total sales  

### 🍝 Dish Name Processing
To handle inconsistent dish naming:

- Generated **semantic embeddings** using Google Gemini API  
- Reduced dimensionality using **PCA** (127 components)  
- Applied **KMeans clustering** (150 groups)  

This allowed the model to capture similarities between dishes even when names differ.

---

## 🤖 Models

We evaluated multiple models:

- Linear Regression  
- Random Forest  
- XGBoost  

Key findings:
- Time-based features alone already perform well  
- Embeddings slightly improve performance  
- Clustering provides a simple and interpretable boost  
- **XGBoost performed best overall** :contentReference[oaicite:2]{index=2}  

---

## 📁 Repository Structure

- **`main.ipynb`** – Full pipeline: preprocessing, feature engineering, modeling  
- **`embedding_generation.ipynb`** – Generates semantic embeddings  
- **`embedding_clustering.ipynb`** – Clustering of dish embeddings  
- **`/pickle_files/`** – Saved intermediate results  

- **`/data/`** – Contains original Mensa datasets  
  ⚠️ *Not included in this repository due to data privacy and sharing restrictions*

---

## 🔒 Data Availability

The dataset used in this project is not publicly available due to data protection policies.  
The repository contains only code and processed artifacts required to reproduce the workflow.

---

## 🚀 Future Improvements

- Improve handling of dish name variability  
- Integrate external features (weather, events, holidays)  
- Combine model predictions with staff estimates  
- Explore deep learning approaches for text embeddings  

---

## 👩‍💻 Authors

- **Olga Ivanova**  
- **Artem Kardaiev**

---

## 📚 References

- Google Gemini API (Embeddings)  
- XGBoost Library  
- Hands-on Machine Learning (Aurélien Géron)  
