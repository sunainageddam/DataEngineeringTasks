""" Create a list containing the numbers 1 through 100. Use the ﬁlter()
function to create a new list containing only the prime numbers from the
original list. Use the reduce() function to calculate the sum of the
prime numbers in the new list. Print the sum to the console in python.
"""

from functools import reduce

numbers = list(range(1, 101))
def is_prime(n):
    flag = False
    if n < 2:
        return False
    for i in range(2, n):
            if (n % i) == 0:
                flag = True
                break
    if flag:
        return False
    else:
        return True 
primes = list(filter(is_prime, numbers))
print(primes)
sum_of_primes = reduce(lambda x,y: x+y, primes)

print(sum_of_primes)
