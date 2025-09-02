from stats import get_word_count, get_char_count, sort_dictionary
import sys

def main():

    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(book_text)
    char_count = sort_dictionary(get_char_count(book_text))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print ("--------- Character Count -------")
    for char in char_count:
        print(f"{char['char']}: {char['num']}")

    print("============= END ===============")

def get_book_text(file_location):
    with open(file_location) as f:
        file_contents = f.read()
    return file_contents

main()
