def fibonacciFirst(n):
    
    if not isinstance(n, int):
        return TypeError("Invalid input - Input must be an integer")
    if n < 0:
        return TypeError("Invalid input - Input must be a positive integer")
    sequence = [0, 1]  # Initialize the sequence with the first two numbers
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]  # Calculate the next number
        sequence.append(next_number)  # Add the next number to the sequence
    return sequence

def fibonacci(n):
    p = fibonacciFirst(n)
    #print(p)
    if n == 0:
        return p[n]
    else:
        return p[n-1]
    

""""
# Test the function
n = 0  # Number of Fibonacci numbers to generate
result = fibonacci(n)
print(result)


# Celsius to Fahrenheit
print(CelesiusToFahrenheit(54))
print(FahrenheitToCelsius(-80))
"""

def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        return TypeError("Invalid input - Input must be an integer or float")
    if celsius < -273.15:
        return ValueError("Invalid input - Temperature cannot be less than -273.15°C")
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        return TypeError("Invalid input - Input must be an integer or float")
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def is_prime(n):
    if not isinstance(n, int):
        return TypeError("Invalid input")
    if n <= 0:
        return False
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

"""
print(primes_in_range(12, 13))

print(is_prime(1))
print(is_prime(2))
print(is_prime(0))
print(is_prime("a"))

print(primes_in_range(0, 11))

print("Hello World")

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test the function
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubblesort(arr))

twoDimArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(twoDimArray[1][1])

"""