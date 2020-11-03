def sumsquare(s):
    return (sum([i for i in range(1,s+1)])**2) - (sum([i**2 for i in range(1,s+1)]))

if __name__ == "__main__":
    print(sumsquare(int(input())))
