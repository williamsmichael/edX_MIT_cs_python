print "Please think of a number between 0 and 100!"
question = "Is your secret number "
instructions = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "
low = 0
high = 100
reply = ""
while (reply != "c"):
    guess = (low + high) / 2
    reply = raw_input(question + str(guess) + "?\n" + instructions)
    if (reply == "c"):
        break
    elif (reply == "h"):
        high = guess
    elif (reply == "l"):
        low = guess
    else: 
        print "Sorry, I did not understand your input"
print "Game over. Your secret number was: ", guess  
