import time

square = lambda x: x * x
print(square(5))

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(square, numbers))
print(squared_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

def decorator(func):
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper

@decorator
def say_hello():
    print("Hello!")
    
say_hello()

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
    return wrapper

@time_decorator
def long_running_function():
    time.sleep(2)
    print("Finished long running function.")
long_running_function()

try:
    num = int(input("Enter a number: "))
    print(10/num)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
finally:
    print("This will always execute.")
    