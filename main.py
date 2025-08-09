import sys
from stats import get_word_count
from stats import get_letter_count
from stats import sort_by

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    path_to_file = sys.argv[1]


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(path_to_file)
    word_count = get_word_count(book_text)
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {path_to_file}...")
    print('----------- Word Count ----------')
    print(f"Found {word_count} total words")
    print('--------- Character Count -------')
    letter_count = get_letter_count(book_text)
    sorted_list = sort_by(letter_count)
    for i in sorted_list:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
    print('============= END ===============')
    
if __name__ == "__main__":
    main()