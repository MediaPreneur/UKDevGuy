"""
Recrusive implementation of the fibonacci function.
The fibonacci sequence is defined as "a series of
numbers in which each number (Fibonacci number)
is the sum of the two preceding numbers"
"""

def fib(num):
    # First two fibonacci numbers are 1
    return 1 if num in [1, 2] else fib(num-1) + fib(num-2)


# Output the first 10 numbers
for n in range(1, 11):
    print("fib(", n, ") =", fib(n))