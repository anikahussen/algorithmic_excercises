
import myfunctions
import random

#input settings and validate

attempts = int(input("How many problems would you like to attempt? "))

while attempts <= 0:
    if attempts == 0:
        print("No inputs.")
        attempts = int(input("How many problems would you like to attempt? ")) 
    
    elif attempts < 0:
        print ("Invalid number, try again")
        attempts = int(input("How many problems would you like to attempt? "))

       
        

width = int(input("How wide do you want your digits to be? 5-10: "))

while width < 5 or width > 10:
    print ("Invalid width, try again")
    width = int(input("How wide do you want your digits to be? 5-10: "))


print()   
print ("Here we go!")
print()



correct_count = 0
attempt_num = 0
while attempt_num < attempts:
    print ("What is...")
    print()
    #random operand 1 


    digital_operand1 = random.randint(0,9)
    number1 = digital_operand1    
        
    if digital_operand1 == 0:
        digital_operand1 = myfunctions.number_0(width)
    elif digital_operand1 == 1:
        digital_operand1 = myfunctions.number_1(width)
    elif digital_operand1 == 2:
        digital_operand1 = myfunctions.number_2(width)
    elif digital_operand1 == 3:
        digital_operand1 = myfunctions.number_3(width)
    elif digital_operand1 == 4:
        digital_operand1 = myfunctions.number_4(width)
    elif digital_operand1 == 5:
        digital_operand1 = myfunctions.number_5(width)
    elif digital_operand1 == 6:
        digital_operand1 = myfunctions.number_6(width)
    elif digital_operand1 == 7:
        digital_operand1 = myfunctions.number_7(width)
    elif digital_operand1 == 8:
        digital_operand1 = myfunctions.number_8(width)
    elif digital_operand1 == 9:
        digital_operand1 = myfunctions.number_9(width)



    #random operation sign

  
    operation = random.randint(0,1)
    
    if operation == 0:
        
        myfunctions.addition(width)
        operator = "+"
        

        
    elif operation == 1:
        myfunctions.subtraction(width)
        operator = "-"
        



    #random operand 2
      

    digital_operand2 = random.randint(0,9)
    number2 = digital_operand2
       
        
    if digital_operand2 == 0:
        digital_operand2 = myfunctions.number_0(width)
    elif digital_operand2 == 1:
        digital_operand2 = myfunctions.number_1(width)
    elif digital_operand2 == 2:
        digital_operand2 = myfunctions.number_2(width)
    elif digital_operand2 == 3:
        digital_operand2 = myfunctions.number_3(width)
    elif digital_operand2 == 4:
        digital_operand2 = myfunctions.number_4(width)
    elif digital_operand2 == 5:
        digital_operand2 = myfunctions.number_5(width)
    elif digital_operand2 == 6:
        digital_operand2 = myfunctions.number_6(width)
    elif digital_operand2 == 7:
        digital_operand2 = myfunctions.number_7(width)
    elif digital_operand2 == 8:
        digital_operand2 = myfunctions.number_8(width)
    elif digital_operand2 == 9:
        digital_operand2 = myfunctions.number_9(width)
        
    attempt_num += 1

    
    
    answer = int(input("= "))
    check = myfunctions.check_answer(number1,number2,answer,operator)
    
    if check == True:
        print ("Correct!")
        correct_count+=1
        
    elif check == False:
        print ("Sorry, that is not correct.")
        
print()      
print ("You got", correct_count, "out of", attempts, "correct.")
        
