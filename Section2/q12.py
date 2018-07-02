def main():
    f = open("hightemp.txt","r",encoding="utf-8_sig")
    lines=f.readlines()
    l1=[]
    l2=[]
    for line in lines:
        words=line.split("\t")
        l1.append(words[0])
        l2.append(words[1])
    f.close()
    f1=open("col1.txt","w",encoding="utf-8_sig")
    f1.write("\n".join(l1))
    f1.close()
    f2=open("col2.txt","w",encoding="utf-8_sig")
    f2.write("\n".join(l2))
    f2.close()
if __name__ == "__main__":
    main()
