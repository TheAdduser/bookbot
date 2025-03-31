from stats import count_words, count_characters, sort_character_count
filepath = 'books/frankenstein.txt'

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
        
def main():
    book_text = (get_book_text(filepath))

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print(f"----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print(f"--------- Character Count -------")
    letter_count = sort_character_count(count_characters(book_text))
    for letter in letter_count:
        name = letter["name"]
        count = letter["count"]
        print(f"{name}: {count}")
main()