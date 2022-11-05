pico = [16,9,3,15,3,20,6]
msg = [20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]
flag1 = ''
flag2 = ''

for i in pico:
    i += 64
    flag1 += chr(i)
    print(chr(i))
    
print()
    
for i in msg:
    i += 64
    flag2 += chr(i)
    print(chr(i))
    
print(flag1 + '{' + flag2 + '}')