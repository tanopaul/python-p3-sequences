#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []
    for i in range(length):
        if len(fib) == 0:
            fib.append(i)
        elif len(fib) == 1:
            fib.append(i)
        else:
            num = fib[i - 2] + fib[i - 1]
            fib.append(num)
    print(fib)

print_fibonacci(9)