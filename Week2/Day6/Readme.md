# Week1 Day6

---

# **1. Vector Projections**

The projection of vector **v** onto vector **w**:

[
\text{proj}_w(v) = \frac{v \cdot w}{||w||^2} w
]

Python implementation:

```python
import numpy as np

def vector_projection(v, w):
    w = np.array(w)
    v = np.array(v)
    scalar = np.dot(v, w) / np.dot(w, w)
    return scalar * w
```

**Example:**

```python
v = [3, 4]
w = [2, 1]
proj = vector_projection(v, w)
print("Projection of v onto w:", proj)
```

---

# **2. Angle Between Two Vectors**

Formula:

[
\theta = \arccos\left(\frac{v \cdot w}{||v|| , ||w||}\right)
]

```python
def angle_between(v, w):
    v = np.array(v)
    w = np.array(w)
    cos_theta = np.dot(v, w) / (np.linalg.norm(v) * np.linalg.norm(w))
    return np.arccos(np.clip(cos_theta, -1, 1))  # Clip avoids numerical errors

v = [3, 4]
w = [2, 1]
theta = angle_between(v, w)
print("Angle (radians):", theta)
print("Angle (degrees):", np.degrees(theta))
```

---

# **3. 2D Vector Plotting**

```python
import matplotlib.pyplot as plt

v = [3, 4]
w = [2, 1]
proj = vector_projection(v, w)

plt.figure(figsize=(6,6))
origin = [0, 0]

plt.quiver(*origin, *v, color='r', scale=1, scale_units='xy', angles='xy', label='v')
plt.quiver(*origin, *w, color='b', scale=1, scale_units='xy', angles='xy', label='w')
plt.quiver(*origin, *proj, color='g', scale=1, scale_units='xy', angles='xy', label='proj of v on w')

plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.grid()
plt.legend()
plt.show()
```

* Red: **v**
* Blue: **w**
* Green: **projection of v on w**

---

# **4. 3D Vector Plotting**

```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

v = [1, 2, 3]
w = [3, 1, 2]

ax.quiver(0,0,0,*v, color='r', label='v')
ax.quiver(0,0,0,*w, color='b', label='w')

ax.set_xlim([0,4])
ax.set_ylim([0,4])
ax.set_zlim([0,4])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
```

---

# **5. Summary / Insights**

1. **Projection** → shows how much of one vector aligns with another
2. **Angle** → cosine similarity; core idea in ML embeddings and similarity measures
3. **2D plotting** → helps understand vector relationships visually
4. **3D plotting** → scales intuition to higher dimensions

---