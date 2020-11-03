def pp(d):
    s = ""
    for i in range(d):
        s+="9"

    print(s)
    
    s_convert = int(s)
    palindromes = []
    for i in range(s_convert, 0, -1):
        for j in range(s_convert, 0, -1):
            p = str(i*j)
            if p == p[::-1]:
                #print(i, j, i*j)
                palindromes.append(i*j)

    palindromes.sort()
    print(palindromes[-1])
                
if __name__ == "__main__":
    print(pp(int(input())))
