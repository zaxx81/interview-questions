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
        if temp == 1:
            break
        aggregate *= temp
        upper_factor = int(upper_factor / temp)
    
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
    if not n % 2:
        return 2

    end_range = int(n / 2) + 1

    for i in range(3, end_range):
        if is_prime(i) and is_factor(n, i):
            return i
    return 1


@timer_func
def test_case():
    # print(is_prime(999998727899999)) # largest 12-digit prime number
    # print(is_prime(1000000000100011)) # first 16-digit prime number
    # print(is_prime(10089886811898868001)) # first 20-digit prime number
    
    print(largest_prime_factor(600851475143))

test_case()