import math
import time

START = 10**12
t = START #total
s_time = time.time()

#x solution given by wolfram alpha lmao
#https://www.wolframalpha.com/input/?i=%5Cleft%28%5Cfrac%7Bx%7D%7Bt%7D%5Cright%29%5Ccdot%5Cfrac%7B%5Cleft%28x-1%5Cright%29%7D%7B%5Cleft%28t-1%5Cright%29%7D+%3D+1%2F2
while True:
    elapsed = time.time() - s_time
    #x = -1/2 (1 - t) t (sqrt(2 t^2 - 2 t + 1)/((t - 1) t) - 1/((1 - t) t))
    #x = -.5 * (1 - t)*t*(math.sqrt(2*t**2 - 2*t + 1))
    #x = -.5*(1-t)*(t)*( ((math.pow(((2*t)**2-(2*t)+1),.5))/(t*(t-1))) - (1/(t*(1-t))) )
    x = -.5*(1-t)*(t)*( ((math.pow((2*t**2-2*t+1),.5))/(t*(t-1))) - (1/(t*(1-t))) )
    if math.isclose(x, int(x), abs_tol=10):
        print('\nFound possible?: %s at %s' % (x, t))
        if input('Continue: Y/N') == 'N':
            break
    print('\rTime: %s and Searching: %i with X: %s' % (str(elapsed)[:4], t, str(x)), end='', flush =True)
    #time.sleep(.5)
    t+=1
    