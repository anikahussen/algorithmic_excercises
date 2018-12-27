#ask user for color amount and shirt amount 
color_amount = int(input("How many colors will each shirt be printed with (1, 2, or 3)? "))
shirt_amount = int(input("How many shirts do you want to purchase? "))
# set tax variable 
tax = 0.0875


#first if statement is for 1 color
#nested if statement shows the possibilities of shirt amounts
if color_amount == 1:
    if shirt_amount >=1 and shirt_amount <=99:
        total = shirt_amount * 8
    elif shirt_amount >=100 and shirt_amount <=249:    #only run through elif statement if the if statement above is false
        total = shirt_amount * 6
    elif shirt_amount >=250:
        total = shirt_amount * 5
  #repeat same procedure for the rest of the color amount answers (2 and 3)                  
if color_amount == 2:
    if shirt_amount >=1 and shirt_amount <=99:
        total = shirt_amount * 9
    elif shirt_amount >=100 and shirt_amount <=249:
        total = shirt_amount * 7
    elif shirt_amount >=250:
        total = shirt_amount * 6
                   

if color_amount == 3:
    if shirt_amount >=1 and shirt_amount <=99:
        total = shirt_amount * 10
    elif shirt_amount >=100 and shirt_amount <=249:
        total = shirt_amount * 8
    elif shirt_amount >=250:
        total = shirt_amount * 7
                   
 #take the total that program stopped at or ran and multiply by the set tax; take that number and add to total                  
price = (total * tax) + total
formatted_price = format(price, ".2f")     #format for float because when the integer total is multiplied by the float tax, the price becomes a float
                   
 #print answer  
                
print (shirt_amount, "shirts screen printed with" , color_amount, "colors:", formatted_price) 



                       
