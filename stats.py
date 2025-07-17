def get_book_file(input):
    with open(input) as f:
        file_contents = f.read()
        return file_contents
         

def get_book_length(input):
    with open(input) as f:
        file_contents = f.read()
        split_into_strings = file_contents.split()
        num_words = len(split_into_strings)
        return f"Found {num_words} total words"   

def counts_letters_symbols(input):
    with open(input) as f:
        file_contents = f.read()
        split_into_strings = list(file_contents)
        counts = {}

        allowed_keys = [
           'e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'd', 'l', 'm', 'u', 'c', 'f', 'y',
           'w', 'p', 'g', 'b', 'v', 'k', 'x', 'j', 'q', 'z', 'æ', 'â', 'ê', 'ë', 'ô'
        ]

        for item in split_into_strings:
            lower_case_item = item.lower()
            counts[lower_case_item] = counts.get(lower_case_item, 0) + 1

        for key,value in counts.items():
             if key == ' ':
                continue
             if key.lower() in allowed_keys:
                print(f"{key}: {value}")

        print("============= END ===============")
        #print(counts)


         