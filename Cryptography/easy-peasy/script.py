msg = '51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57'
flag = ''

for i in range(0, len(msg), 2):
    flag += chr(int(msg[i:i+2], 16))
    
print('picoCTF{%s}'% flag)