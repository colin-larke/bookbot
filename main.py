def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    # print(book_text)
    word_count = get_word_count(book_text)
    # print(f"Word Count:{word_count}")
    sorted_letters = sort_letters(letter_count(book_text))

    print(f"Beginning book report on {book_path}")
    print(f"Word Count:{word_count}")
    print()

    for letter in sorted_letters:
        ls = letter["letter"]
        ln = letter["num"]
        print(f"The letter {ls} was found {ln} times")

    print("End of Report")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(words):
    count = len(words.split())
    return count

def letter_count(book):
    book = book.lower()
    letter_dict = {}
    for i in range(0, len(book)):
        if book[i].isalpha() and book[i] not in letter_dict:
            count = str(book.count(book[i]))
            letter_dict[book[i]] = count  
    return(letter_dict)

def sort_on(dict):
    return dict["num"]

def sort_letters(dict):
    letter_list = []
    for k,v in dict.items():
        let_dict = {"letter":k, "num":int(v)}
        letter_list.append(let_dict)
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list

main()