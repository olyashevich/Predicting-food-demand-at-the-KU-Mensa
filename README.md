# Predicting Food Demand at the KU Mensa

This project aims to develop a machine learning model that can predict the daily sales of meals at the KU Mensa. The current prediction process relies on manual planning by the Mensa staff. Our goal is to provide a data-driven solution that outperforms or complements these manual estimates.

The project was developed as part of the **Data Lab** course.

---

## Repository Structure

- **`/data/`** – Contains two types of Excel tables from Mensa:
    - **Produktionsplanung** – Daily planned dishes, including "Essen 1–5", dish ingredients, and production estimates (target_amount).
    - **Verkaufszahlen** – Actual number of portions sold, formatted for human readability but requiring complex parsing for ML use.

- **`main.ipynb`** – The main notebook containing:
  - Data сollection and preprocessing
  - Visualization
  - Feature engineering
  - Model training and evaluation

- **`embedding_generation.ipynb`** – Generates semantic embeddings for dish names using Google Gemini API with **task_type = "SEMANTIC_SIMILARITY"**. These embeddings capture textual similarities between meal descriptions.

- **`embedding_clustering.ipynb`** –  Generates clustering-based embeddings using **task_type = "CLUSTERING"** from the Gemini API. Useful for grouping semantically similar dishes into categories.

- **`/pickle_files/`** – Saved outputs of the embedding notebooks in `.pkl` format.

---

## Authors

- Olga Ivanova  
- Artem Kardaiev

