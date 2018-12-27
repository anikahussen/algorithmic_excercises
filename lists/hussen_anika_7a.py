import math

test_range = int(input("Enter a number range: "))
test_list = ["P"] * (test_range+1)
test_list[0] = "N"
test_list[1] = "N"


for n in range(2, int(math.sqrt(test_range+1))):
    if test_list[n] == "P":
        for j in range(n+1, test_range+1):
            if j % n == 0:
                test_list[j] = "N"

count = 0
for i in range(0, test_range+1):
    if test_list[i] == "P":
        print(format(str(test_list.index("P")), ">8s"),end="")
        test_list[i]="SP"
        count += 1
        if count % 10 == 0:
            print("")

    
 
