def main():
    path = "github.com/FT1006/bookbot/books/frankenstein.txt"
    text =  get_book_text(path) 
    num_word = get_words_num(text)
    print(f"{num_word} words in this book")
    print(get_char_count(text))

def get_book_text(path):
    with open(path) as f:
        # read the file
        return f.read()

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

main()