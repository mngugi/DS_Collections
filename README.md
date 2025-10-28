## Welcome to the DS_Collections wiki!

# 📊 DS_Collections: Data Science Projects Repository

Welcome to **DS_Collections**, a curated collection of data science projects and notebooks. This repository showcases various aspects of data analysis, machine learning, and data visualization using Python.

---

## 🧠 Projects Overview

| Notebook Title                          | Description                                      |
|-----------------------------------------|--------------------------------------------------|
| `Electric_Size_Market_.ipynb`           | Analysis of electric market size trends.         |
| `MLLearningWithPython.ipynb`            | Introduction to machine learning concepts.       |
| `Seaborn_Visualizations.ipynb`          | Data visualization using Seaborn library.        |
| `Sequential_model.ipynb`                | Implementation of sequential neural networks.    |
| `Timeseriesplot.ipynb`                  | Time series data plotting and analysis.          |
| `Yoro_vs_Man_united_Center_Backs.ipynb` | Comparative analysis of football center backs.   |
| `linearRegression.ipynb`                | Linear regression model implementation.          |
| `lineplot.ipynb`                        | Line plot visualizations with sample data.       |
| `mnistdataset.ipynb`                    | MNIST dataset exploration and modeling.          |
| `tensorTest.ipynb`                      | Tensor operations and manipulations.             |

DS_Collections/ 
├── .jupyter/ 

├── Electric_Size_Market_.ipynb 

├── MLLearningWithPython.ipynb 

├── Seaborn_Visualizations.ipynb 

├── Sequential_model.ipynb 

├── Timeseriesplot.ipynb 

├── Yoro_vs_Man_united_Center_Backs.ipynb 

├── linearRegression.ipynb 

├── lineplot.ipynb 

├── mnistdataset.ipynb 

├── tensorTest.ipynb 

├── LICENSE 

└── README.md

---

## 🎯 Purpose

This repository serves as a learning and reference resource for:

- Understanding and applying data science techniques.
- Exploring machine learning models and their implementations.
- Visualizing data effectively to derive insights.

---

## 🤝 Contributions

Contributions are welcome! If you have suggestions, improvements, or additional projects to add, feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the [GPL-3.0 License](LICENSE).

---

## 📬 Contact

For any inquiries or discussions, please open an issue on the repository.

---

*Happy Data Exploring!*


---

## 🛠️ Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - Data Manipulation: `pandas`, `numpy`
  - Visualization: `matplotlib`, `seaborn`
  - Machine Learning: `scikit-learn`, `tensorflow`
- **Tools**: Jupyter Notebooks

---

## 📁 Repository Structure

---

### Seaborn_Visualizations.ipynb

**Code**
```python
# Anscombe Quartet

import seaborn as sns

sns.set_theme(style = "darkgrid")

Anscombe_Dt = sns.load_dataset("anscombe")

sns.lmplot(data= Anscombe_Dt, x= "x", y="y",
           hue= "dataset",col = "dataset", col_wrap=2, palette= "muted",
           ci=None,height=4, scatter_kws={"s": 50, "alpha": 1})

Anscombe_Dt.head()

```

* **data:** The DataFrame to use (in this case, Anscombe_Dt).
* **x:** The variable to be plotted on the x-axis.
* **y:** The variable to be plotted on the y-axis.
* **hue:** Grouping variable that will produce points with different colors. Here, it's based on the "dataset" column.
* **col:** Variable that will produce separate columns within the grid for different values. This will create separate plots for each "dataset".
* **col_wrap:** Number of columns in the grid before wrapping to a new row.
* **palette:** Color palette to use for the different levels of the hue variable.
* **ci:** Confidence interval for the regression estimate. None in this case.
* **height:** Height (in inches) of each facet.
* **scatter_kws:** Additional keyword arguments to pass to plt.scatter and plt.plot.

  ---

---
title: "Ice Cream Sales Regression Model"
description: "Linear regression analysis of the relationship between temperature and ice cream sales using the ice_sales.csv dataset."
author: "Peter Ngugi"
date: 2025-10-28
project: "Regression Models"
dataset:
  file_name: "ice_sales.csv"
  shape: [12, 3]
  columns:
    - name: "Temperature (x)"
      type: int64
      role: independent_variable
      description: "Represents the temperature in degrees used as the predictor variable."
    - name: "Ice cream sales (y)"
      type: int64
      role: dependent_variable
      description: "Actual number of ice cream sales corresponding to each temperature."
    - name: "Predicted Sales ('Y)"
      type: int64
      role: predicted_variable
      description: "Existing predicted values from an earlier or external model."
  missing_values:
    Temperature (x): 0
    Ice cream sales (y): 0
    "Predicted Sales ('Y)": 0
  notes: "Dataset is clean, numeric, and ready for regression modeling."

analysis_plan:
  objective: "To model the relationship between temperature and ice cream sales."
  model_type: "Simple Linear Regression"
  target_variable: "Ice cream sales (y)"
  predictor_variable: "Temperature (x)"
  alternative_model: "Compare regression predictions to 'Predicted Sales (Y)' to evaluate model performance."
  steps:
    - "Load and explore dataset."
    - "Visualize data (scatter plot of temperature vs sales)."
    - "Fit a linear regression model."
    - "Evaluate performance using R², MAE, and RMSE."
    - "Plot regression line over actual data."
  libraries_used:
    - pandas
    - scikit-learn
    - matplotlib
    - numpy

expected_output:
  - "Regression equation: y = m*x + b"
  - "Correlation coefficient and R² value."
  - "Residual plot for model diagnostics."
  - "Comparison chart: Actual Sales vs Predicted Sales."
  - "Statistical metrics showing accuracy and error rate."

comments:
  - "No missing or invalid data detected."
  - "Linear relationship expected between temperature and sales."
  - "Dataset size (12 samples) is small; model will demonstrate linear fitting rather than robust forecasting."
  - "Future work: Expand dataset with more temperature points for stronger generalization."
---

