# Day7 - Iris Dataset Full EDA + Visualization

Dataset: `Iris` (built-in from sklearn)
Goal:

* Understand class distribution
* Analyze feature relationships
* Detect correlation
* Prepare for ML

---

# 🧠 What You Will Learn

* Distribution analysis
* Class imbalance check
* Feature comparison
* Correlation heatmap
* Pairwise visualization
* Drawing conclusions

---

# 📁 Project Structure

```
iris_eda_project/
│
├── 1. Load Data
├── 2. Basic Info
├── 3. Univariate Analysis
├── 4. Bivariate Analysis
├── 5. Correlation Analysis
└── 6. Conclusion
```

---

# 🚀 Step 1: Load Data

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

sns.set_style("whitegrid")

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# convert numeric target to names
df['species'] = df['species'].map({0:'setosa',1:'versicolor',2:'virginica'})

df.head()
```

---

# 🔍 Step 2: Basic Info

```python
df.info()
df.describe()
```

Check:

* Any missing values?
* Mean & std
* Feature ranges

---

# 📊 Step 3: Univariate Analysis (Single Feature)

## 1️⃣ Class Distribution

```python
sns.countplot(x='species', data=df)
plt.title("Class Distribution")
plt.show()
```

👉 Check if data is balanced.

---

## 2️⃣ Feature Distribution

```python
sns.histplot(df['sepal length (cm)'], kde=True)
plt.title("Sepal Length Distribution")
plt.show()
```

Try for all features.

---

## 3️⃣ Boxplot (Outlier Detection)

```python
sns.boxplot(x='species', y='sepal length (cm)', data=df)
plt.show()
```

Observe:

* Does one species have larger petals?
* Any outliers?

---

# 🔗 Step 4: Bivariate Analysis

## 1️⃣ Scatter Plot

```python
sns.scatterplot(
    x='sepal length (cm)',
    y='petal length (cm)',
    hue='species',
    data=df
)
plt.show()
```

Look:

* Is one class clearly separable?

---

## 2️⃣ Pairplot (Very Powerful)

```python
sns.pairplot(df, hue='species')
plt.show()
```

This shows:

* All feature relationships
* Class separation

---

# 🔥 Step 5: Correlation Analysis

```python
corr = df.drop('species', axis=1).corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
```

Check:

* Which features are highly correlated?
* Any multicollinearity?

---

# 🧾 Step 6: Write Conclusion (VERY IMPORTANT)

Write in notebook:

Example:

> 1. Dataset is balanced.
> 2. Petal length strongly separates classes.
> 3. Petal width and petal length are highly correlated.
> 4. Setosa is clearly separable from others.
> 5. Sepal features overlap more.

THIS is what interviewers want.

---
