def main():
    with open("books/frankenstein.txt") as rawTxt:
        fileContents = rawTxt.read()
        cntWords(fileContents)
        numInstances(fileContents)


def cntWords(fileContents):
    eachWord = fileContents.split()
    if len(eachWord) == 77986:
        print("total number of words =", len(eachWord))


def numInstances(fileContents):
    #create dictionary
    alphabetDict = {'a':0, 'b':0,'c':0, 'd':0,
                    'e':0, 'f':0,'g':0, 'h':0,
                    'i':0, 'j':0,'k':0, 'l':0,
                    'm':0, 'n':0,'o':0, 'p':0,
                    'q':0, 'r':0,'s':0, 't':0,
                    'u':0, 'v':0,'w':0, 'x':0,
                    'y':0, 'z':0}
    #remove everything excepts letter a-z
    onlyChars = ''.join(filter(str.isalpha, fileContents))
    onlyChars = onlyChars.lower()
    for x in onlyChars:
        if x in alphabetDict:
            alphabetDict[x] += 1
    print(alphabetDict)


#run main()
if __name__ == "__main__":
    main()