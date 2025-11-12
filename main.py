import sys
from stats import get_num_words, count_chars, sort_dict, sort_on

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read() 


def main(): 

    if len(sys.argv) == 2:
        pass
    else: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    words = get_num_words(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    char_count = count_chars(book)
    sorted_list = sort_dict(char_count)
    

    for dic in sorted_list:
        if dic["char"].isalpha():
            print(f"{dic["char"]}: {dic["count"]}")
    print("============= END ===============")


main() 

