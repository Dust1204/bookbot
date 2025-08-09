def get_word_count(book_text): 
    word_list = book_text.split()
    return len(word_list)

def get_letter_count(book_text):
    lower_text = book_text.lower()
    letter_count = {}
    for letter in lower_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def sort_by(letter_count):
    list_of_letters = []
    for letter in letter_count:
        new_dict = {}
        new_dict['char'] = letter
        new_dict['num'] = letter_count[letter]
        list_of_letters.append(new_dict)
    list_of_letters.sort(reverse=True, key=lambda new_dict:new_dict['num'])
    return list_of_letters


    


