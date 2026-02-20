# 📊 Day6 - Employee Data Analysis with Pandas

## 📌 Project Overview

This project demonstrates practical data analysis and preprocessing using **Pandas**.
We analyze a synthetic Tech Company Employee dataset to practice real-world data manipulation, feature engineering, and exploratory analysis techniques used in Machine Learning workflows.

---

## 📂 Dataset Description

The dataset contains 12 employees with the following features:

| Column            | Description                      |
| ----------------- | -------------------------------- |
| employee_id       | Unique employee identifier       |
| name              | Employee name                    |
| department        | Department (AI, Web, HR)         |
| age               | Age of employee                  |
| experience_years  | Years of professional experience |
| salary            | Annual salary                    |
| performance_score | Performance rating (1–10 scale)  |

---

## 🛠️ Key Operations Performed

### 1️⃣ Data Exploration

* Checked dataset shape
* Reviewed data types
* Generated statistical summary
* Inspected missing values

### 2️⃣ Data Filtering

* Filtered employees by department
* Selected high salary employees
* Applied multiple condition filters

### 3️⃣ Feature Engineering

* Created `salary_after_tax` column
* Created `seniority_level` (Junior / Mid / Senior)
* Calculated employee efficiency

### 4️⃣ GroupBy & Aggregation

* Average salary per department
* Average performance per department
* Employee count per department
* Identified department with highest average salary

### 5️⃣ Sorting & Ranking

* Sorted employees by salary
* Extracted top 3 highest-paid employees
* Added salary ranking column

### 6️⃣ Correlation Analysis

* Measured correlation between experience and salary
* Generated correlation matrix

### 7️⃣ Pivot Table

* Created pivot table showing average salary per department

---

## 📈 Skills Demonstrated

* DataFrame creation
* Indexing with `loc` and `iloc`
* Boolean filtering
* `apply()` and custom functions
* `groupby()` operations
* Sorting and ranking
* Correlation analysis
* Pivot tables
* Basic feature engineering

---

## 🎯 Learning Objective

The goal of this project is to build strong foundational skills in Pandas for:

* Data cleaning
* Feature engineering
* Exploratory data analysis
* Preparing datasets for Machine Learning models

---

## 🚀 Future Improvements

* Introduce missing values and handle them
* Encode categorical variables
* Scale numerical features
* Build a Machine Learning model using this dataset
* Add data visualization using Matplotlib / Seaborn

---
