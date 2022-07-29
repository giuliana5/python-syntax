def print_upper_words(words):
    """Prints out each word on a separate line in uppercase."""
    
    for word in words:
        print(word.upper())

def print_upper_words(words, starts_with):
    """Prints out each word if it starts with the letters indicated."""
    for word in words:
        for letter in starts_with:
            if word.startswith(letter):
                print(word.upper())
                break


    
