def main():
    f = open("hightemp.txt","r",encoding="utf-8_sig")
    lines=f.readlines()
    f.close()
    l=[]
    sortl=[]
    for i in range(len(lines)):
        temp=float(lines[i].split("\t")[2])
        l.append([i,temp])
    print(l)
    while(len(l)>0):
        lowest=1000000
        num=-1
        s=-1
        for i in range(len(l)):
            if(lowest>l[i][1]):
                num=l[i][0]
                highest=l[i][1]
                s=i
        sortl.append(lines[num])
        del l[s]
    print(sortl)
if __name__ == "__main__":
    main()
