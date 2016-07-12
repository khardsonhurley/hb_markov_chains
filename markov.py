from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_string = open(file_path) #open file and save as a variable
    text_string = text_string.read() #save content as a string
    return text_string #returns a string of the content 


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    words = text_string.split() #takes in string and provides a list of all the words
    chains = {} #create empty dictionary that will contain word pairings 
                #with their third word options

    for i in range(len(words)-2):   #iterate using the indices of the list
        word_tuple = tuple([words[i], words[i + 1]])    #get first key, turn into tuple, save 
                                                        #as variable
        chains[word_tuple] = []     #add key to dictionary, if doesn't exist default empty 
                                    #list as value
    for i in range(len(words)-2):   #iterate using the indices of the list
        word_tuple = tuple([words[i], words[i + 1]]) #get first key, turn into tuple, save as 
                                                     #variable
        chains[word_tuple] = chains[word_tuple] + [words[i+2]] #Adding new word (in list) to 
                                                                #old list in the value of key 
                                                                #word_tuple
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text

