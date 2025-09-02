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

def sort_key(char_dictionary):
    return char_dictionary["num"]

def sort_dictionary(dictionary):
    sorted_list = []
    for char in dictionary:
        if(char.isalpha()):
            temp_dictionary = {"char": char, "num": dictionary[char]}
            sorted_list.append(temp_dictionary)

    sorted_list.sort(reverse=True, key=sort_key)
    return sorted_list
