# Define a function called word_counter that accepts one string argument and returns a number representing how many separate words are in that string.
def word_counter(word):
    return len(word.split())

print (word_counter('hello'))    
