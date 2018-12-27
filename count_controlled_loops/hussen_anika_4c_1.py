number = int(input("Enter a positive number to test: "))
            
while number < 0:
        print ("That is not a positive number.")
        number = int(input("Enter a positive number to test: "))
   

print ()

prime = True
if number == 1:
    prime = False


for i in range(2, number):
    if number % i == 0:
        print (i, "is a divisor of", number, ". . . continuing")
        prime = False
        
        break
    else:
        print (i, "is not a divisor of", number, ". . . continuing")
        
        
print ()
                     

if prime == True:
    print (number, "is a prime number.")
    
elif prime == False:
    print (number, "is not a prime number.")
