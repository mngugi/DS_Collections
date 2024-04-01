Welcome to the DS_Collections wiki!

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
