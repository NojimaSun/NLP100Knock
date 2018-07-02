def main():
    f = open("hightemp.txt",encoding="utf-8_sig")
    print(len(f.readlines()))
    f.close()
if __name__ == "__main__":
    main()
