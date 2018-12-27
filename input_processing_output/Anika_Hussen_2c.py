#import random module

import random

#generate random numbers from 1 to 11 inclusive

secret_number = random.randint (1, 11)

# variable for tries
x = 0

#Set up
print ("I'm thinking of a number between 1 and 11.")


#prompt user to guess secret number

guess_1 = int(input("Guess my secret number (First try!): "))   #convert to integer for mathematical operation use 
x+=1 #counts the tries the user takes (after prompted for a try) 
if guess_1 == secret_number:
    print("You got it!")  #Stop prompting
             
              
elif guess_1 < secret_number:
    print ("Too low, try again.")  #align elif statements with initial if statement for guess 1
    guess_2 = int(input("Guess my secret number (Second try!): "))
    x+=1 #counts the tries the user takes (after prompted for a try)
    if guess_2 == secret_number:
        print("You got it!")   #nested if statement for the next possibilities for the next guesses #Stop prompting
    elif guess_2 < secret_number:
        print ("Too low, try again.")
    
        
    elif guess_2 > secret_number:
        print ("Too high, try again.")
        guess_3 = int(input("Guess my secret number (Third try!): "))
        x+=1 #counts the tries the user takes (after prompted for a try)
        if guess_3 == secret_number:
            print("You got it!")   #Stop prompting
        elif guess_3 < secret_number:
            print ("Sorry, game over.")
        elif guess_3 > secret_number:
            print ("Sorry, game over.")
        
            
elif guess_1 > secret_number:
    print ("Too high, try again.")
    guess_2 = int(input("Guess my secret number (Second try!): "))
    x+=1 #counts the tries the user takes (after prompted for a try)
    if guess_2 == secret_number:
        print("You got it!")    #Stop prompting
    elif guess_2 < secret_number:
        print ("Too low, try again.")

        guess_3 = int(input("Guess my secret number (Third try!): "))
        x+=1 #counts the tries the user takes (after prompted for a try)
        if guess_3 == secret_number:
            print("You got it!")   
        elif guess_3 < secret_number:
            print ("Sorry, game over.")
        elif guess_3 > secret_number:
            print ("Game over.")
    elif guess_2 > secret_number:
        print ("Too high, try again.")

        guess_3 = int(input("Guess my secret number (Third try!): "))
        x+=1 #counts the tries the user takes (after prompted for a try)
        if guess_3 == secret_number:
            print("You got it!")    
        elif guess_3 < secret_number:
            print ("Sorry, game over.")
        elif guess_3 > secret_number:
            print ("Sorry, game over.")



print ()  #space in between print statements 
print ("The secret number was", str(secret)+".")   #convert secret_number to string in order to concatenate
print ("It took you", x, "tries.")    #the x comes from the program counting the tries taken 

    
