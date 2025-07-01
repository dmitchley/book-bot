def get_book_text(f):
     
    return f.read()

def count_words(text):
    
    words = text.split()
    #new = text.replace(" ", "")
    #print(new)
    return len(words)

word_counts = {}
def count_chars(text):
    #loop_text = text.split()
    
    words = text.replace(" ", "")
    
    for word in words:
        word = word.lower().strip(".,!?")  
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return str(word_counts)


def new_function(inputstuff):

     

    new = inputstuff.split()
    print(new.sort())
    #print(new[0::2])
    print(new.values())
    #print(new.sort(reverse=True, new.values()))
    return inputstuff
 

#new_function(word_counts)