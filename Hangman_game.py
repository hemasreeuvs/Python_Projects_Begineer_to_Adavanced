word_list=  ["planning" , "preparing" , "winning"]

import random
chosen_word = random.choice(word_list)
print(chosen_word)

game_over = False
correct_letters = []
lives = 6


while not game_over:

    guess = input("Guess a letter:").lower()
    print(guess)


    display =""


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+= letter
           
        else:
            display += "-"

    if guess not in chosen_word:
        lives-=1
        if lives == 0:
            print("you win")



    print(stages[lives])

     



    place_holder = ""
    word_length = len(chosen_word)
    
    for letter in range(6):
        place_holder += "-"
    print(place_holder)


 




