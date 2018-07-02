def set_character_bigram(word):
    s=set()
    for i in range(len(word)-1):
        s.add(word[i:i+2])
    return s
def main():
    w1="paraparaparadise"
    w2="paragraph"
    xset=set_character_bigram(w1)
    yset=set_character_bigram(w2)
    print(str(xset|yset)+" is intersection")
    print(str(xset&yset)+" is union")
    print(str(xset-yset)+" is difference")
if __name__ == "__main__":
    main()
