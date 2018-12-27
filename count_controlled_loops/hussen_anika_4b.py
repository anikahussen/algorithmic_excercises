student_num = int(input ("How many students are in your class? "))

while student_num <= 0:
        print ("Invalid number of students, try again.")
        student_num = int(input ("How many students are in your class? "))
        
print ()   

test_num = int(input ("How many tests in this class? "))

while test_num < 0:
        print("Invalid number of tests, try again.")
        test_num = int(input ("How many tests in this class? "))
        print()
 

print("Ok, let's begin ...")
        
      


individual_score = 0
average_total = 0 
for i in range(1, student_num + 1):
    print()
    print ("**** Student #" + str(i) + " ****")
    for j in range(1, test_num + 1):   
        test_score = float(input("Enter a score for test #" + str(j) + ": "))
    
        while test_score < 0 or test_score > 100:
            print ("Invalid score, try again.")
            test_score = float(input("Enter a score for test #" + str(j) + ": "))
           
        individual_score += test_score
        average_score = individual_score/test_num
        formatted_average_score = format(average_score, ".2f")
        
    print ("Average score for student #" + str(i), "is", formatted_average_score)
    
    test_score = 0
    individual_score = 0
    average_total += average_score
    
    
average_total = average_total/(student_num)
formatted_average_total = format(average_total, ".2f")

print ()
print("Average score for all students is: ", formatted_average_total)


    

            
    
