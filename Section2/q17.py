def main():
    f = open("hightemp.txt","r",encoding="utf-8_sig")
    lines=f.readlines()
    l1=set()
    for line in lines:
        words=line.split("\t")
        l1.add(words[0])
    f.close()
    print(len(l1))
if __name__ == "__main__":
    main()
