#Name: Raj Kansal
#PRN: 20190802013
#Date: 31 August 2021
#B.Tech CSE 5th Sem (3rd Year)


def encrypt(text, shift):
 
  cipher = ''
  for char in text:
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher
 
text = input("Enter Text: ")
shift = int(input("Enter shift value: "))
print("Original Text: ", text)
print("Cipher Text: ", encrypt(text, shift))
