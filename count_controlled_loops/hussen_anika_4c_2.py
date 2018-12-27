


for i in range(2, 1001):
    prime = True
    for j in range (2,i):
        if i % j == 0:
            prime = False
            break
        
            
                  
    if prime == True:
        print(i, "is a prime number!")
                     



