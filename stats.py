def count_words(text):
    word_count = 0
    for word in text.split():
        word_count += 1
    return word_count

def count_characters(text):
    char_dict = {}
    for char in text.lower():
        if char not in char_dict:
            char_dict[char]=1
        else:
            char_dict[char]+=1
    return char_dict

def sort_characters(char_dict):
    # Build a list of dictionaries
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "num": count})

    # Helper function for sorting
    def sort_on(d):
        return d["num"]

    # Sort from greatest to least
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list