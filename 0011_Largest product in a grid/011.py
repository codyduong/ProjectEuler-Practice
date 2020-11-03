import fileinput
import math
import numpy
import itertools

def product(a):
    result = 1
    #print(a)
    for i in range(len(a)):
        result*=int(a[i])
    return result

def product_d(a, p, s1, s2):
    to_product = []
    for i in range(4):
        to_product.append(a[p[0]+(i*s1),p[1]+(i*s2)])
    return product(to_product)

def h_max_product(a):
    result = 0
    for i in range(20):
        result = max(result, max(product(a[i,j:j+4]) for j in range(16)))
    return result

def v_max_product(a):
    result = 0
    for i in range(20):
        result = max(result, max(product(a[j:j+4,i]) for j in range(16)))
    return result

def d_max_product(a):
    result = 0
    """
    possible diag combos are
    (x,y) * (x+1,y+1) *... *(x+3,y+3)
    (x,y) * (x-1,y+1) *...
    (x,y) * (x-1,y-1) *...
    (x,y) * (x+1,y-1) *...
    """
    for i in range(20):
        for j in range(20):
            try:
                result = max(result, product_d(a, [i,j], 1 , 1))
            except:
                pass
            try:
                result = max(result, product_d(a, [i,j], -1, 1))
            except:
                pass
            try:
                result = max(result, product_d(a, [i,j], -1,-1))
            except:
                pass
            try:
                result = max(result, product_d(a, [i,j], 1 ,-1))
            except:
                pass

    return result
    
def pg(n):
    l = [n[i*2]+n[i*2+1] for i in range((len(n)//2))]
    a = numpy.array(l).reshape(20,20)
    print(max(h_max_product(a), v_max_product(a), d_max_product(a)))

if __name__ == "__main__":
    i = ''.join([line for line in fileinput.input()]).replace('\n','').replace(' ','')
    print(pg(i))
