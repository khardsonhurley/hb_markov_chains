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

    #text = "" #string to be used at very end

    sentence = [] #create empty list "sentence"
    dict_of_words = chains #saves the inputted dictionary as a variable

    first_tuple = choice(dict_of_words.keys())   #randomly selected a key in the 
                                                        #dictionary
    
    #VERIFY THE TUPLE: If tuple not in dictionary, end loop and print text. 

    sentence.append(first_tuple[0])#add tuple[0] to our sentence
    sentence.append(first_tuple[1])#add tuple[1] to our sentence
    print sentence
    random_third_word = choice(dict_of_words[first_tuple])
    print random_third_word
    #randomly pick an item in the value's list
    #add the new string to "sentence"
    #to get new key call index -2 and -1 of "sentence"--> creating a tuple
    #call dictionary on new tuple --> unpack etc. 

    #turn "sentence" into long string by adding elements into the string "text"



input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)

random_text

