def main():
    s=s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    l=[]
    for i in s.split(" "):
        l.append(str(len(i)))
    l.insert(1,".")
    print(l)
if __name__ == "__main__":
    main()
