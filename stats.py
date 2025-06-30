def get_book_text(f):
     
    return f.read()

def count_words(text):
    
    words = text.split()
    #new = text.replace(" ", "")
    #print(new)
    return len(words)

def count_chars(text):
    #loop_text = text.split()
    word_counts = {}
    words = text.replace(" ", "")
    
    for word in words:
        word = word.lower().strip(".,!?")  # clean basic punctuation
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return str(word_counts)

 