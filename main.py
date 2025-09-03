from stats import get_word_count, get_char_count, sort_dictionary
import sys

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        print(f"\nError: 2 arguments are needed for running main.py. {len(sys.argv)} was given")
        sys.exit(1)


    book_text = get_book_text(sys.argv[1])
    word_count = get_word_count(book_text)
    char_count = sort_dictionary(get_char_count(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
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
