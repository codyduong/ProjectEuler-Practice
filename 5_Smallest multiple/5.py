import math

def sm(s):
    l = [i for i in range(1,s+1)]

    return math.lcm(*l)

if __name__ == "__main__":
    print(sm(int(input())))
