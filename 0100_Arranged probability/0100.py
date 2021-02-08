#this is totally not the intended way to do this, and at this rate the brute-force checking of each number is bad.
#probably an optimized algo i need to figure out...
#mostly running into issues with precision at the 10**12 scale. ugh time to move to C or it's deriatives.

import math
import time
from decimal import Decimal

START = 10**12
t = START #total
s_time = time.time()

#x solution given by wolfram alpha lmao
#https://www.wolframalpha.com/input/?i=%5Cleft%28%5Cfrac%7Bx%7D%7Bt%7D%5Cright%29%5Ccdot%5Cfrac%7B%5Cleft%28x-1%5Cright%29%7D%7B%5Cleft%28t-1%5Cright%29%7D+%3D+1%2F2
while True:
    elapsed = time.time() - s_time
    #x = (2t^{2}-2t+1)
    x = Decimal(.5*(math.pow(2*t**2 - 2*t + 1, .5)) +1)
    if x.as_integer_ratio() == (1,2):
        print('\nFound possible?: %s at %s' % (str(x), t))
        if input('Continue: Y/N') == 'N':
            break
    print('\rTime: %s and Searching: %i with X: %s' % (str(elapsed)[:4], t, str(x)), end='', flush =True)
    t+=1
    