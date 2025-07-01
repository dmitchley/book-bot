def get_book_text(f):
     
    return f.read()

def count_words(text):
    
    words = text.split()
    return len(words)

def count_types(texts):
    counts = {}

    for item in texts:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    
     
    sorted_dict = dict(sorted(counts.items()))
     
    return sorted_dict

 