msg = '65D9C68E03807969851A83B28BBEBED1'
flag = ''

for i in range(0, len(msg), 2):
    print(chr(int(msg[i:i+2], 16)))
        
print(flag)