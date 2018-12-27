#Prompt the user for the number of sticks in the game

sticks = int(input("How many sticks to start with (10-100)? "))



#Validate their input before you continue


while True:
    if sticks > 100:  #condition for when invalid/too high
        print ("Sorry, that's too many sticks. Try again.")
        sticks = int(input("How many sticks to start with (10-100)? "))

    elif sticks < 10:  #condition for when invalid/too low
        print ("Sorry, that's too few sticks. Try again.")
        sticks = int(input("How many sticks to start with (10-100)? "))

    elif (sticks >= 10 and sticks <= 100):  #condition just right
        print ("Great, let's play.")
        print (" ")
        break



sticks_left = sticks  #reassigning to update total

#Player 1
while True:
    print ("Player 1 Turn")
    print ("There are", sticks_left, "sticks on the table.")  #print how many sticks there are (even before the first input)
    while True:
        sticks_pickup1 = int(input("How many sticks do you want to take (1, 2 or 3)? "))
        
        if sticks_pickup1 != 1 and sticks_pickup1 != 2 and sticks_pickup1 != 3:  #invalid instances of picking up sticks
            print("Sorry, that's not a valid number.") 
            print (" ")
        if sticks_pickup1 == 1 or sticks_pickup1 == 2 or sticks_pickup1 == 3: #valid instances of picking up sticks
            if sticks_pickup1 > sticks_left: #player can't pick up more than what is on the table
                print("You are trying to pick up too many sticks.")
                print (" ")
            elif sticks_pickup1 <= sticks_left: 
                break #once the player inputs a valid answer, break out of the inner loop
                
    sticks_left = sticks_left - sticks_pickup1 #evaluate what the new total (how many sticks left) on the table (reassign)
    
    print ()
    if sticks_left == 0:
        print("There are no sticks left on the table. Game over.") #once there are no sticks left, a player will win and the game is over
        print ("Player 2 Wins!")
        break #break out of the game (outer while loop)


#Player 2 (same as Player 1)
    print ("Player 2 Turn")
    print ("There are", sticks_left, "sticks on the table.")
    while True: #same indentation as the inner while loop for Player 1
        sticks_pickup2 = int(input("How many sticks do you want to take (1, 2 or 3)? "))
        
        if sticks_pickup2 != 1 and sticks_pickup2 != 2 and sticks_pickup2 != 3:
            print("Sorry, that's not a valid number.")
            print (" ")
        if sticks_pickup2 == 1 or sticks_pickup2 == 2 or sticks_pickup2 == 3:
            if sticks_pickup2 > sticks_left:
                print("You are trying to pick up too many sticks.")
                print (" ")
            elif sticks_pickup2 <= sticks_left:
                break
                
    sticks_left = sticks_left - sticks_pickup2
    
    print ()         
    if sticks_left == 0:
        print("There are no sticks left on the table. Game over.")
        print ("Player 1 Wins!")
        break  #break out of the game (outer while loop)          
