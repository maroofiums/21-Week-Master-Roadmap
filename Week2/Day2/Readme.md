# 📘 Day 2 – Matrices (Linear Algebra for ML)

## 📌 Overview

This module covers fundamental matrix operations required for Machine Learning:

* Matrix Addition
* Matrix Multiplication
* Transpose
* Determinant
* Inverse

These concepts are essential for:

* Linear Regression
* Neural Networks
* Optimization
* Gradient Descent
* Feature transformations

---

# 🔢 What is a Matrix?

A matrix is a rectangular array of numbers arranged in rows and columns.

Example:

```
A = [ 1  2
      3  4 ]
```

This is a 2×2 matrix
(2 rows, 2 columns)

---

# ➕ Matrix Addition

Two matrices can be added only if they have the same dimensions.

Formula:

```
A + B = element-wise addition
```

Example:

```
A = [1 2]
    [3 4]

B = [5 6]
    [7 8]

A + B = [6 8]
        [10 12]
```

---

# ✖️ Matrix Multiplication

Matrix multiplication is not element-wise.

Rules:

1. Columns of first matrix = Rows of second matrix
2. Result size = (rows of first × columns of second)

Example:

```
A = [1 2]
    [3 4]

B = [5 6]
    [7 8]

A × B = [19 22]
        [43 50]
```

---

# 🔁 Transpose

Transpose flips rows and columns.

```
A = [1 2]
    [3 4]

Aᵀ = [1 3]
      [2 4]
```

---

# 🔍 Determinant (2×2 only)

For:

```
A = [a b]
    [c d]
```

det(A) = ad − bc

Example:

```
A = [1 2]
    [3 4]

det(A) = (1×4) − (2×3)
        = 4 − 6
        = -2
```

If determinant = 0 → matrix is NOT invertible.

---

# 🔄 Inverse (2×2)

Inverse exists only if determinant ≠ 0.

Formula:

```
A⁻¹ = (1/det(A)) × [ d  -b
                     -c  a ]
```

Example:

```
A = [1 2]
    [3 4]

A⁻¹ = [-2   1]
       [1.5 -0.5]
```

---

# 💡 Why This Matters in ML

Matrices are used in:

* Linear regression (XW)
* Neural networks (weight matrices)
* Feature transformations
* Backpropagation
* Solving systems of equations

---

# 🧠 Practice Problems

1. Add two 2×2 matrices
2. Multiply two 2×2 matrices
3. Compute transpose of 2×3 matrix
4. Compute determinant of 2×2
5. Find inverse of 2×2 matrix

---
