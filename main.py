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
    print(sort_character_count(book_text))
    # for letter in sort_character_count(book_text):
    #     if letter.isalpha(letter) == True:
    #         print(f"{letter["name"]}: {letter["count"]}")
    
main()