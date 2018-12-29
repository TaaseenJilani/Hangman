import random
print ("Hello, and welcome to Hangman.")
def list_of_words():
    words = ['Communication',
        'Bottle',
        'Technology',
        'Headphones',
        'Calculator']
    return random.choice(words).upper()
def check(word_gotten, guesses, guess):
    output = ""
    matches = 0
    for letter in word_gotten:
        if letter in guesses:
         output += letter
        else:
         output += "*"
        if letter == guess:
         matches += 1
    if matches > 1:
        print("Yes! The word contains " + str(matches)+ " " + str(guess) + "s")
    elif matches == 1:
        print("Yes! The word contains the letter " + str(guess) +".")
    else:
        print("Sorry. The word does not contain the letter " + str(guess) + ".")
    return output

def main():
   word_gotten = list_of_words()
   guesses = []
   guessed = False
   print("The word contains " + str(len(word_gotten)) + " letters.")
   while not guessed:
     guess = input("Please enter a letter or a " + str(len(word_gotten)) + " letter word: ")
     guess = guess.upper()
     if guess in guesses:
         print ("You have already guessed " + str(guess) + ".")
     elif len(guess) == len(word_gotten):
         guesses.append(guess)
         if guess == word_gotten:
           guessed = True
         else:
           print ("Sorry, that is incorrect")
     elif len(guess) == 1:
          guesses.append(guess)
          result = check(word_gotten, guesses, guess)
          if result == word_gotten:
              guessed = True
          else:
              print (result)
     else:
         print ("Invalid entry!")

   print ("Yes, the word is " + str(word_gotten) + "! You got it in " + str(len(guesses)) + " tries.")

main()
