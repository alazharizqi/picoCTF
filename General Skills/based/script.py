bin_msg = '011100110111010001110010011001010110010101110100'

oct_msg = '143157156164141151156145162'

hex_msg = '736f636b6574'

msg = []

for i in range(0, len(bin_msg), 8):
    print(chr(int(bin_msg[i:i+8], 2)))
    
print('\n')
    

for i in range(0, len(oct_msg), 3):
    print(chr(int(oct_msg[i:i+3], 8)))
    
print('\n')

for i in range(0, len(hex_msg), 2):
    print (chr(int(hex_msg[i:i+2], 16)))

# for i in range(0, len(msg)):
#     flag += print(msg[i])
    
# print(flag)