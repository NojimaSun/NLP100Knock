def main():
    f = open("hightemp.txt",encoding="utf-8_sig")
    lines=f.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].replace("\t"," ")
    f.close()
    print(lines)
if __name__ == "__main__":
    main()
