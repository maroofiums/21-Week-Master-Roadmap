# Week1 - Day4

## 🔹 1. Lambda Functions

A **lambda function** is a small anonymous function written in one line.

### Syntax:

```python
lambda arguments: expression
```

### Example:

```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

---

## 🔹 2. `map()` Function

`map()` applies a function to every item in an iterable (like a list).

### Syntax:

```python
map(function, iterable)
```

### ✅ Practice: Square all numbers in a list

```python
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))

print(squared)
# Output: [1, 4, 9, 16, 25]
```

---

## 🔹 3. `filter()` Function

`filter()` selects items from an iterable based on a condition.

### Syntax:

```python
filter(function, iterable)
```

### ✅ Practice: Filter all even numbers from a list

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
# Output: [2, 4, 6, 8]
```

---

## 🔹 4. `reduce()` Function

`reduce()` applies a function cumulatively to items.

It is in the `functools` module.

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)  # Output: 10
```

👉 It reduces the list to a single value.

---

## 🔹 5. Decorators (Basic Idea)

A **decorator** is a function that modifies another function.

### Basic Structure:

```python
def decorator_function(original_function):
    def wrapper():
        print("Something before the function runs")
        original_function()
        print("Something after the function runs")
    return wrapper
```

### Using It:

```python
@decorator_function
def say_hello():
    print("Hello!")

say_hello()
```

---

## ✅ Practice: Create a Decorator to Time Function Execution

```python
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        
        result = func(*args, **kwargs)
        
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        
        return result
    return wrapper


@timer_decorator
def slow_function():
    time.sleep(2)
    print("Function finished")


slow_function()
```

✔ This decorator measures how long a function takes to run.

---

## 🔹 6. Exception Handling (`try/except`)

Used to handle runtime errors without crashing the program.

### Basic Example:

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError:
    print("You cannot divide by zero!")

except ValueError:
    print("Invalid input! Please enter a number.")

finally:
    print("Done!")
```

* `try` → code that might cause error
* `except` → handles the error
* `finally` → always runs

---

## 🎯 Summary – Day 4

You learned:

* ✅ Lambda functions
* ✅ `map()`
* ✅ `filter()`
* ✅ `reduce()`
* ✅ Decorators (basic concept)
* ✅ Exception handling

---
