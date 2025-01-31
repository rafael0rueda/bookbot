def main():
    with open("books/frankenstein.txt") as f:
        file_contens = f.read()
        cw = count_words(file_contens)
        cc = count_characters(file_contens)
        print(f"--- Begin report of {f.name} ---")
        print(f"{cw} words found in the document\n")
        report(cc)
        

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

def sort_on(dict):
    return dict["num"]

def report(count_ch):
    for ch in count_ch:
        if ch.isalpha():
            print(f"The '{ch}' character was found {count_ch[ch]} times")
    
    return


main()