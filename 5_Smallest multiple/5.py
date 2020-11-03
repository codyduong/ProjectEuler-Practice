import math

def sm(s):
    l = []
    for i in range(1,s+1):
        l.append(i)

    return math.lcm(*l)

if __name__ == "__main__":
    print(sm(int(input())))
