# Week1 - Day5

---

## 🔹 1. What is NumPy?

**NumPy** (Numerical Python) is used for:

* Fast numerical computations
* Working with arrays & matrices
* Mathematical operations

```python
import numpy as np
```

---

## 🔹 2. NumPy Arrays

### Create a 1D Array

```python
arr = np.array([1, 2, 3, 4])
print(arr)
```

### Create a 2D Array

```python
arr2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(arr2d)
```

---

## 🔹 3. Array Indexing & Slicing

### Indexing

```python
print(arr2d[0, 1])   # Row 0, Column 1 → 2
```

### Slicing

```python
print(arr2d[:, 1])   # All rows, column 1
print(arr2d[0, :])   # First row
print(arr2d[0:2, 1:3])  # Submatrix
```

---

## 🔹 4. Mathematical Operations

### Sum

```python
np.sum(arr2d)           # Total sum
np.sum(arr2d, axis=0)   # Column-wise sum
np.sum(arr2d, axis=1)   # Row-wise sum
```

### Mean

```python
np.mean(arr2d)
```

### Transpose

```python
print(arr2d.T)
```

### Dot Product

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))
```

---

## 🔹 5. Random Number Generation

```python
np.random.rand(3, 3)        # Random numbers (0 to 1)
np.random.randint(1, 10, (3, 3))  # Random integers
np.random.randn(3, 3)       # Normal distribution
```

---

## ✅ Practice 1: Create a 2D Array & Compute Row/Column Sums

```python
import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Row sums
row_sums = np.sum(matrix, axis=1)

# Column sums
col_sums = np.sum(matrix, axis=0)

print("Matrix:\n", matrix)
print("Row sums:", row_sums)
print("Column sums:", col_sums)
```

---

## ✅ Practice 2: Matrix Multiplication

## 🔹 Manual Implementation

```python
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

result_manual = np.zeros((2, 2))

for i in range(2):
    for j in range(2):
        for k in range(2):
            result_manual[i][j] += A[i][k] * B[k][j]

print("Manual Multiplication:\n", result_manual)
```

---

## 🔹 Using NumPy Built-in

```python
result_numpy = np.dot(A, B)
# OR
result_numpy = A @ B

print("NumPy Multiplication:\n", result_numpy)
```

---

## ✅ Practice 3: Generate Random Dataset

```python
# Generate dataset of 100 students with 3 subjects
dataset = np.random.randint(40, 100, (100, 3))

print("Dataset shape:", dataset.shape)
print("First 5 rows:\n", dataset[:5])

# Calculate average marks per subject
subject_mean = np.mean(dataset, axis=0)
print("Average per subject:", subject_mean)
```

---

## 🎯 Mini Challenge (Optional)

Try this:

1. Generate a 5×5 random matrix
2. Find:

   * Maximum value
   * Minimum value
   * Mean of each row
   * Transpose
3. Multiply the matrix by itself

---

## 🧠 Day 5 Summary

You learned:

* ✅ NumPy arrays
* ✅ Indexing & slicing
* ✅ Sum, mean, transpose, dot product
* ✅ Random number generation
* ✅ Manual vs NumPy matrix multiplication

---