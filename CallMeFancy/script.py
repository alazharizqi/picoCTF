def encryption(msg):
    ct = {}
    for char in msg:
        ct[(123 * char + 18) % 256] = char
    return ct

arr = '780e7153935372ce9df6f6729d721e9d932ce0784d11f339f32bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921'

num = []

print()
for i in range(0, len(arr), 2):
    print(int(arr[i:i+2], 16))
    num.append(int(arr[i:i+2], 16))

# print(num)

a = encryption(range(200))

# print(a)

flag = ''

for i in num:
    if i in a.keys():
        flag += chr(a[i])


print(flag)        