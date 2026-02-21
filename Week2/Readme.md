## **Week 2: Linear Algebra & Vectors**

**Goal:** Build a strong linear algebra foundation for ML/DL. This will help you understand how models compute, how data transforms, and how optimization works.

---

### **Topics to Cover**

1. **Scalars, Vectors, Matrices, Tensors**

   * Scalar = single number
   * Vector = 1D array, e.g., `[1, 2, 3]`
   * Matrix = 2D array, e.g., `[[1, 2], [3, 4]]`
   * Tensor = N-dimensional array (generalization of vectors & matrices)

2. **Matrix Operations**

   * Addition & subtraction
   * Multiplication (dot product)
   * Transpose
   * Inverse (only for square matrices)
   * Determinant
   * Identity matrix & diagonal matrices

3. **Vector Operations**

   * Dot product & cross product
   * Norms (L1, L2)
   * Projection of one vector onto another
   * Angle between vectors

4. **Eigenvalues & Eigenvectors**

   * What they are & why they matter in ML (PCA, covariance matrices)
   * Compute simple examples by hand

5. **Tensors in ML Frameworks**

   * PyTorch: `torch.tensor()`, `torch.matmul()`, broadcasting
   * TensorFlow: `tf.constant()`, `tf.linalg.matmul()`

---

### **Practice / Mini Projects**

1. **Vector & Matrix Operations in Python**

   * Implement addition, subtraction, dot product, cross product **from scratch**
   * Verify with NumPy

2. **Matrix Inversion & Determinant**

   * Compute determinant and inverse of 2x2 and 3x3 matrices manually
   * Compare with `numpy.linalg.inv()` & `numpy.linalg.det()`

3. **Eigenvectors & Eigenvalues**

   * Simple 2x2 matrix example
   * Visualize eigenvectors as directions of stretching

4. **PyTorch / TensorFlow Tensors**

   * Create 2D and 3D tensors
   * Perform basic operations (add, multiply, transpose)
   * Apply simple broadcasting

5. **Visualization**

   * Plot vectors in 2D/3D with Matplotlib
   * Show projections and angles between vectors

---

### **Daily Schedule Suggestion (2–4 hrs/day)**

| Day   | Task                                                                             |
| ----- | -------------------------------------------------------------------------------- |
| Day 1 | Scalars, vectors, norms, dot/cross products, small exercises                     |
| Day 2 | Matrices: addition, multiplication, transpose, determinant, inverse              |
| Day 3 | Eigenvectors & eigenvalues, visualize with 2D plots                              |
| Day 4 | Introduction to tensors in PyTorch/TensorFlow, basic operations                  |
| Day 5 | Mini project: implement vector & matrix operations from scratch, test with NumPy |
| Day 6 | Visualizations: vector projections, angles, 2D/3D plotting                       |
| Day 7 | Revision & small test: linear algebra exercises + tensor practice                |

---

### **Tips**

* Focus on **understanding concepts visually**—e.g., vectors as arrows in space.
* Linear algebra is **core to ML/DL**, so don’t rush. A solid foundation here will make Week 4 (Gradient Descent & Optimization) much easier.
* Always check your **manual calculations** against NumPy/PyTorch to build confidence.
