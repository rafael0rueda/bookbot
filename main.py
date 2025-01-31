def main():
    with open("books/frankenstein.txt") as f:
        file_contens = f.read()
        cw = count_words(file_contens)
        print(count_characters(file_contens))

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowered_text = text.lower()
    count_ch = {}
    characters = list(lowered_text)
    for ch in characters:
        if ch in count_ch:
            count_ch[ch] += 1
        else:
            count_ch[ch] = 1
    return count_ch

main()