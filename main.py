from stats import get_book_text
from stats import count_words
from stats import count_chars
from stats import new_function
 
def main():
    path_to_file = "./books/frankenstein.txt"
    with open(path_to_file, 'r', encoding='utf-8') as f:
        contents = get_book_text(f)   
    
    num_words = count_words(contents)
    #print(f"{num_words} words found in the document")

    counted = count_chars(contents)
    #print(f'numbers return is : {counted}')

    newsht = new_function(counted)
    print(newsht)

if __name__ == "__main__":
    main()
