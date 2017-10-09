import itertools

def primes():
    number = 1
    while True:
        divisors = 0
        number += 1
        for i in range(1, number+1):
            if number % i == 0:
                divisors += 1
        if divisors < 3 :
            yield number

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
