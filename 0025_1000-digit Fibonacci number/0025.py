# this is done in python because bignum is handled easier than in most others
import math

stored = [1,1]
iteration = 3
digitCount = 1
while True:
    stored.append(stored[-1]+stored[-2])
    stored.pop(0)
    if stored[-1] >= 10**999:
        print(iteration)
        break
    iteration+=1
