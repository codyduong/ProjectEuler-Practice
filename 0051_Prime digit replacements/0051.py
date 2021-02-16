import math
import time


#Taken from 0003_Largest prime number
def isPrime(n: int) -> bool:
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


#There is without a doubt a better way to do this. This is like o(n)logn time plus a little more
def checkPrimeSet(i: int) -> int:
    """
    Takes parameter (i: int) and finds the prime digit replacement as of defined by problem 51 on
    Project Euler.
    """
    ts = time.time()
    tf = 0
    count=56003 #we know this is where 7 starts
    operations=0
    currentPrime = 0
    while True:
        if isPrime(count):
            currentPrime = count
            replacementDict = returnPossibleDigitReplacements(currentPrime)
            primeList = []
            for key in replacementDict:
                primeReplacements = []
                removedDupes = list(dict.fromkeys(replacementDict[key]))
                for each in removedDupes:   
                    if isPrime(each):
                        primeReplacements.append(each)
                        currentPrime = each
                        if each>count:
                            primeList.append(each)
                if len(primeReplacements) == i:
                    print(primeReplacements)
                    return(primeReplacements[0])
            if tf<=.001:
                primeList.sort()
                try: count = primeList[1]
                except: pass
        count += 1
        operations += 1
        tf = time.time()-ts
        print("\rCount: %i | Current Prime: %i | Elapsed Time: %f | Timedx: %f" % (count, currentPrime, tf, tf/operations),  end='', flush=True)

#This recursive function is beyond fucked. Good luck if you're trying to use this.
def returnPossibleDigitReplacements(i: int, r={}, length_override=None, starter=None) -> dict():
    """
    Takes parameter (i: int) and finds all varying combinations of replacing subdigits of the input,
    but retaining at least 1 number in the original input in the same place, returns the combinations
    that are prime. IE:
        i = 123 ---> returns a dictionary of a table of values (IE starting location and length replacement) then all variations []
        | {'x23' = [123, 223, 323,... 923], '1x3' = [113, 223, 333,... 993]... }
    """
    int_to_str = str(i)
    replace = None
    ref_dict = r
    starterKey = starter or ''
    for start_location in range(0, len(int_to_str), 1):
        doneAlready = False
        for n in ['0','1','2','3','4','5','6','7','8','9']:
            replace = ''
            key_string = ''
            length_subtract = 0 if length_override else 1
            max_length = min(len(int_to_str)-length_subtract, len(int_to_str)-start_location)
            for i in range(0, max_length, 1):
                start = int_to_str[:start_location] 
                replace += n
                end = int_to_str[start_location+len(replace):]
                key_string += 'x'
                final_str = starterKey.replace('x', n) + start + replace + end
                if final_str != str(int(final_str)): #This removes any instances of decreasing replacement IE. 123 -> 023 or 003 is omitted
                    continue
                try:
                    ref_dict[starterKey+start+key_string+end].append(int(final_str))
                except:
                    ref_dict.update({starterKey+start+key_string+end: [int(final_str)]})
                if len(end) >= 2 and not doneAlready:
                    ref_dict = returnPossibleDigitReplacements(int(int_to_str[start_location+len(replace)+1:]), ref_dict, True, start+key_string+end[0])
                    doneAlready = True
                    #print(ref_dict)
    
    return ref_dict

#print(returnPossibleDigitReplacements(199))
print(checkPrimeSet(8))
