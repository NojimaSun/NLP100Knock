def word_monogram(lines):
    dic={}
    for line in lines:
        pref=line.split("\t")[0]
        for i in range(len(pref)-1):
            if(dic.get(pref) is None):
                dic[pref]=1
            else:
                dic[pref]+=1
    for k ,v in sorted(dic.items(), key=lambda x: -x[1]):
        print(str(k) + ": " + str(v))
    print(dic)
def main():
    f = open("hightemp.txt","r",encoding="utf-8_sig")
    lines=f.readlines()
    f.close()
    word_monogram(lines)
if __name__ == "__main__":
    main()
