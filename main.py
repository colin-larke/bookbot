def main() :
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count = word_count(file_contents)
        char_dict = char_count(file_contents)
        sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{count} words found in the document")
        print()
        for c in sorted_dict:
            print(f"The '{c}' was character was found {sorted_dict[c]} times")
        print("--- End report ---")

def word_count(text):
    num_words = len(text.split())
    return num_words

def char_count(text):
    text = text.lower()
    char_dic = {}
    for c in text:
        if c.isalpha() == True:
            if c not in char_dic:
                char_dic[c] = 1
            else:
                char_dic[c] += 1
    return char_dic

main()