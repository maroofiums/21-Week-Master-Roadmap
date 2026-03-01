# 🔵 Week 3 - Probability & Statistics

Goal: Think probabilistically like an ML scientist.

---

# 🟢 Day 1 - Probability Foundations

### 🎯 Goal:

Understand how probability works mathematically and conceptually.

### Topics:

* Sample space & events
* Basic probability rules
* Complement rule
* Addition rule
* Multiplication rule
* Independence vs dependence

### Deep Understanding:

* What does it mean for events to be independent?
* Why does P(A ∩ B) change if events are dependent?

### Practice:

* Coin toss probability problems
* Card deck problems
* Dice problems
* Solve 10 manual probability questions

### Coding:

Simulate coin toss and dice probability using NumPy.

---

# 🟢 Day 2 - Conditional Probability & Bayes Theorem

### 🎯 Goal:

Understand belief updating.

### Topics:

* Conditional probability
* P(A|B) vs P(B|A)
* Bayes theorem derivation
* Real-world examples (medical testing)

### Deep Thinking:

* Why is P(disease|positive test) NOT same as P(positive|disease)?
* How does prior probability affect result?

### Practice:

* Solve 5 Bayes theorem word problems
* Implement Bayes formula in Python

### Coding:

Simulate disease testing with probabilities and observe outcomes.

This day is critical for ML classification.

---

# 🟢 Day 3 - Random Variables & Distributions

### 🎯 Goal:

Understand discrete vs continuous randomness.

### Topics:

* Random variables
* PMF vs PDF
* Binomial distribution
* Poisson distribution
* Normal distribution

### Deep Understanding:

* When to use Binomial?
* Why Poisson models rare events?
* Why Normal appears everywhere?

### Practice:

* Calculate binomial probability manually
* Simulate binomial trials
* Plot normal curve

### Coding:

Generate and visualize:

* Binomial distribution
* Poisson distribution
* Normal distribution

---

# 🟢 Day 4 - Expectation, Variance, Covariance, Correlation

### 🎯 Goal:

Measure average and spread mathematically.

### Topics:

* Expectation
* Variance
* Standard deviation
* Covariance
* Correlation

### Deep Understanding:

* Why variance squares differences?
* Why correlation is normalized covariance?
* Why correlation ranges between -1 and 1?

### Practice:

* Compute mean and variance manually
* Derive variance formula E[X²] − (E[X])²

### Coding:

* Load small dataset
* Compute covariance matrix
* Plot correlation heatmap

This day directly connects to PCA (Week 2 link).

---

# 🟢 Day 5 - Sampling & Central Limit Theorem

### 🎯 Goal:

Understand why normal distribution dominates statistics.

### Topics:

* Population vs sample
* Sampling distributions
* Law of Large Numbers
* Central Limit Theorem (CLT)

### Deep Understanding:

* Why does sample mean become normal?
* Why is CLT extremely important for ML evaluation?

### Practice:

* Draw random samples from non-normal distribution
* Compute sample means repeatedly

### Coding:

Simulate:

* Draw 1000 samples
* Plot distribution of sample means
* Observe bell curve formation

This is a “wow” moment if done properly.

---

# 🟢 Day 6 - Statistical Tests (Hypothesis Testing)

### 🎯 Goal:

Learn decision making using statistics.

### Topics:

* Null hypothesis (H0)
* Alternative hypothesis (H1)
* p-value
* t-test
* Chi-square test

### Deep Understanding:

* What does p-value really mean?
* Why 0.05 threshold?
* When to use t-test vs chi-square?

### Practice:

* Compare two sample means manually
* Perform t-test using scipy
* Perform chi-square on categorical data

This is useful in:

* A/B testing
* Model comparison
* Feature selection

---

# 🟢 Day 7 - Full Revision + Applied ML Thinking

### 🎯 Goal:

Consolidate everything.

### Self-Test Questions:

1. Explain Bayes theorem without formula.
2. Why does CLT justify normal approximation?
3. Difference between covariance and correlation?
4. When to use Poisson instead of Binomial?
5. What does variance measure intuitively?
6. Why do ML models output probabilities?

### Mini Project:

Build:

Probability Simulation Notebook:

* Coin toss
* Dice
* Binomial experiment
* CLT simulation
* Correlation heatmap

Make it clean & GitHub-ready.

---

# 🧠 What Week 3 Should Change In You

After this week:

You should:

* Think in uncertainty
* Understand probabilistic reasoning
* Be comfortable reading distributions
* Understand variance mathematically
* Connect stats to ML evaluation

---

# 🔥 Important ML Connections

* Logistic regression → probability modeling
* Naive Bayes → Bayes theorem
* Loss functions → expectation
* Regularization → variance control
* PCA → covariance matrix
* Evaluation metrics → statistical testing
