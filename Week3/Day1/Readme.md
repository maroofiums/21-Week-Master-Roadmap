# 🟢 Day 1 — Probability Foundations (Deep Understanding Mode)

Forget formulas for a moment.

Probability is about **uncertainty + structure**.

---

# 1️⃣ What is Probability Really?

Probability measures how likely something is to happen.

Mathematically:

[
P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total possible outcomes}}
]

But this only works when outcomes are equally likely.

---

# 2️⃣ Sample Space (Ω)

The **sample space** is the set of all possible outcomes.

### Example: Toss a coin

[
\Omega = {H, T}
]

### Example: Roll a die

[
\Omega = {1,2,3,4,5,6}
]

Everything in probability starts here.

If your sample space is wrong → everything is wrong.

---

# 3️⃣ Events

An event is a subset of the sample space.

Example (die):

* Event A = “roll even”
* A = {2,4,6}

Probability:

[
P(A) = 3/6 = 1/2
]

---

# 4️⃣ Core Probability Rules

These are fundamental. Not optional.

---

## 🔹 Rule 1: Complement Rule

[
P(A^c) = 1 - P(A)
]

If probability of rain is 0.3
Probability of no rain = 0.7

Total probability must equal 1.

Why?
Because something either happens or it doesn’t.

---

## 🔹 Rule 2: Addition Rule

If A and B cannot happen together:

[
P(A \cup B) = P(A) + P(B)
]

Example:
Rolling a die:
P(1 or 2) = 1/6 + 1/6 = 2/6

---

### If they CAN happen together:

[
P(A \cup B) = P(A) + P(B) - P(A \cap B)
]

Why subtract?

Because we double counted the overlap.

This concept is crucial for ML (especially in classification overlaps).

---

## 🔹 Rule 3: Multiplication Rule

If events are independent:

[
P(A \cap B) = P(A)P(B)
]

Example:
Two coin tosses:
P(H and H) = 0.5 × 0.5 = 0.25

---

# 5️⃣ Independence (VERY Important for ML)

Two events A and B are independent if:

[
P(A \cap B) = P(A)P(B)
]

This means:

The outcome of one does NOT affect the other.

---

### Example of Independent Events:

* Toss coin
* Roll die

Coin does not influence die.

---

### Example of Dependent Events:

* Pick a card
* Don’t replace it
* Pick again

Now probabilities change.

Dependency is extremely important in:

* Naive Bayes
* Bayesian networks
* Feature independence assumptions

---

# 6️⃣ Why Independence Matters in ML

Naive Bayes assumes:

Features are conditionally independent given the class.

That assumption simplifies:

[
P(x_1, x_2, ..., x_n | y)
]

into:

[
P(x_1|y)P(x_2|y)...P(x_n|y)
]

Without independence → exponential complexity.

---

# 7️⃣ Visual Intuition (Think in Areas)

Imagine probability as area in a rectangle of size 1.

* Whole space = area 1
* Event A = some region
* Event B = another region
* Overlap = intersection

This is why:
[
P(A \cup B) = P(A) + P(B) - P(A \cap B)
]

You’re subtracting overlapping area.

---

# 8️⃣ Conceptual Questions (Answer Mentally)

1. If P(A) = 0.7, can P(A ∩ B) be 0.8?
2. If P(A) = 0.5 and P(B) = 0.5, are they automatically independent?
3. If two events are independent, can they overlap?
4. What happens to multiplication rule if events are dependent?

Think before scrolling.

---

# Answers

1️⃣ No. Intersection can’t exceed individual probability.
2️⃣ No. Independence requires product condition.
3️⃣ Yes. Overlap can exist while independent.
4️⃣ We must use:
[
P(A \cap B) = P(A|B)P(B)
]

---

# 9️⃣ Python Practice (Simulation)

Try this:

```python
import numpy as np

# Simulate 100,000 coin tosses
n = 100000
coin = np.random.choice(['H', 'T'], size=n)

# Estimate P(H)
p_h = np.mean(coin == 'H')
print("Estimated P(H):", p_h)
```

Now simulate two tosses and estimate:

P(H and H)

Compare with theoretical 0.25.

This builds intuition for:

Law of Large Numbers (Day 5).

---
