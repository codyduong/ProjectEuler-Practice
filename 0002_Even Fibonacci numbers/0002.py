import itertools

#s is the value of the !function (noted as 4mil on ProjectEuler)
def even_fib(s):
    fib = [1, 2]
    for i in itertools.count(0):
        f = fib[-1] + fib[-2]
        if f>s:
            break
        else:
            fib.append(f)

    #print(fib)
    evens = list(t for t in itertools.filterfalse(lambda x: x%2, fib))
    count = 0
    for i in evens:
        count+=i
        #print(count)

    return count

if __name__ == "__main__":
    print(even_fib(int(input())))
