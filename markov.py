from random import choice

import sys

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    #open file and save as a variable
    text_string = open(file_path) 
    #save content as a string
    text_string = text_string.read() 
    #returns a string of the content 
    return text_string 

def user_input_n():

    #get input from the user of however long the user wants the grams to be
    n = int(raw_input("What do you want n to be for your n-grams? "))

    return n    

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    #takes in string and provides a list of all the words
    words = text_string.split() 
    #create empty dictionary that will contain word pairings with their third word options
    chains = {} 

    n = user_input_n()

    #iterate using the indices of the list
    for i in range(len(words)-n):

        #create empty list that we will append the words to and create a tuple for the key
        word_list_for_key = []

        #for loop for n times, to grab the appropriate amount of words and add them to list
        for j in range(i,i+n):

            #get first key, turn into tuple, save as variable
            word_list_for_key.append(words[j])     

        word_tuple = tuple(word_list_for_key)

        #add key to dictionary, if doesn't exist default empty list as value  
        values_list = chains.get(word_tuple, [])

        #Adding new word (in list) to old list in the value of key word_tuple
        values_list.append(words[i + n])

        chains[word_tuple] = values_list

    return chains
    




#change the list into a tuple





def make_text(chains):
    """Takes dictionary of markov chains; returns random text as a string."""

    #string to be used at very end
    text = " " 

    #create empty list "sentence"
    sentence = [] 
    #saves the inputted dictionary as a variable
    dict_of_words = chains
    #new dictionary to store all keys and values where the key has a capital letter. 
    dict_of_capitals = {}
    #new list to put all the keys that will go into dict_of_capitals.
    list_of_keys = []
    #Get list of keys from dict_of_words to sort through. 
    list_of_keys = dict_of_words.keys() 
    #Iterating through the list of tuples
    for key in list_of_keys:
        #Assigning the first letter of the first word in the tuple to a variable. 
        first_letter = key[0][0]
        #Check to see if that letter is capital. If it is, add the key and value to dict_of_capitals. 
        if first_letter.isupper() == True:
            value = dict_of_words[key]
            dict_of_capitals[key] = value
   
    #randomly selected a key in the capitals dictionary
    first_tuple = choice(dict_of_capitals.keys())

    #add tuple[0] to our sentence
    sentence.append(first_tuple[0])
    #add tuple[1] to our sentence
    sentence.append(first_tuple[1])
    
    #randomly pick an item in the value's list
    random_third_word = choice(dict_of_words[first_tuple])   

    #add the new string to "sentence"
    sentence.append(random_third_word) 
    

    while True:
        #Grabs last two items of sentence and creating new tuple to become our key
        end_tuple = tuple([sentence[-2],sentence[-1]]) 

        #If the key is not in our dictionary, the loop breaks.
        if end_tuple not in dict_of_words: 
            break
        #Otherwise, we randomly select another value from the list of values of 
        #the key (random_tuple)
        else:
            #randomly pick an item in the value's list                               
            third_word = choice(dict_of_words[end_tuple]) 
            #Add the third_word to the sentence list. 
            sentence.append(third_word)   

    #joining the sentence list together to create one string
    return text.join(sentence) 

def format_string(string):
    text= ""
    string_list = string.split("?")
    for i in range(len(string_list)-1):
        string_list[i] = string_list[i] + "?\n"
    
    string_list[0] = " "+string_list[0]

    return text.join(string_list)
        

def main():

    input_path = sys.argv[1]
    # Open the file and turn it into one long string
    input_text = open_and_read_file(input_path)

    # Get a Markov chain
    chains = make_chains(input_text)

    # Produce random text
    random_text = make_text(chains)

    print random_text

if __name__ == '__main__':
    main()