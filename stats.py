def count_words(text):
    split_text = text.split()

    return len(split_text)
        
def count_characters(text):
    letter_count = {
    }
    text = text.lower()
    
    for letter in text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    return letter_count

def sort_character_count(letter_count):
    list_of_dicts = []
    
    def sort_on(dict):
        return dict["count"]
    
    for character in letter_count:
        d = { "name" : character, "count" : letter_count[character]}
        list_of_dicts.append(d)
    
    list_of_dicts.sort(reverse=True, key = sort_on)
    return letter_count