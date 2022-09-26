from functools import lru_cache

@lru_cache()

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

for i in range(500):
    print(f"{i} : {fib(i)}")