def primes():
    number = 2
#    print("BEFORE while")
    while True:
#        print("IN while")
        divisors = 0
        for i in range(1, number+1):
            if number % i == 0:
                divisors += 1
#        print("number = " + number)
#        print("divisors" + divisors)
        if divisors < 3 :
            yield number
        else:
            number += 1

for j in range (30):
    print(primes())
