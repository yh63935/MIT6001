# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for character in secret_word:
        if character not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    hangmanArr = []
    for character in secret_word:
        if character not in letters_guessed:
            hangmanArr.append("_ ")
        else:
            hangmanArr.append(character)
    return "".join(hangmanArr)
         

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = ""
    all_letters = string.ascii_lowercase
    for letter in all_letters:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters

def get_num_unique_letters(secret_word):
    """
    secret_word : string, secret word to pass

    Get number of unique letters in the secret word

    returns: integer representing number of unique letters

    """
    unique_letters = set(secret_word)
    num_unique_letters = len(unique_letters)
    return num_unique_letters

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # Initialize game
    guesses = 6
    letters_guessed = []
    warnings = 3
    guessed_word = get_guessed_word(secret_word, letters_guessed)   
    vowels = ("a", "e", "i", "o", "u")
    
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings} warnings left. ")
    print("-------------  ")


    while(is_word_guessed(secret_word, letters_guessed)==False and guesses>0):
        print(f"You have {guesses} guesses left.")
        available_letters = get_available_letters(letters_guessed)
        
        print(f"Available letters: {available_letters}")
        guess = input("Please guess a letter: ")
        formattedGuess = str.lower(guess)
        # Decrease warnings if invalid guess or letter is already guessed
        # If warnings exist, if not decrease guesses
        if str.isalpha(guess) == False or formattedGuess in letters_guessed:

            if warnings>0:
                warnings-=1
                message = f"You have {warnings} warnings left: {guessed_word}"

            else:
                guesses-=1
                message = f"You have no warnings left so you lose one guess: {guessed_word}"
            
            if str.isalpha(guess) == False:
                print(f"Oops! That is not a valid letter. {message}")
            else:
                print(f"Oops! You've already guessed that letter. {message}")
        # If formattedGuess is not in the secret word
        # Decrease guesses by 1 or 2 depending if it is a vowel or consonant
        elif formattedGuess not in secret_word:
            if formattedGuess in vowels:
                guesses-=2
            else: 
                guesses-=1
            letters_guessed.append(formattedGuess)
            print(f"Oops! That letter is not in my word: {guessed_word}")   
        else:
            letters_guessed.append(formattedGuess)
            guessed_word = get_guessed_word(secret_word, letters_guessed)   

            if formattedGuess in secret_word:        
                print(f"Good guess: {guessed_word} ")

        print("-------------  ")
    total_score = guesses * get_num_unique_letters(secret_word)
    if is_word_guessed(secret_word, letters_guessed)==True:
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {total_score} ")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")
        
    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------




def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_no_spaces = my_word.replace(" ", "")
    
    # If my_word and other_word are not the same length, return False
    if len(my_word_no_spaces) != len(other_word):
        return False
    for letter in range(len(my_word_no_spaces)):
        if my_word_no_spaces[letter] != "_":
            if other_word[letter] != my_word_no_spaces[letter]:
                return False
        # If the letter of other_word at my_word's hidden letter index exists in my_word, that means that letter has already been guessed
        # Hidden letter can not be one of the letters that has already been revealed
        else: 
            if other_word[letter] in my_word:
                return False
    return True
            
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
        matches = ""
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches += word + " "
    if matches:     
       print(matches)
    else: 
        print("No matches found")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
#     # pass

#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
 
