import sys
from stats import count_words, count_characters, sort_character_count


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
        
def main():
    filepath = ""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:    
        book_text = (get_book_text(sys.argv[1]))
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print(f"----------- Word Count ----------")
        print(f"Found {count_words(book_text)} total words")
        print(f"--------- Character Count -------")
        letter_count = sort_character_count(count_characters(book_text))
        for letter in letter_count:
            name = letter["name"]
            count = letter["count"]
            print(f"{name}: {count}")

main()