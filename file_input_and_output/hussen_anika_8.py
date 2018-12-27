

file_name = input("Enter a class to grade (i.e. class1 for class1.txt): ")

try:
    file = open(file_name+".txt", 'r')
    
except FileNotFoundError:
        print('File not found.')
else:
    print("Successfully opened", file_name+".txt")
    lines = file.read().split('\n') #splitting file, turning into list of lines/student info
    file.close()
    print()

#########################################################################

    #line count
    lines_total = 0
    invalid_lines_total = 0
    valid_lines_total = 0




    print()
    print("**** ANALYZING ****")


    total_of_scores = 0 #score count
    score_list = [] #accumulating individual scores
    writing_file = open(file_name+"_grades.txt", 'w')

    #iterating every student separately
    for line in lines:
        
        a = True #when valid line
        if line[0] != "N":
            print ("Invalid line of data: N# is invalid")
            print(line)
            print()
            invalid_lines_total += 1
            a = False #when invalid line
            
        for char in line[1:9]:
            if not char.isnumeric():
                print ("Invalid line of data: N# is invalid")
                print (line)
                print ()
                invalid_lines_total += 1
                a = False #when invalid line
        
        #split scores
        val = line.split(',')
        
        if len(val) != 26:
            print ("Invalid line of data: does not contain exactly 26 values")
            print(line)
            print ()
            invalid_lines_total += 1
            a = False #when invalid line

        if a==True:
            valid_lines_total += 1 #if nothing turns "a" false



            answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
            real_answers = answer_key.split(',') #splitting the answer key, turning into list

            
            
            
            individual_score = 0
            
            for n in range (0, len(val)-1):
                if val[n+1] == real_answers[n]:
                    individual_score += 4
                elif  val[n+1] == '':
                    individual_score += 0
                elif val[n+1] != real_answers[n] and val[n+1] != "" :
                    individual_score -= 1
                
            score_list += [individual_score] #accumulate each students score

            writing_file.write(val[0]+","+str(individual_score)+ "\n")
                
            
            total_of_scores +=  individual_score
        lines_total += 1


    writing_file.close()


    if invalid_lines_total==0:
        print("No errors found!") #when there are no invalid lines, there will be no errors
        
        

    #Calculations
    #average
    avg = total_of_scores / valid_lines_total #valid students
    formatted_average = format(avg, ".2f")

    #highest score
    high_score = max(score_list)

    #lowest score
    low_score = min(score_list)

    #range of scores
    range_of_scores = high_score - low_score

    #median score

    #create a duplicate list to sort, but preserve original score list
    sorting_score_list = []
    for i in score_list:
        sorting_score_list.append(i)

    sorting_score_list.sort()


    if valid_lines_total % 2 != 0: #odd
        half_mark = len(sorting_score_list) // 2
        #index after the half mark is the median // since the index starts with 0, it is not one above, but the same
        med_score = sorting_score_list[half_mark]
    elif valid_lines_total % 2 == 0: #even
        half_mark = len(sorting_score_list) // 2
        mid1 = sorting_score_list[half_mark-1]
        mid2 = sorting_score_list[half_mark]
        sum_of_mid = mid1 + mid2
        avg_of_mid = sum_of_mid /2
        med_score =  avg_of_mid



    print()
    print ("**** REPORT ****")
    print()
    print ("Total valid lines of data:", valid_lines_total) #num of students
    print ("Total invalid lines of data:", invalid_lines_total)
    print()
    print ("Overall Total of Lines:", lines_total)
    print()
    print()
    print("Mean (average) score:", (formatted_average))
    print("Highest Score: ", high_score)
    print("Lowest Score: ", low_score)    
    print("Range of scores:", range_of_scores)
    print("Median scores:", med_score)





        
