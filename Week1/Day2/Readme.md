# Week 1 — Day 2: Loops & Functions

This lesson covers basic looping constructs, comprehensions, and function definitions in Python, plus three short practice exercises.

## Topics

- Loops: `for`, `while` — iterating over ranges, lists, and other iterables.
- List comprehensions & dictionary comprehensions — concise construction of lists and dicts.
- Functions: `def`, `return`, parameters, and default arguments — building reusable code blocks.

## Practice Exercises

Implement the following functions to practise loops, comprehensions, and functions. You can add these to `main.py` or create a new module.

1) Sum all even numbers in a list

   - Goal: Given a list of integers, return the sum of all even values.
   - Example implementation:

   ```python
   def sum_even(numbers: list[int]) -> int:
	   return sum(x for x in numbers if x % 2 == 0)
   ```

2) Count vowels in a string

   - Goal: Count vowel characters (`a, e, i, o, u`) in a string (case-insensitive).
   - Example implementation:

   ```python
   def count_vowels(s: str) -> int:
	   return sum(1 for ch in s.lower() if ch in 'aeiou')
   ```

3) Fibonacci sequence generator

   - Goal: Produce Fibonacci numbers. Try both a generator version and a function that returns the nth value (prefer iterative approaches to avoid recursion limits).
   - Example generator:

   ```python
   def fibonacci_generator(n: int):
	   a, b = 0, 1
	   for _ in range(n):
		   yield a
		   a, b = b, a + b
   ```

   - Example nth-value (iterative):

   ```python
   def fibonacci_n(n: int) -> int:
	   a, b = 0, 1
	   for _ in range(n):
		   a, b = b, a + b
	   return a
   ```

## Running the examples

Run the repository's `main.py` to see simple demo outputs:

```
python main.py
```


