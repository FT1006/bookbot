def main():
    path = "/Users/spaceship/workspace/githubcom/FT1006/bookbot/books/frankenstein.txt"
    text =  get_book_text(path) 
    num_word = get_words_num(text)
    char_count_dict = get_char_count(text)
    sorted_char_count_list = sort_reverse(char_count_dict)
    print_report(num_word, sorted_char_count_list)

def get_book_text(path):
    try:
        with open(path) as file:
            # read the file
            return file.read()
    except FileNotFoundError:
        print(f"'{path}' was not found.")

def get_words_num(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lowered_string = text.lower()
    count_char = {}
    for char in lowered_string: 
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1 
    return count_char

def sort_on(dict):
    # Return the value of the "count" key to use as a sorting key
    return dict["count"]

def sort_reverse(char_count_dict):
    # Use list comprehension to filter and create the list of dictionaries
    sorted_list = [{'char': char, 'count': count} for char, count in char_count_dict.items() if char.isalpha()]
    
    # Sort the filtered list
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(word_count, sorted_char_count_list):
    print(f"i--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for item in sorted_char_count_list:
        print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End report ---")

main()