# Week2 Day5 

# Vector Operations (From Scratch)

We represent a vector as:

```python
v = [1, 2, 3]
```

## 1. Vector Addition

Formula:
v + w = [v1+w1, v2+w2, ..., vn+wn]

```python
def vector_add(v, w):
    if len(v) != len(w):
        raise ValueError("Vectors must be same length")
    return [v[i] + w[i] for i in range(len(v))]
```

---

## 2. Scalar Multiplication

Formula:
c * v = [c*v1, c*v2, ..., c*vn]

```python
def scalar_multiply(c, v):
    return [c * x for x in v]
```

---

## 3. Dot Product

Formula:
v · w = v1*w1 + v2*w2 + ... + vn*wn

```python
def dot_product(v, w):
    if len(v) != len(w):
        raise ValueError("Vectors must be same length")
    return sum(v[i] * w[i] for i in range(len(v)))
```

---

## 4. Vector Magnitude

Formula:
||v|| = sqrt(v1² + v2² + ... + vn²)

```python
import math

def magnitude(v):
    return math.sqrt(sum(x**2 for x in v))
```

---

# Matrix Operations (From Scratch)

Matrix representation:

```python
A = [
    [1, 2],
    [3, 4]
]
```

---

## 1. Matrix Addition

```python
def matrix_add(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have same dimensions")

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return result
```

---

## 2. Matrix Transpose

Swap rows and columns.

```python
def transpose(A):
    rows = len(A)
    cols = len(A[0])

    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(A[i][j])
        result.append(row)

    return result
```

---

## 3. Matrix Multiplication

Core idea:

If A is (m × n) and B is (n × p)
Result is (m × p)

Element formula:
C[i][j] = sum(A[i][k] * B[k][j])

```python
def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Invalid dimensions for multiplication")

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            value = 0
            for k in range(len(B)):
                value += A[i][k] * B[k][j]
            row.append(value)
        result.append(row)

    return result
```

---

# Testing With NumPy (Verification Phase)

Now we verify correctness.

```python
import numpy as np

v = [1, 2, 3]
w = [4, 5, 6]

print("Vector Add:", vector_add(v, w))
print("NumPy:", list(np.array(v) + np.array(w)))

print("Dot Product:", dot_product(v, w))
print("NumPy:", np.dot(v, w))

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

print("Matrix Multiply:", matrix_multiply(A, B))
print("NumPy:", np.matmul(A, B))
```

If outputs match → your implementation is correct.

---

# What This Project Teaches You

Very important for ML:

* How dot product actually works (core of neural networks)
* Why matrix multiplication is expensive
* How dimensions must align
* What happens inside PyTorch / TensorFlow
* Why GPU acceleration matters

When you understand this deeply, linear algebra stops being “magic”.
