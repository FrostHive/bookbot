def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(book_text)
    print(f"{word_count} words found in the document")

def get_book_text(file_location):
    with open(file_location) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(book_text):
    word_list = book_text.split()
    return len(word_list)

main()
