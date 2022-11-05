import string

# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.ascii_letters)
# print(string.digits)

flag = []

with open("message.txt") as file:
    
    contents = file.read()
    numbers = [int(value) for value in contents.split()]
    
    for number in numbers :
        modulus = number % 37
        
        if modulus in range(26):
            flag.append(string.ascii_uppercase[modulus])
        elif modulus in range(26, 36) :
            flag.append(string.digits[modulus - 26])
        else :
            flag.append("_")
            
print("picoCTF{%s}" % "".join(flag))