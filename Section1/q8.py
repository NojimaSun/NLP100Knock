def cipher(word):
    s=""
    for w in word:
        if(w.islower()):
            s=s+chr(219-ord(w))
        else:
            s=s+w
    return s
def main():
    cip=cipher("Sample Sentence だよ")
    print(cip)
    rev_chip=cipher(cip)
    print(rev_chip)
if __name__ == "__main__":
    main()
