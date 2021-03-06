from time import time
  
# This function shows the execution time of 
# the function object passed
def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

# The largest prime factor of n is as follows:
# 1. upper_factor = n
# 2. loop through:
# 2a. Find smallest_prime_number () of upper_factor
# 2b. Multiple aggregate by the smallest_prime_number ()
# 2c. Update upper_factor = upper_factor / smallest_prime_number ()
# 2d. Loop until smallest_prime_number() == upper_factor
def largest_prime_factor(n):
    aggregate = 1
    upper_factor = n
    
    while aggregate != n:
        temp = smallest_prime_factor(upper_factor)
        if temp == upper_factor:
            return upper_factor
        aggregate *= temp
        upper_factor = upper_factor / temp
    
    return int(upper_factor)

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
    # If even return 2
    if n % 2 == 0:
        return 2

    # Interate from 3 to sqrt(N)
    i = 3
    while(i * i <= n):
        # returns i if it is a factor of n
        if n % i == 0:
            return i
        # returns next odd number
        i +=2
    # If no prime factors return n
    return n

# Test cases with timer
@timer_func
def test_case(arg):
    return largest_prime_factor(arg)

print(test_case(2) == 2)
print(test_case(3) == 3)
print(test_case(3784) == 43)
print(test_case(600851475143) == 6857)
print(test_case(6008514751435) == 171671850041)
print(test_case(25698751364526) == 328513)
print(test_case(54654681351684) == 4554556779307) 
print(test_case(54684681352168) == 319831)
print(test_case(9007199254740991) == 20394401)
print(test_case(900719925474480991) == 4952856173)
