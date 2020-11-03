import itertools
import math

def isprime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i: int = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(s):
    if s%2 == 0: #input is even?
        factors = [1, 2]
        s_number = 3
    else:
        factors = []
        s_number = 1
    for i in range(s_number, math.ceil(s**0.5), 2): #sqrt of s, because you only need first half of factors, derive second half by s//i
        if s%i == 0:
            #print("checking", i)
            if len(factors)>=2:
                for j in range(1, len(factors)):
                    if i%factors[j] == 0: #removes any numbers that are a factor of the factors (making it not prime)
                        break
                    else:
                        factors.append(i)
                        print(factors)
                        break
                for j in range(1, len(factors)):
                    #print("checking", s//i)
                    if s//i%factors[j] == 0: #removes any numbers that are a factor of the factors (making it not prime)
                        break
                    else:
                        factors.append(s//i)
                        print(factors)
                        break
            else:
                factors.append(i)
                print(factors)

    factors.sort()
    print(factors)

    for i in range(len(factors)-1, -1, -1):
        if isprime(factors[i]):
            return factors[i]


if __name__ == "__main__":
    print(prime_factors(int(input())))
