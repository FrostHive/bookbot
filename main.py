from stats import get_word_count, get_char_count

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(book_text)
    print(f"{word_count} words found in the document")
    print(get_char_count(book_text))

def get_book_text(file_location):
    with open(file_location) as f:
        file_contents = f.read()
    return file_contents

main()
