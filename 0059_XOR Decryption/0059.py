import fileinput
import itertools

def decrypter(toDecrypt, key): 
    result = []

    for each in toDecrypt:
        result.append(bin(each ^ key))

    return result

if __name__ == "__main__":
    with open fileinput:
    decrypter