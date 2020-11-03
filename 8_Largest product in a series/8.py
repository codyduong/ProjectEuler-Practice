import fileinput
import math

def product(s):
    p = 1
    for c in s:
        p *= int(c)
    return p

def ps(n):
    zero_split = n.split('0') #splits between 0's
    to_pop = []
    for i in range(len(zero_split)):
        if len(zero_split[i])<13:
            to_pop.append(i)

    for j in range(len(to_pop)):
        zero_split.pop(to_pop[j]-j)

    current = 0
    for each in zero_split:
        current = max(current, max(product(each[i : i + 13]) for i in range(len(each) - 13 + 1)))
        print(current)
        
    """without list comprehension
    for sequence in zero_split:
        shift = len(sequence)-13 + 1
        for i in range(shift):
            newseq = sequence[i:13+i]
            product = 1
            for j in newseq:
                product *= int(j)
            current = max(current, product)
            print(current)
    """
        

if __name__ == "__main__":
    i = ''.join([line for line in fileinput.input()]).replace('\n','')
    print(ps(i))
