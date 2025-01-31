def main():
    with open("books/frankenstein.txt") as f:
        file_contens = f.read()
        print(count_words(file_contens))

def count_words(text):
    words = text.split()
    return len(words)


main()