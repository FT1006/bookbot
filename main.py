def main():
    path = "github.com/FT1006/bookbot/books/frankenstein.txt"
    text =  get_book_text(path) 
    num_word = get_words_num(text)
    print(f"{num_word} words in this book")

def get_book_text(path):
    with open(path) as f:
        # read the file
        return f.read()

def get_words_num(text):
    words = text.split()
    return len(words)

main()