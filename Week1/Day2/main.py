def SumEven(n):
    sum = 0 
    for i in range(1, n+1):
        if i % 2 == 0:
            sum += i
    return sum

def count_vowel(s):
    count = 0
    for char in s:
        if char in 'aeiouAEIOU':
            count += 1
    return count

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

if __name__ == "__main__":
    n = 10
    print(f"Sum of even numbers from 1 to {n}: {SumEven(n)}")

    s = "Hello World"
    print(f"Number of vowels in '{s}': {count_vowel(s)}")

    n = 10
    print(f"The {n}th Fibonacci number: {fibonacci(n)}")

