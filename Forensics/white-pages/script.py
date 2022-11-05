with open('whitepages.txt', 'r') as file:
    content = file.read()

first = '  '
seccond = ' '
binary = ''

for i in content:
    if i == first:
        binary += '0'
    else:
        binary += '1'

print(binary)