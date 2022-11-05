from chunk import Chunk


with open("message.txt", "r") as file:
    content = file.read()
    
flag = ''
    
for i in range(0, len(content), 3):
    block = content[i:i+3]
    # print(block)
    a, b, c = block
    flag += c+a+b
    
print(flag)