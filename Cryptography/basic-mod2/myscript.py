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
        modulus = pow(number, -1, 41)
        # print(modulus)
        
        if modulus in range(1, 27):
            flag.append(string.ascii_uppercase[modulus-1])
        elif modulus in range(27, 37) :
            flag.append(string.digits[modulus-27])
        else :
            flag.append("_")
            
print("picoCTF{%s}" % "".join(flag))