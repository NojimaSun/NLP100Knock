def main():
    sentence="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    l=[]
    s={}
    numl=[1, 5, 6, 7, 8, 9, 15, 16, 19]
    words=sentence.split(" ")
    for i in range(len(words)):
        if(i in numl):
            s[words[i][0]]=i
        else:
            s[words[i][0:2]]=i
    print(s)
if __name__ == "__main__":
    main()
