import sys
n=int(sys.argv[1])
def main():
    f = open("hightemp.txt","r",encoding="utf-8_sig")
    lines=f.readlines()
    f.close()
    l1=[]
    l=[]
    for i in range(len(lines)):
        l1.append(lines[i])
        if(i==len(lines)-1 or (i+1)%n==0):
            l.append(l1)
            l1=[]
    print(l)
if __name__ == "__main__":
    main()
