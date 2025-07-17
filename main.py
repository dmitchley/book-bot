import sys
from stats import get_book_file, get_book_length, counts_letters_symbols
 
 

def main():
    #print('firing')
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(get_book_length(sys.argv[1]))
    print('--------- Character Count -------')
    print(counts_letters_symbols(sys.argv[1]))

if __name__ == "__main__":
    main()
