import string


def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)


{
    141: 1,
    8: 2,
    
}

ct = encryption([2])
f = open('./msg.enc', 'w')
# f.write(ct.hex())
# print(in(ct))
encDecimal = [i for i in ct]
print(encDecimal, "\n")
print(int('0x780e7153935372ce9df6f6729d721e9d932ce0784d11f339f32bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921', 16))
f.close()
