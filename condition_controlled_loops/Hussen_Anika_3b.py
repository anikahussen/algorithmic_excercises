
'''
#Prompt the user for the number of sides to the dice they will be rolling

dice_sides = int(input("How many sides are there on your dice (4-20)? "))



#Validate their input before you continue

while (dice_sides < 4) or (dice_sides > 20):  #condition for when invalid
    print ("Sorry, that's not a valid number of sides.", end = (" "))
    print ("Please choose a positive number between 4 and 20.")
    print ()
    dice_sides = int(input("How many sides on your dice (4-20)? "))
    
print("Ok, let's play!")
print ()


#import random module
import random

#generate virtual dice 
first_die = random.randint(1, dice_sides)
second_die = random.randint(1, dice_sides)
roll_count = 0

#accumulator variables
total_sum1 = 0


total_sum2 = 0
attempt_num = 1
doubles_count = 0


while attempt_num > 0:
    first_die = random.randint(1, dice_sides)
    total_sum1 += first_die
    second_die = random.randint(1, dice_sides)
    total_sum2 += second_die
    print (str(attempt_num) + ".", "The first die is" , first_die, "and the second die is", str(second_die) + ".")
    roll_count += 1
    attempt_num += 1
    if first_die == second_die:
        doubles_count += 1
    if first_die == 1 and second_die == 1:
        print ("")
        print ("You got snake eyes on try", str(roll_count) + ".")
        break
    

#print out doubles count

print ("Along the way you rolled doubles", str(doubles_count), "times.")

    
#Calculate average for first die

first_avg = total_sum1 / roll_count

print ("The average roll for the first die was: ", str(first_avg) + ".")

#Calculate average for second die

second_avg = total_sum2 / roll_count

print ("The average roll for the second die was: ", str(second_avg) + ".")

'''
import random

secret = random.randint(1,11)
guess = int(input("Enter your guess (1-11): "))

if guess > secret:
    print ("Too high, try again.")
    guess2 = int(input("Enter your guess (1-11): "))
    if guess2 == secret:
        print("You got it!")   #nested if statement for the next possibilities for the next guesses #Stop prompting
    elif guess2 < secret:
        print ("Too low, try again.")
elif guess < secret:
    print ("Too low, try again.")
    guess3 = int(input("Enter your guess (1-11): "))
    if guess3 == secret:
        print("You got it!")   #nested if statement for the next possibilities for the next guesses #Stop prompting
    elif guess3 < secret:
        print ("Too low, try again.")
elif guess == secret:
    print ("You got it.")

print ("The secret number", str(secret) + ".")
