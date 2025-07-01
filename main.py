from stats import get_book_text
from stats import count_words
from stats import count_types
 
 
def main():
    path_to_file = "./books/frankenstein.txt"
    with open(path_to_file, 'r', encoding='utf-8') as f:
        contents = get_book_text(f)   
      
    num_words = count_words(contents)
     

    item_return = count_types(contents)
    print(item_return)


if __name__ == "__main__":
    main()