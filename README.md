# LifespanHealth-AIWorkshop
Code and datasets for the Lifespan Health AI Workshop at UEA

# 1) ...

# 2) ...


# 3) Workshop: Simple AI Methods for Dementia Research using Orange
Welcome to the workshop on applying simple AI methods for dementia research using the Orange Data Mining tool!

# About Orange Data Mining
[Orange](https://orangedatamining.com/) is an open-source data visualization, machine learning, and data mining toolkit. It features a visual programming front-end for explorative data analysis and interactive visualization, and can also be used as a Python library. Orange is designed to be user-friendly, making complex data analysis tasks accessible to everyone.

## Workshop Materials
All materials are located within this `orange_workshop` directory.
 
* **Example Workflows:** Pre-built Orange workflow files (`.ows`) are stored in `orange_workshop/examples/`.
* **Synthetic Datasets:** The synthetic data files (`.csv`) for use in the workflows are stored in `orange_workshop/data/`.

## Synthetic Datasets
The datasets provided in the `orange_workshop/data/` directory are **synthetically generated**. They are designed to mimic the statistical properties and trends found in real patient samples but **do not contain any real patient information**. These datasets are for example workshop purposes only.

We have provided datasets with two different feature sets and two different sample sizes (5k/20k):

1.  **MRI Features:** These datasets contain features typically derived from Magnetic Resonance Imaging.
2.  **Cognitive Scores:** These datasets contain features representing scores from various cognitive tests.

## Example Workflows

Located in `orange_workshop/examples/`, these Orange workflow files (`.ows`) provide starting points for your exploration:

1.  **`1_simple_classification.ows`:**
    * Demonstrates a basic classification pipeline: loading data, selecting features, training a simple model (e.g., Logistic Regression or kNN), and evaluating its performance (e.g., accuracy, confusion matrix).
2.  **`2_advanced_classification.ows`:**
    * Expands on the simple classification by introducing more advanced techniques such as cross-validation, comparing multiple algorithms (e.g., Random Forest, Support Vector Machines, Gradient Boosting), hyperparameter tuning (if applicable widgets are used), and more detailed performance evaluation (e.g., ROC curves, precision-recall curves).
3.  **`3_visualisations.ows`:**
    * Focuses on data exploration and visualization. This workflow will showcase various Orange widgets for understanding data distributions, relationships between features, and visualizing high-dimensional data (e.g., scatter plots, box plots, distributions, heatmaps).

**To use these workflows:**
1.  Open Orange.
2.  Go to `File > Open...`
3.  Navigate to the `orange_workshop/examples/` directory and select the `.ows` file you wish to explore.
4.  Ensure the "File" widgets within the workflows are pointing to the correct synthetic dataset files in the `orange_workshop/data/` directory. You might need to adjust the file paths within Orange if they are not automatically resolved.

## Getting Started

1.  **Install Orange:** If you haven't already, download and install Orange from [https://orangedatamining.com/download/](https://orangedatamining.com/download/).
2.  **Review Slides:** Familiarize yourself with the concepts presented in `Simple_AI_Methods_for_Demetia_slides.pptx`.
3.  **Explore Workflows:** Open the example workflows in Orange and experiment with the different widgets and datasets.

We hope you find this workshop informative and enjoy exploring the capabilities of Orange for data analysis in dementia research!

---

**Note on Synthetic Data:** The synthetic data used in this workshop is generated to mimic real-world trends for educational purposes. It is entirely artificial and does not correspond to any real individuals. When working with real patient data, always adhere to strict ethical guidelines, privacy regulations (e.g., GDPR, HIPAA), and data use agreements.
