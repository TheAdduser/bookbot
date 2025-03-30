def count_words(text):
    split_text = text.split()

    return len(split_text)
        
def count_characters(text):
    letter_count = {}
    text = text.lower()
    
    for letter in text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    return letter_count