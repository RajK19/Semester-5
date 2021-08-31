#Name: Raj Kansal
#PRN: 20190802013
#Date: 31 August 2021
#B.Tech CSE 5th Sem (3rd Year)


def monocode(c):
    dictionary = {
    'a': 'D','b': 'K','c': 'V','d': 'Q',
    'e': 'F','f': 'I','g': 'B','h': 'J',
    'i': 'W','j': 'P','k': 'E','l': 'S',
    'm': 'C','n': 'X','o': 'H','p': 'T',
    'q': 'M','r': 'Y','s': 'A','t': 'U',
    'u': 'O','v': 'L','w': 'R','x': 'G',
    'y': 'Z','z': 'N',
    ' ': ' '
    }

    return dictionary[c]

def encrypt(s):
    res = ""
    for i in s:
        res += monocode(i.lower())

    return res

inp = input("Enter text to encrypt : ")
ans = encrypt(inp)
print()
print("Encrypted Text is : ", ans)
