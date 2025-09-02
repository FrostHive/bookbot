def get_word_count(book_text):
    word_list = book_text.split()
    return len(word_list)

def get_char_count(book_text):
    char_dict = {}
    for char in book_text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
