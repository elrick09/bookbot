def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_words_number(text)
    chars_dict = num_char(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words_number(text):
    return len(text.split())

def num_char(text):
    lowered_text = text.lower()
    symbols_dict = {}
    for symbol in lowered_text:
            # Check if the symbol already exists in the dictionary
            if symbol in symbols_dict:
                symbols_dict[symbol] += 1
            else:
            # Initialize the count to 1 if the key doesn't exist
                symbols_dict[symbol] = 1
    return symbols_dict

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        if char.isalpha():
            sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()