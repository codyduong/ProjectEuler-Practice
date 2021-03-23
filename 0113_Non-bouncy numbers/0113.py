#a runtime test
import time

GOOGL = 10*100
i = GOOGL

start = time.time()
while True:
    i+=1
    print("\rCurrent runtime: %f and Current number: %i" % (start-time.time(), i), end='', flush=True)