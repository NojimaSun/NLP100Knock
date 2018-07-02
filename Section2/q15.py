import sys
n=int(sys.argv[1])
def main():
    f = open("hightemp.txt","r",encoding="utf-8_sig")
    lines=f.readlines()
    f.close()
    for i in range(len(lines)):
        if(n<=i):
            print(lines[i])
if __name__ == "__main__":
    main()
