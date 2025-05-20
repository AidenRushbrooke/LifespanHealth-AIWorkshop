# LifespanHealth-AIWorkshop: AI-Driven Symptom Clustering

Welcome to the Lifespan Health AI Workshop! This repository contains everything you need to complete the **symptom clustering workshop** using synthetic Long Covid data and unsupervised machine learning.

## What You'll Be Doing

You’ll be working with one of five **synthetic datasets**, each simulating self-reported Long Covid symptoms. Your goal is to:

1. **Explore the data** using dimensionality reduction (UMAP)
2. **Identify symptom clusters** using unsupervised clustering (HDBSCAN)
3. **Interpret the clinical relevance** of your findings

Don’t worry if you’ve never used Python before — this guide will walk you through every step.

---

## 1. Installing Python (for Beginners)

If you don’t already have Python installed:

1. Go to the official Python website: https://www.python.org/downloads/
2. Click “Download Python 3.12.x” (or latest version).
3. Run the installer.
4. **IMPORTANT**: During installation, tick the box that says **“Add Python to PATH”** before clicking "Install Now".

Once Python is installed, open your Terminal (macOS/Linux) or Command Prompt (Windows) and run:

```bash
pip install pandas numpy scikit-learn umap-learn hdbscan matplotlib seaborn
```

This installs all the Python packages you’ll need for this project.


---

## 2. How to Use the Clustering Notebook

### 1: Open the Jupyter Notebook

If this is your first time using Jupyter Notebook, install it with:

```bash
pip install notebook
```

Then launch it:
```bash
jupyter notebook
```

A browser window will open. Navigate to and open **"notebook_clustering.ipynb"** .
### 2: Load a Dataset

At the top of the notebook, choose one dataset:

```
python
import pandas as pd
data = pd.read_csv("synthetic_dataset_1.csv")
```

You can pick any of the 5 datasets provided.

### 3: Run UMAP for Dimensionality Reduction

UMAP will help reduce the data to 2D for visualisation:

```python
import umap
reducer = umap.UMAP(random_state=42)
embedding = reducer.fit_transform(data)
```

### 📍 Step 4: Apply HDBSCAN for Clustering

```python
import hdbscan
clusterer = hdbscan.HDBSCAN(min_cluster_size=20)
labels = clusterer.fit_predict(embedding)
```

### 5: Visualise
```python
import matplotlib.pyplot as plt
plt.scatter(embedding[:, 0], embedding[:, 1], c=labels, cmap='Spectral', s=10)
plt.title("Symptom Clusters Identified by HDBSCAN")
plt.show()
```













