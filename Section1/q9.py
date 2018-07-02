import random
def makeset(words):
    l=[]
    for i in range(len(words)):
        if(len(words[i]))>4:
            l.append(i)
    random.shuffle(l)
    return l
def change_words(words,l):
    s=""
    j=0
    for i in range(len(words)):
        if(i in l):
            s=s+" "+words[l[j]]
            j+=1
        else:
            s=s+" "+words[i]
    return s[1:-1]
def main():
    sentence="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    words=sentence.split(" ")
    l=makeset(words)
    print(change_words(words,l))
if __name__ == "__main__":
    main()
