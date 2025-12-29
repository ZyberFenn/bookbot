from stats import count_words, count_characters, sort_characters
import sys
def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    txt_path = sys.argv[1]
    book_txt = get_book_text(txt_path)
    word_count = count_words(book_txt)
    char_dict = count_characters(book_txt)
    sorted_chars = sort_characters(char_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {txt_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words" )
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
    


main()
    