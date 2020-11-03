def find_multiples(i):
    count = 0
    for i in range(0, i, 3):
        if not i%5 == 0:
            count+=i
    for i in range(0, i, 5):
        count+=i

    return count

if __name__ == "__main__":
    print(find_multiples(int(input())))
