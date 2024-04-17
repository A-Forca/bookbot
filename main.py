def main():

    with open("bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()

    def numOfWords():
        words = file_contents.split()
        wordCount = 0
        for word in words:
            wordCount += 1
        print(wordCount)

    numOfWords()

    def numOfChar():
        charDict = {}
        for char in file_contents:


if __name__ == '__main__':
    main()
