def character_bigram(words):
    dic={}
    for word in words:
        for i in range(len(word)-1):
            if(dic.get(word[i:i+2]) is None):
                dic[word[i:i+2]]=1
            else:
                dic[word[i:i+2]]+=1
    print(dic)
def word_bigram(words):
    dic={}
    for i in range(len(words)-1):
        if(dic.get(words[i]+" , "+words[i+1]) is None):
            dic[words[i]+" , "+words[i+1]]=1
        else:
            dic[words[i]+" , "+words[i+1]]+=1
    print(dic)
def main():
    sentence="I am an NLPer"
    words=sentence.split(" ")
    character_bigram(words)
    word_bigram(words)
if __name__ == "__main__":
    main()
