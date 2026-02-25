# Week2 Day4

## 1. What Is a Tensor?

A tensor is just a generalization of:

* Scalar → 0D tensor
* Vector → 1D tensor
* Matrix → 2D tensor
* 3D array → 3D tensor
* n-dimensional array → nD tensor

So mathematically:

Tensor = multidimensional array

In deep learning:
Everything is a tensor.

Images, text embeddings, batches of data, model weights — all tensors.

---

## 2. Tensor Dimensions (Very Important)

Example shapes:

Scalar:
5
Shape: ()

Vector:
[1, 2, 3]
Shape: (3,)

Matrix:
[[1, 2],
[3, 4]]
Shape: (2, 2)

Image (RGB 32×32):
Shape: (3, 32, 32)

Batch of 64 images:
Shape: (64, 3, 32, 32)

You must train your brain to read shapes instantly.

Shape reading skill = advanced ML thinking.

---

## 3. Tensors in PyTorch

### Creating Tensors

```python
import torch

# Scalar
a = torch.tensor(5)

# Vector
v = torch.tensor([1, 2, 3])

# Matrix
m = torch.tensor([[1, 2],
                  [3, 4]])

print(v.shape)
print(m.shape)
```

---

### Basic Operations

```python
x = torch.tensor([1.0, 2.0])
y = torch.tensor([3.0, 4.0])

# Addition
print(x + y)

# Element-wise multiplication
print(x * y)

# Dot product
print(torch.dot(x, y))

# Matrix multiplication
A = torch.tensor([[1., 2.],
                  [3., 4.]])

B = torch.tensor([[5., 6.],
                  [7., 8.]])

print(torch.matmul(A, B))
```

Important difference:

* * → element-wise
* matmul() → matrix multiplication

---

## 4. Tensors in TensorFlow

Very similar idea.

```python
import tensorflow as tf

x = tf.constant([1.0, 2.0])
y = tf.constant([3.0, 4.0])

print(x + y)
print(tf.tensordot(x, y, axes=1))
```

Matrix multiplication:

```python
A = tf.constant([[1., 2.],
                 [3., 4.]])
B = tf.constant([[5., 6.],
                 [7., 8.]])

print(tf.linalg.matmul(A, B))
```

---

## 5. Broadcasting (Extremely Important)

Broadcasting allows operations between tensors of different shapes.

Example:

```python
x = torch.tensor([[1, 2],
                  [3, 4]])

y = torch.tensor([10, 20])

print(x + y)
```

Result:
[[11, 22],
[13, 24]]

What happened?

Tensor y was automatically expanded to match rows.

Broadcasting rules (simplified):

* Shapes must match from right to left
* One of the dimensions must be 1

Example:

(2, 2)
(2,) → treated as (1, 2)

This concept is used everywhere in neural networks.

---

## 6. Why Tensors Matter in Deep Learning

Neural network layer:

y = Wx + b

Where:

W → matrix (2D tensor)
x → input vector (1D tensor)
b → bias vector

Everything is tensor math.

Training = repeated tensor operations + gradient computation.

---

## 7. Autograd (Why PyTorch Is Powerful)

PyTorch can compute gradients automatically.

```python
x = torch.tensor(2.0, requires_grad=True)

y = x**2 + 3*x

y.backward()

print(x.grad)
```

This computes derivative automatically.

That is the backbone of deep learning.

Without tensors, no neural networks.

---

