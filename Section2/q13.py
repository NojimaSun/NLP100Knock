def main():
    f1=open("col1.txt","r",encoding="utf-8_sig")
    f2=open("col2.txt","r",encoding="utf-8_sig")
    l1=f1.readlines()
    l2=f2.readlines()
    l=[]
    for i in range(len(l1)):
        l.append(l1[i].replace("\n","")+"\t"+l2[i].replace("\n",""))
    f1.close()
    f2.close()
    f3=open("col3.txt","w",encoding="utf-8_sig")
    f3.write("\n".join(l))
    f3.close()
if __name__ == "__main__":
    main()
