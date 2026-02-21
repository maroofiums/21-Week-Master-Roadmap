# Week2 Day1

---

## **1. Scalars vs Vectors**

**Scalar**

* A scalar is just a single number.
* It only has **magnitude**, no direction.
* Examples: `5` (temperature), `10 kg` (weight), `3.14` (pi)

**Vector**

* A vector has both **magnitude and direction**.
* Represented as a list/array of numbers: `[x, y]` in 2D, `[x, y, z]` in 3D.
* Examples:

  * Velocity: `5 m/s north` → `[5, 0]`
  * Force in 3D: `[2, 3, -1]`

**Visual intuition:**
Think of a vector as an **arrow** pointing somewhere.

* Length of the arrow → magnitude
* Direction → the vector’s direction

---

## **2. Vector Operations**

### **2.1 Addition & Subtraction**

* **Addition:** Move one vector to the tip of the other, draw arrow from origin → tip.

  * Formula: `[x1, y1] + [x2, y2] = [x1+x2, y1+y2]`
* **Subtraction:** Flip the vector you subtract, then add.

  * Formula: `[x1, y1] - [x2, y2] = [x1-x2, y1-y2]`

**Example:**

```
u = [2, 3]
v = [1, 4]
u + v = [3, 7]
u - v = [1, -1]
```

**Intuition:** Addition = combining, subtraction = difference

---

### **2.2 Scalar Multiplication**

* Multiply a vector by a scalar → stretch/shrink its length.
* Formula: `k * [x, y] = [k*x, k*y]`
* Example: `2 * [3, 4] = [6, 8]`

**Visual:** The vector points in the same direction but gets longer or shorter.

---

## **3. Dot Product**

**Definition:**

* Combines two vectors into a single number (scalar).
* Formula:
  [
  u \cdot v = u_1 v_1 + u_2 v_2 + ... + u_n v_n
  ]

**Geometric meaning:**
[
u \cdot v = |u||v|\cos\theta
]

* `|u|` = magnitude of u
* `|v|` = magnitude of v
* `θ` = angle between them

**Use:**

* Measures similarity or alignment of vectors
* If `dot = 0` → vectors are perpendicular

**Example:**

```
u = [1, 2]
v = [3, 4]
dot = 1*3 + 2*4 = 11
```

---

## **4. Vector Norms (Length of a vector)**

**L2 norm (Euclidean length):**
[
||v||_2 = \sqrt{x^2 + y^2 + z^2 + ...}
]

* Think of it as distance from origin.

**L1 norm (Manhattan distance):**
[
||v||_1 = |x| + |y| + |z| + ...
]

* Sum of absolute values (like walking along grid streets in a city)

**Example:**

```
v = [3, 4]
||v||2 = sqrt(3^2 + 4^2) = 5
||v||1 = |3| + |4| = 7
```

---

## **5. Cross Product (3D only)**

**Definition:**

* Produces a new vector perpendicular to two given vectors
* Formula (for 3D):
  [
  u × v = [u_2 v_3 - u_3 v_2, u_3 v_1 - u_1 v_3, u_1 v_2 - u_2 v_1]
  ]

**Intuition:**

* Imagine two arrows in space → cross product gives an arrow **sticking out perpendicular** to the plane they form.
* Magnitude = area of the parallelogram spanned by u and v

**Example:**

```
u = [1, 2, 3]
v = [4, 5, 6]
cross = [-3, 6, -3]
```

---

## **6. Visual Intuition**

* **2D vectors:** arrows in a plane
* **Dot product:** angle between arrows (if dot=0 → 90°)
* **Cross product:** 3D, arrow perpendicular to both

---