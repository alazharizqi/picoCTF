import tarfile

for i in range(1000, 1, -1):
    file = str(i) + '.tar'
    tar = tarfile.open(file)
    tar.extractall()
    tar.close()