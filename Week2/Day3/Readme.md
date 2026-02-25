# Day3

## 1. What is an Eigenvector?

For a matrix **A**, an eigenvector **v** is a special vector that:

When multiplied by A:

```
A v = λ v
```

It **does not change direction** —
It only gets **scaled** (stretched or shrunk).

* `v` → eigenvector
* `λ` (lambda) → eigenvalue (scaling factor)

---

## 2. Geometric Meaning (2D Intuition)

Normally, when a matrix transforms a vector:

* Direction changes
* Length changes

But for eigenvectors:

* Direction stays same
* Only magnitude changes

So eigenvectors are **special directions of transformation**.

---

## 3. Simple 2×2 Example

Let’s take:

[
A =
\begin{bmatrix}
2 & 0 \
0 & 1
\end{bmatrix}
]

This matrix:

* Stretches x-direction by 2
* Leaves y-direction unchanged

### Eigenvectors:

1. ( v_1 = [1,0] )
2. ( v_2 = [0,1] )

### Eigenvalues:

* λ₁ = 2
* λ₂ = 1

Why?

```
A [1,0] = [2,0] = 2[1,0]
A [0,1] = [0,1] = 1[0,1]
```

Direction unchanged → eigenvector confirmed.

---

## 4. Let’s VISUALIZE in 2D (Matplotlib)

You can run this in Jupyter.

```python
import numpy as np
import matplotlib.pyplot as plt

# Define matrix
A = np.array([[2, 0],
              [0, 1]])

# Define vectors
v1 = np.array([1, 0])   # eigenvector 1
v2 = np.array([0, 1])   # eigenvector 2

# Transform vectors
Av1 = A @ v1
Av2 = A @ v2

# Plot
plt.figure()

# Original vectors
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1)
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1)

# Transformed vectors
plt.quiver(0, 0, Av1[0], Av1[1], angles='xy', scale_units='xy', scale=1)
plt.quiver(0, 0, Av2[0], Av2[1], angles='xy', scale_units='xy', scale=1)

plt.xlim(-3,3)
plt.ylim(-3,3)
plt.axhline(0)
plt.axvline(0)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.title("Eigenvector Transformation")
plt.show()
```

What you'll see:

* x-axis vector doubles
* y-axis vector stays same
* No direction change

That’s eigen behavior.

---

## 5. More Interesting Example (Rotation + Scaling)

Now take:

[
A =
\begin{bmatrix}
3 & 1 \
0 & 2
\end{bmatrix}
]

Now directions will change for most vectors.

Let’s compute eigenvalues & eigenvectors:

```python
A = np.array([[3,1],
              [0,2]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
```

Each column of `eigenvectors` is an eigenvector.

---

## 6. Why ML Engineers Care

Eigenvectors appear in:

### 1. PCA (Principal Component Analysis)

Covariance matrix → eigenvectors give **principal directions**

### 2. SVD

Used in:

* Recommender systems
* NLP embeddings
* Dimensionality reduction

### 3. Stability of Systems

In deep learning optimization.

---

## 7. Geometric Summary

Think of a matrix as:

“Space deformation machine”

Most vectors:

* Rotate
* Stretch
* Change direction

Eigenvectors:

* Stay aligned
* Only scale

Eigenvalues:

* Tell how much stretching

---

## 8. Important Concept (Very Important for You)

If:

* λ > 1 → stretching
* 0 < λ < 1 → shrinking
* λ < 0 → flip direction
* λ = 0 → collapse to zero

---

## 9. Mental Picture

Imagine pressing a rubber sheet.

Most arrows change direction.

But two special arrows remain straight.
Those are eigenvectors.

---
