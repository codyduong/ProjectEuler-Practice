"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math
import itertools

def pytrip(n):
    triplets = []
    for a in range(1, n//2):
        for b in range(1, n//2):
            c = (a**2) + (b**2)
            if c**.5 == math.floor(c**.5):
                triplets.append([a, b, int(c**.5)])
                
    print(triplets)
    result = itertools.filterfalse(lambda x: x[0]+x[1]+x[2]!=n, triplets)
    for each in result:
        print(each, each[0]*each[1]*each[2])

if __name__ == "__main__":
    pytrip(int(input()))
