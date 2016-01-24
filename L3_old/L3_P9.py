# In this problem, you'll create a program that guesses a secret number!
# Note: your program should be using raw_input to obtain the user's input! Be sure to handle the case when the user's input is not one of h, l, or c.

prompt = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "
user_response = ""

# initializes the game
low = 0
high = 100
guess_int = (low + high) / 2 # first guess by the computer

# start print
print("Please think of a number between {} and {}!".format(low, high))

# enter game, exits on keypress 'c' for correct answer
while user_response != 'c':
  secret_guess = 'Is your secret number {}?'.format(guess_int)
  print(secret_guess)
  user_response = raw_input(prompt)

  if user_response not in ('h', 'l', 'c'):
    print("Sorry, I did not understand your input.")
  else:
    if user_response == 'h': # too high
      high = guess_int
      # print(low, " low")
      # print(high, " high")

    elif user_response == 'l': # too low
      low = guess_int
      # print(low, " low")
      # print(high, " high")

  # reset the guess)int based on the new high or low
  guess_int = (high + low) / 2

print("Game over. Your secret number was: {}".format(guess_int))






