from stats import get_book_text
from stats import count_words

def main():
    path_to_file = "./books/frankenstein.txt"
    with open(path_to_file, 'r', encoding='utf-8') as f:
        contents = get_book_text(f)   
    
    num_words = count_words(contents)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()
