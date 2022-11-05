def decode(num):
    r = num % 37
    return r

def main():
    f = open("message.txt", "r", encoding="utf-8")
    lst = f.read().split()

    dec_lst = []

    for i in range(len(lst)):
        dec_lst.append(decode(int(lst[i])))

    print(dec_lst)

if __name__ == "__main__":
    main()