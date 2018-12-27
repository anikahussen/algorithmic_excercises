start_number = int(input("Start number: "))
end_number = int(input("End number: "))


while start_number < 0 or end_number < 0:
    if start_number > end_number:
        print ("End number must be greater than start number.")
        print ("Start and end must be positive.")
        print ()
        start_number = int(input("Start number: "))
        end_number = int(input("End number: "))
            
    elif start_number < end_number:
        print ("Start and end must be positive.")
        print ()
        start_number = int(input("Start number: "))
        end_number = int(input("End number: "))
        

    elif start_number == end_number:
        print ("Start and end must be positive.")
        print ()
        start_number = int(input("Start number: "))
        end_number = int(input("End number: "))


while start_number > 0 or end_number > 0:
    if start_number > end_number:
        print ("End number must be greater than start number.")
        print ()
        start_number = int(input("Start number: "))
        end_number = int(input("End number: "))


    elif start_number <= end_number:
       
        break

print ()


for i in range(start_number, end_number + 1):

    if i == 1:
        continue
    prime = True
    
    for j in range (2, i):
        if i % j == 0:
            prime = False
            break
        
            
                  
    if prime == True:
        print(i)
                        
