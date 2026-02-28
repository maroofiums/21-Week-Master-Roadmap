# Day 7 – Linear Algebra & Tensors

---

# 1. Scalars, Vectors, Matrices, Tensors

## Scalar

A single number.

Example:

```
5
```

Shape: ()

---

## Vector

1D array (magnitude + direction).

Example:

```
[1, 2, 3]
```

Shape: (3,)

Geometric meaning:
Arrow in space.

---

## Matrix

2D array.

Example:

```
[[1, 2],
 [3, 4]]
```

Shape: (2, 2)

Represents linear transformation.

---

## Tensor

Generalization of vectors and matrices.

* 0D → Scalar
* 1D → Vector
* 2D → Matrix
* 3D+ → Tensor

Example (image RGB):
Shape: (3, 32, 32)

Batch of 64 images:
Shape: (64, 3, 32, 32)

---

# 2. Vector Operations

## Vector Addition

v1 + v2 = [v1_i + v2_i]

Geometric meaning:
Tip-to-tail addition.

---

## Scalar Multiplication

k * v = stretch/shrink vector.

If k < 0 → direction flips.

---

## Dot Product

Formula:

```
u · v = u1v1 + u2v2 + ... + unvn
```

Geometric form:

```
u · v = |u||v|cosθ
```

Important facts:

* Dot = 0 → perpendicular
* Measures similarity

Used in:

* Cosine similarity
* Neural network layers
* Attention mechanisms

---

## Cross Product (3D only)

Formula:

```
u × v =
[
u2v3 - u3v2,
u3v1 - u1v3,
u1v2 - u2v1
]
```

Result:
Vector perpendicular to both.

Magnitude = area of parallelogram.

---

# 3. Vector Norms

## L2 Norm (Euclidean)

```
||v||2 = sqrt(v1^2 + v2^2 + ... + vn^2)
```

Represents:
Distance from origin.

---

## L1 Norm (Manhattan)

```
||v||1 = |v1| + |v2| + ... + |vn|
```

Represents:
Grid distance.

Used in:

* Lasso regularization
* Sparsity models

---

# 4. Matrix Operations

## Matrix Addition

Element-wise addition.

Same shape required.

---

## Matrix Multiplication

If:
A shape = (m, n)
B shape = (n, p)

Result shape:
(m, p)

Formula:

```
C[i][j] = Σ A[i][k] * B[k][j]
```

Geometric meaning:
Matrix = transformation.

Matrix multiplication = combining transformations.

Important:
Matrix multiplication is NOT commutative.

AB ≠ BA

---

## Transpose

Swap rows and columns.

Shape:
(m, n) → (n, m)

---

# 5. Eigenvalues & Eigenvectors

Definition:

```
A v = λ v
```

v → eigenvector
λ → eigenvalue

Meaning:
Vector that does not change direction after transformation.

If:
λ > 1 → stretch
0 < λ < 1 → shrink
λ < 0 → flip direction

---

## Finding Eigenvalues

Solve:

```
det(A − λI) = 0
```

---

## Why Important?

Used in:

* PCA (Principal Component Analysis)
* Covariance matrices
* Stability analysis
* Markov chains

In PCA:
Largest eigenvalue → direction of maximum variance.

---

# 6. Tensors in PyTorch

## Creating Tensors

```python
import torch

x = torch.tensor([1., 2., 3.])
```

---

## Basic Operations

```python
x + y          # element-wise
x * y          # element-wise
torch.dot(x,y) # dot product
torch.matmul(A,B) # matrix multiplication
```

---

## Shapes

Always inspect shape:

```python
print(x.shape)
```

Shape awareness = ML maturity.

---

# 7. Broadcasting

Allows operations between different shapes.

Rules:

1. Compare from right to left.
2. Dimensions must match OR be 1.

Example:
(2, 2)
(2,) → treated as (1, 2)

---

# 8. Autograd (PyTorch)

```python
x = torch.tensor(2.0, requires_grad=True)

y = x**2 + 3*x
y.backward()

print(x.grad)
```

Automatic gradient computation.

Foundation of deep learning.

---

# 9. Core ML Connections

Matrix multiplication → neural network layers
Dot product → similarity & attention
Eigenvectors → PCA
Norms → regularization
Broadcasting → bias addition in layers
Tensors → everything in DL

---

# 10. Mental Models

Matrix = transformation
Eigenvector = stable direction
Eigenvalue = stretch factor
Tensor = data container for ML computation

---
