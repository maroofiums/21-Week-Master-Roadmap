# **Week 1 – Day 1: Python Basics**

**Goal:** Get comfortable with **Python data types, variables, operators, and conditionals**. This is the foundation for everything else in ML/DL.

**Time:** ~3–4 hours

---

## **Step 1: Python Data Types & Variables (45–60 min)**

**Topics to cover:**

* Numbers: int, float
* Strings: str, string operations
* Lists, Tuples, Sets, Dictionaries
* Variables and assignment

**Mini Examples:**

```python
# Numbers
a = 10         # int
b = 3.5        # float

# Strings
name = "Maroof"
print(name.upper())   # "MAROOF"
print(name[0])       # "M"

# List
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits[1])     # "banana"

# Tuple (immutable)
coords = (10, 20)

# Set
unique_nums = {1, 2, 3, 3}
print(unique_nums)    # {1,2,3}

# Dictionary
student = {"name": "Maroof", "age": 20}
print(student["age"])
```

**Practice Exercise:**

* Create variables for **your name, age, and favorite numbers**.
* Make a **list of 5 cities**, a **tuple of 3 coordinates**, a **set of 5 random numbers**, and a **dictionary for a student's info**.

---

## **Step 2: Python Operators (30 min)**

**Topics:**

* Arithmetic: `+ - * / % ** //`
* Comparison: `==, !=, >, <, >=, <=`
* Logical: `and, or, not`

**Mini Examples:**

```python
x = 10
y = 3

print(x + y)    # 13
print(x // y)   # 3
print(x ** y)   # 1000

# Comparison
print(x > y)    # True
print(x == y)   # False

# Logical
print(x > 5 and y < 5)  # True
print(not(x == y))       # True
```

**Practice Exercise:**

* Check if a number is **even or odd**.
* Compare your age with a friend’s and print who is older.
* Create a boolean expression using `and`, `or`, and `not`.

---

## **Step 3: Conditional Statements (45 min)**

**Topics:**

* `if`, `elif`, `else`

**Mini Examples:**

```python
age = 18

if age >= 18:
    print("You can vote")
elif age >= 16:
    print("You can drive")
else:
    print("You are too young")
```

**Practice Exercise:**

* Write a program to **grade a student**:

  * marks >= 90 → A
  * marks >= 75 → B
  * marks >= 60 → C
  * else → Fail
* Write a program to check if a **number is positive, negative, or zero**.

---

## **Step 4: Mini Project / Challenge (30–45 min)**

**Goal:** Apply what you learned in a small program

**Project Idea:** “Number Checker”

* Input a number from the user
* Check if it is **positive, negative, or zero**
* Check if it is **even or odd**

```python
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Optional Challenge:**

* Ask for **two numbers**, then print which one is bigger.
* Try **nested if-else** statements for multiple conditions.

---

### ✅ **Day 1 Summary**

1. Understand **data types & variables**.
2. Practice **operators** for arithmetic, comparison, and logic.
3. Learn **if-elif-else** for decision-making.
4. Complete a **mini project** (number checker).
