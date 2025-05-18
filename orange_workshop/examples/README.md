## Further Exploration & Challenges

Once you're comfortable with the example workflows, try a couple of additional tasks to deepen your understanding and experiment further. You can modify the existing example workflows or create new ones from scratch.

### A. Deeper Data Exploration & Understanding (Using Workshop Data)

1.  **Targeted Visualizations:**
    * Using the `synthetic_mri_features` (5k or 20k) dataset, create a **Scatter Plot** of `Hippocampus` vs. `Ventricles`. Color the points by the `DX` (diagnosis) column. Do you see any visual separation or trends? Try this with other pairs of MRI features.
    * For the `synthetic_cognitive_scores` dataset, use the **Distributions** widget to compare the distribution of `MMSE` scores for each `DX` group. Repeat for `ADAS13` and `RAVLT_immediate`. What differences do you observe?
    * Use the **Box Plot** widget to examine the spread and median of `AGE` for each `DX` group.

2.  **Correlation Analysis:**
    * Load one of the datasets and use the **Correlations** widget (or create a **Heatmap** of a correlation matrix). Identify any pairs of features that are highly correlated (e.g., |correlation| > 0.7).

3.  **Handling Missing Data (if present in synthetic data):**
    * Compare the effect of different imputation methods (e.g., "Average/Most frequent", "Model-based imputer") on the distribution of a feature or on the performance of a simple classification model from `1_simple_classification.ows`.

4.  **Data Subsetting:**
    * Use the **Select Rows** widget to filter one of the datasets (e.g., select only participants where `AGE` > 70 and `PTGENDER` is a specific value).
    * Re-run the `1_simple_classification.ows` workflow on this subset. How does the model performance change? Are different features now more important?

### B. Advanced Modeling & Evaluation

1.  **Trying Different Models:**
    * Modify `2_advanced_classification.ows` to include other classifiers available in Orange that weren't in the original workflow (e.g., Naive Bayes, AdaBoost, Neural Network). How do they compare in performance?

2.  **Exploring Evaluation Metrics:**
    * In the "Test & Score" widget, spend time looking at different metrics beyond AUC and CA (Accuracy). What do Precision, Recall, and F1 tell you about the model's performance for each `DX` class?
    * Use the **ROC Analysis** widget to compare multiple models. 
    * Examine the **Confusion Matrix**. Which classes are most often confused with each other?

### C. (Optional) Bringing Your Own Data

If you have your own tabular dataset (e.g., a CSV file) that you'd like to explore for a classification or regression task:

1.  **Load Your Data:** Use the **File** widget in Orange.
2.  **Inspect & Preprocess:**
    * Use **Data Info** and **Feature Statistics** to understand its structure.
    * Use **Edit Domain** to correct any misidentified data types (e.g., categorical features read as numbers).
    * Use **Select Columns** to choose your features and define your target variable.
    * Use **Impute** if you have missing data.
3.  **Apply Workflows:** Try to adapt the example workflows from this workshop (e.g., `1_simple_classification.ows` or `3_visualisations.ows`) to your dataset.

Remember to save your modified workflows often! Have fun exploring!
