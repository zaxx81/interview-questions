import math
from re import I

from time import time
  
def timer_func(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

# 
def largest_prime_factor(n):
    aggregate = 1
    upper_factor = n
    
    while aggregate != n:
        temp = smallest_prime_factor(upper_factor)
        if temp == upper_factor:
            return upper_factor
        aggregate *= temp
        upper_factor = int(upper_factor / temp)
        
        # print(aggregate)
        # print(f'Smallest Prime Factor: {temp}')
        # print(f'Upper Factor: {upper_factor}')
    
    return upper_factor

# Determines if i is a factor of n
def is_factor(n, i):
    return not n%i

# Determines if n is a prime number using 6k+-1 optimization, aka Primality test
def is_prime(n):
    if n <= 3:
        return n > 1
    
    if not n%2 or not n%3:
        return False
    
    i = 5
    stop = int(n**0.5)
    
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    
    return True

# Finds the smallest prime factor of n
def smallest_prime_factor(n):
    if n % 2 == 0:
        return 2

    i = 3
    while(i * i <= n):
        if n % i == 0:
            return i
        i +=2
    return n


@timer_func
def test_case():
    # print(is_prime(999998727899999)) # largest 12-digit prime number
    # print(is_prime(1000000000100011)) # first 16-digit prime number
    # print(is_prime(10089886811898868001)) # first 20-digit prime number
    
    # print(smallest_prime_factor(473)) # => 11

    
    # print(smallest_prime_factor(3784)) # => 2
    # print(smallest_prime_factor(1892)) # => 2
    # print(smallest_prime_factor(946)) # => 2
    # print(smallest_prime_factor(473)) # => 11
    # print(smallest_prime_factor(43)) # => 43
    # print(largest_prime_factor(3784)) # => 43
    # print(largest_prime_factor(600851475143)) # => 6857
    # print(largest_prime_factor(6008514751435)) # => 171671850041
    # print(largest_prime_factor(25698751364526)) # => 328513

    # print(largest_prime_factor(999999999999)) #12-digit arg is fast
    # print(largest_prime_factor(9999999999999)) #13-digit arg
    # print(largest_prime_factor(9999999999999)) #14-digit arg
    # print(largest_prime_factor(9999999999999)) #15-digit arg
    # print(largest_prime_factor(9999999999999)) #16-digit arg
    print(largest_prime_factor(99999999999999999999)) #20-digit arg

test_case()