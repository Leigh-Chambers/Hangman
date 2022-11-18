from AsciiArt import stages, logo
from hangman_words import word_list
from replit import clear
import random

print(logo+ "\n\n\nHere is your word. Take your guess\n\n")

chosen_word = random.choice(word_list)
blank_spaces = []

for _ in range(len(chosen_word)):
  blank_spaces += "_"
print(blank_spaces)
lives = 6

end_of_game = False

while not end_of_game: 
  guess = (input("Please make a guess:\n\n").lower())
  clear()
  if guess in blank_spaces:
    print(f"\nYou have already guessed the letter '{guess}''. Please choose a different letter.\n\n")
    
    
  elif guess in chosen_word:
    for x in range(len(chosen_word)):
      y = chosen_word[x]
      if guess == y:
        blank_spaces[x] = y
  elif guess not in chosen_word:
    lives-=1
    print(f"\nYou guessed '{guess}'', that is not in this word. you lose a life. \n{lives} lives remaining!\n\n")
    
    if lives == 0:
      print(f"\nSorry! The word was {chosen_word}\n")
      print("\nGame Over!\n")
      break
      
  else:
    continue
  
  print(f"\n\n{' '.join(blank_spaces)}")
  print(stages[lives])
  #Checking if the player has won
  if "_" not in blank_spaces:
    end_of_game = True
    print("You have won! Congratulations")
   
  
  

