def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    def numOfWords():
        words = file_contents.split()
        wordCount = 0
        for word in words:
            wordCount += 1
        print(wordCount)

    numOfWords()

    def numOfChar(s):
        charCount = {}
        s = s.lower()
        for char in s:
            if char in charCount:
                charCount[char] += 1
            else:
                charCount[char] = 1
        return charCount

    chars_in_book = numOfChar(file_contents)
    print(chars_in_book)


if __name__ == '__main__':
    main()
