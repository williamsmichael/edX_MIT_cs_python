# 6.00 Problem Set 3
# 
# Hangman game
#

def hangman(secret_word):

    guess_list = []
    correct_list = []
    guess = ""
    shown = ""
    available_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    final_answer = ""
    chances = 8
    
    # actively reveal the secret_word word
    def display_secret_word(secret_word, guess, shown):
        for letter in secret_word:
            if guess == letter:
                shown += guess + " "
            elif letter in correct_list:
                shown += letter + " "
            else:
                shown += "_ "
        return shown
    
    # check if the letter is in the word, track the guesses
    def check(guess, chances):
        count = 0
        if guess in guess_list:
            print "Oops! You've already guessed that letter:", display_secret_word(secret_word, guess, shown)
        elif guess in secret_word:
            correct_list.append(guess)
            guess_list.append(guess)
            count = secret_word.count(guess)
            print "Good guess: ", display_secret_word(secret_word, guess, shown)
        else:
            print "Oops! That letter is not in my word:", display_secret_word(secret_word, guess, shown)
            chances -= 1
            guess_list.append(guess)
        return chances
            
    def availability(lettersGuessed):
        '''
        lettersGuessed: list, what letters have been guessed so far
        returns: string, comprised of letters that represents what letters have not
          yet been guessed.
        '''
        for guess in guess_list:
            if guess in available_letters:
                available_letters.remove(guess)
        
        return "".join(available_letters)
    
    # welcome message
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
        
    # interact with the user to guess the secret_word word
    display_secret_word(secret_word, guess, shown)
    while chances > 0 and len(final_answer) != len(secret_word):
        
        # ask for a letter and cache zero index
        print "-------------"
        print "You have {} guesses left".format(chances)
        print "Available Letters:", availability(guess_list)
        
        guess = raw_input("Please guess a letter: ").lower()
        
        # check if it is a correct guess
        # initially verify if isalpha, otherwise check if it is a correct guess
        if not guess.replace(' ', '').isalpha():
            print("\nLetters only please. Try again...\n")
        else:
            chances = check(guess, chances)
            
        # display hidden word to user
        final_answer = display_secret_word(secret_word, guess, shown)
        final_answer = final_answer.replace("_", "").replace(" ", "").strip()
        if len(final_answer) == len(secret_word):
            print "-------------"
            print "Congratulations, you won!"
            break
                
    else:
        print "-------------"
        print "Sorry, you ran out of guesses. The word was {}.".format(secret_word)

# ------------------------------------------------------------
# ------------------------------------------------------------
# HANGMAN PART 1: IS THE WORD GUESSED (5 Points)
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    aList = []
    ans = True
    for letter in secretWord:
        if letter in lettersGuessed:
            aList.append(True)
        else:
            aList.append(False)
    if aList.count(False) > 0:
        ans = False
    return ans
            
print isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']) # return False

# ---------------------------------get guessed
# PRINTING OUT THE USER'S GUESS  (5 points possible)
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter + " "
        else:
            guessed += "_ "
            
    return guessed.strip()
    
print getGuessedWord('apple', lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']) # return '_ pp_ e'

# ---------------------------------available letters
# PRINTING OUT ALL AVAILABLE LETTERS  (5 points possible)
import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    aList = []
    for letter in string.ascii_lowercase:
        if letter in lettersGuessed:
            continue
        else:
            aList.append(letter)
            
    return "".join(aList)
    
print getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']) # return abcdfghjlmnoqtuvwxyz
