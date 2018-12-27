# algorithmic_excercises

##Algorithm Instructions
##
##Think about a routine activity—it can be anything from buying lunch to brushing your teeth—and break it down into an algorithm. Make a detailed list of the steps involved in this activity. Your procedure should be at least 10 steps long and pay attention to the subconscious motions involved in the activity.
##
##Write a Python program that assigns each individual step of your algorithmic process to its own variable. Then, print all of the steps to the screen using these variables along with the print() function. Your program should also include at least one code comment.
##
##
################################################
##
##Input, Processing, Output Instructions
##
##Part A
##Create a template word game, in the style of Mad Libs, that prompts users for a series of at least five words (adjective, verb, animal, place, etc.). Insert these parts of speech into a prewritten text that will generate a story or prose poem with the user’s vocabulary and print it to the screen.
##
##Part B
##When you invest money in a savings account your money earns a certain amount of interest over a period of time. For example, investing $100 in an account that yields 1% interest annually would mean that after 1 year your account would be worth $101.
##
##If you left this money in your account you would earn additional interest in the following year due to the fact that your account now has $101 instead of the initial deposit of $100. You would earn interest on the initial deposit plus the $1 you earned in interest—this is called “compound interest.”
##
##For this problem, you will write a program that calculates how much a person can earn by investing in a high-yield savings account. The program should ask the user for an initial deposit amount and an interest rate. The program will then generate a 3-month projection that illustrates how much money the user can expect to earn. Assume that interest is compounded monthly (i.e. if your account earns a rate of 12% interest annually then you would earn a rate of 1% per month). Here’s a sample running of the program:
##
##This program will project how much you can earn by investing money in a high-yield savings account over a 3-month period.
##
##To begin, enter how much money you would like to initially invest (i.e. 500): 500
##Next, enter your projected annual interest rate. For example, enter 0.05 for 5%: 0.05
##
##Calculating . . .
##
##Month Starting Balance     Interest   Ending Balance      
##1     500.00               2.08       502.08              
##2     502.08               2.09       504.18              
##3     504.18               2.10       506.28
##And here’s another sample running:
##
##This program will project how much you can earn by investing money in a high-yield savings account over a 3-month period.
##
##To begin, enter how much money you would like to initially invest (i.e. 500): 10000
##Next, enter your projected annual interest rate. For example, enter 0.05 for 5%: 0.05
##
##Calculating . . .
##
##Month Starting Balance     Interest   Ending Balance      
##1     10,000.00            41.67      10,041.67           
##2     10,041.67            41.84      10,083.51           
##3     10,083.51            42.01      10,125.52
##You can assume that the user will enter reasonable input values (i.e. all input will be valid positive floating point numbers). Use the format() function to ensure that your values line up as in the sample output above.
##
##Part C
##Write a program that prompts the user to enter a file size in kilobytes (KB). Convert the supplied input into bits, bytes, megabytes, and gigabytes with the following conversion values.
##
##8 bits = 1 byte
##1024 bytes = 1 kilobyte (KB)
##1024 kilobytes = 1 megabyte (MB)
##1024 megabytes = 1 gigabyte (GB)
##Output your results as follows. Your converted values should line up in a column (right-justified) followed by the units of measurement (left justified). Format your converted values to one decimal place, and add comma separators as necessary.
##
##Enter a file size in kilobytes (KB): 20000
##
##20000 KB ...
##
##... in bits                163,840,000.0 bits                
##... in bytes                20,480,000.0 bytes               
##... in megabytes                    19.5 MB                  
##... in gigabytes                     0.0 GB
##You may assume that your user gives you a reasonable number to work with. Use the format() function to line up the results neatly.
##
##Finally, list out at least five ways to “crash” the program and document your errors. Include examples of at least one syntax error, one logic (semantic) error, and one run-time error. Include these errors as comments in the program so that the program will still run! Here’s an example:
##
### the following line would cause a syntax error because I forgot
### to delimit the string literal I am attempting to print out
### print(Hello, World!)
##
################################################
##
##Control Structures Instructions
##
##
##Part A
##A New York City screen printing company charges different rates depending on how many T-shirts a customer would like to have printed and how many colors will be used. The rates are as follows.
##
##1 color
##1–99 shirts: $8 per shirt
##100–249 shirts: $6 per shirt
##250 or more shirts: $5 per shirt
##2 colors
##1–99 shirts: $9 per shirt
##100–249 shirts: $7 per shirt
##250 or more shirts: $6 per shirt
##3 colors
##1–99 shirts: $10 per shirt
##100–249 shirts: $8 per shirt
##250 or more shirts: $7 per shirt
##Write a program in which a user can enter the number of T-shirts they would like screen-printed and with how many colors (1, 2, or 3). Calculate the cost based on the company’s rates and include New York sales and use tax of 8.875%. Print this total dollar amount to the screen, formatted to two decimal places. Here is a demo of the program.
##
##Your Screen Printing Quote
##
##How many T-shirts would you like to have printed? 200
##How many colors will each shirt be printed with (1, 2, or 3)? 2
##
##200 shirts screen printed with 2 colors: $1,524.25
##Part B
##Write a program that asks users when their birthday is. Use information provided to give them their astrological sign and a fictional horoscope. Each of the twelve signs should display a different horoscope. Use the following dates for each sign, keeping in mind that both month and day must be evaluated for an accurate result.
##
##Aries: March 21–April 20
##Taurus: April 21–May 21
##Gemini: May 22–June 21
##Cancer: June 22–July 22
##Leo: July 23–August 22
##Virgo: August 23–September 23
##Libra: September 24–October 23
##Scorpio: October 24–November 22
##Sagittarius: November 23–December 21
##Capricorn: December 22–January 20
##Aquarius: January 21–February 19
##Pisces: February 20–March 20
##Here is a demo of the program. Feel free to prompt users to provide their birth month and day in a way that is simple for you to work with.
##
##Your horoscope awaits you . . .
##          
##Enter your birth month (1-12): 9
##Enter your birth day (1-31): 22
##
##You are a Virgo.
##          
##Listen to what your heart is telling you.
##Part C
##Write a game program in which the user must guess a randomly generated number within three tries. The program should start by generating a random whole number between (and including) 1 and 11. Prompt the user to guess this number and tell them whether or not their guess is correct.
##
##If the user does not guess the number, indicate whether it is higher or lower than their guess and prompt the user to try again. If the user guesses correctly, tell them that they have won and stop prompting the user to guess. If, after three tries, the user has not guessed the number, tell them that the game is over and stop.
##
##Here are two demos of the program.
##
##I'm thinking of a number between 1 and 11.
##  				
##Guess my number: 5
##Too low, try again.
##
##Guess my number: 8
##Too high, try again.
##
##Guess my number: 7
##You got it!
##
##The secret number was 7.
##It took you 3 tries to guess the number.
##I'm thinking of a number between 1 and 11.
##  				
##Guess my number: 6
##Too low, try again.
##
##Guess my number: 11
##Too high, try again.
##
##Guess my number: 9
##Sorry, game over.
##
##The secret number was 8.
##
################################################
##
##
##Condition-Controlled Loops Instructions
##
##Part A
##Using nested while-loops, calculate and print the basic multiplication table of numbers 1–9. Format the output so that columns line up as follows.
##
##  1   2   3   4   5   6   7   8   9 
##  2   4   6   8  10  12  14  16  18 
##  3   6   9  12  15  18  21  24  27 
##  4   8  12  16  20  24  28  32  36 
##  5  10  15  20  25  30  35  40  45 
##  6  12  18  24  30  36  42  48  54 
##  7  14  21  28  35  42  49  56  63 
##  8  16  24  32  40  48  56  64  72 
##  9  18  27  36  45  54  63  72  81 
##Part B
##In games with two dice, rolling two 6-sided dice and getting the same side or number on both is called “doubles” (i.e. the first die rolls a 5 and the second die rolls a 5 at the same time). One special type of doubles roll is called “snake eyes,” which is rolling two 1s at the same time.
##
##For this assignment you will be writing a program which first prompts the user for the number of sides to the dice they will be rolling. Your user should be able to input any positive value between 4 and 20 for the number of the sides on their dice, and you can assume that they will enter integers when prompted.
##
##You will need to validate their input before you continue (i.e. entering -10 should cause your program to tell the user that their input is invalid). You should re-prompt the user to enter a value if they supply bad data. Hint: Use a “while” loop to keep the user “trapped” until they supply you with “good” data.
##
##pair of lucite dice
##Next, your program should keep “rolling the dice” until it gets snake eyes. This means that you will roll two virtual dice of the specified size at a time. The program should announce every pair rolled and then tell the user how many rolls were required to get a pair of 1s. You should also keep track of how many times your roll came up with doubles along the way (but don’t end the program until you roll “snake eyes”).
##
##In addition, you will calculate the average roll for each die and present this information to the user. See the sample program below to see what this should look like. Format this number to one decimal place.
##
##How many sides on your dice (4-20)? -10
##Sorry, that's not a valid number of sides. Please choose a positive number between 4 and 20.
##
##How many sides on your dice (4-20)? 30
##Sorry, that's not a valid number of sides. Please choose a positive number between 4 and 20.
##
##How many sides on your dice (4-20)? 6
##Ok, here we go . . .
##
##1. The first die is 5 and the second die is 3
##2. The first die is 2 and the second die is 2
##3. The first die is 1 and the second die is 5
##4. The first die is 6 and the second die is 1
##. . . continue . . . 
##16. The first die is 1 and the second die is 1
##
##You got snake eyes on try number 16!
##Along the way you rolled doubles 5 times.
##The average roll for the first die was: 2.9
##The average roll for the second die was: 3.2
##Note that the “snake eyes” roll that causes your loop to end should also count as a “doubles” roll.
##
##Part C
##For Part C, you will be creating an interface for two people to play a simple game of “Pick-Up Sticks.” Here’s how the game is to be played.
##
##The game begins with a number of sticks on a table—between 10 and 100.
##Each player, in turn, picks up 1–3 sticks off the table.
##The player to take the last stick loses.
##Your job is to build a virtual version of the game using Python. The program is broken into a series of parts to help you understand how to put together a game with several different components. Each part builds on the previous one so you should complete them in order and only turn in the final part (the two-player version) as your solution.
##
##wooden pick-up sticks
##Single-Player Game
##Begin by asking the user for a number of sticks to be used in the game. Only accept numbers between 10 and 100—if the user supplies a number outside of this range you should prompt them to re-enter the number.
##
##Next, continually announce to the user how many sticks are on the table and ask the user to enter a number of sticks to take away. Only accept choices of 1, 2, or 3 sticks—anything else should cause an error message to be displayed. Once a valid number of sticks has been entered, you should deduct that number from the total number of sticks in the game. When you reach 0 sticks left, the game is over.
##
##Here is a sample running of the program.
##
##How many sticks to start with (10-100)? 999
##Sorry, that's too many sticks. Try again.
##
##How many sticks to start with (10-100)? -10
##Sorry, that's too few sticks. Try again.
##
##How many sticks to start with (10-100)? 10
##Great, let's play . . .
##
##There are 10 sticks on the table.
##How many sticks do you want to take (1, 2 or 3)? 999
##Sorry, that's not a valid number.
##
##There are 10 sticks on the table.
##How many sticks do you want to take (1, 2 or 3)? 0
##Sorry, that's not a valid number.
##
##There are 10 sticks on the table.
##How many sticks do you want to take (1, 2 or 3)? 3
##
##There are 7 sticks on the table.
##How many sticks do you want to take (1, 2 or 3)? 2
##
##There are 5 sticks on the table.
##How many sticks do you want to take (1, 2 or 3)? 3
##
##There are 2 sticks on the table.
##How many sticks do you want to take (1, 2 or 3)? 2
##
##There are no sticks left on the table. Game over.
##Two-Player Game
##As you can see, the single-player version of this game isn’t very fun. To make things more interesting we are now going to add an element of competition. For this part you will be implementing a two-player game where players take turns picking up sticks from the table. The same rules apply—each player can only take 1, 2, or 3 sticks per turn. The player who takes the last stick off of the table loses.
##
##Here is a sample running of the game.
##
##How many sticks to start with (10-100)? 250
##Sorry, that's too many sticks. Try again.
##
##How many sticks to start with (10-100)? 10
##Great, let's play . . .
##
##Turn: Player 1
##There are 10 sticks on the table.
##How many sticks do you want to take (1, 2 or 3)? 999
##Sorry, that's not a valid number.
##
##Turn: Player 1
##There are 10 sticks on the table.
##How many sticks do you want to take (1, 2 or 3)? 0
##Sorry, that's not a valid number.
##
##Turn: Player 1
##There are 10 sticks on the table.
##How many sticks do you want to take (1, 2 or 3)? 3
##
##Turn: Player 2
##There are 7 sticks on the table.
##How many sticks do you want to take (1, 2 or 3)? 2
##
##Turn: Player 1
##There are 5 sticks on the table.
##How many sticks do you want to take (1, 2 or 3)? 3
##
##Turn: Player 2
##There are 2 sticks on the table.
##How many sticks do you want to take (1, 2 or 3)? 1
##
##Turn: Player 1
##There is 1 stick on the table.
##How many sticks do you want to take (1, 2 or 3)? 0
##Sorry, that's not a valid number.
##
##Turn: Player 1
##There is 1 stick on the table.
##How many sticks do you want to take (1, 2 or 3)? 1
##
##There are no sticks left on the table. Game over.  
##Player 2 wins!
##Here are some hints to get you started.
##
##You may want to use a variable to keep track of the players and who’s turn it is.
##You only want to switch turns when the player takes a valid number of sticks.
##Don’t allow players to take more than the total number of sticks on the table. For example, if there are two sticks left the player should not be able to take three sticks.
##The player who does not take the last stick is the winner.
##
##
################################################
##
##
##Count-Controlled Loops Instructions
##
##ASCII, the American Standard Code for Information Interchange, is a 20th century character-encoding scheme used to represent text in computers. Originally based on the English alphabet, ASCII includes just 128 basic characters: numbers 0 to 9, lowercase letters a to z, uppercase letters A to Z, basic punctuation symbols, the space character, and a few other non-printing characters. This means that all special punctuation, symbols, and non-Western characters cannot be represented in ASCII.
##
##Here are all the printable ASCII characters—including a space—enclosed in single quotes.
##
##' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
##
##Using the string above, write a program that prompts a user to enter a text. Compare this text to the ASCII string and print out the following information.
##
##The total number of characters (including spaces) in the text
##The total number of ASCII characters in the text
##The total number of non-ASCII characters in the text
##Here is a sample running of the program.
##
##Enter a text to analyze: Let’s go to the café on Sullivan St.
##
##Total number of characters: 36
##Total number of ASCII characters: 34
##Total number of non-ASCII characters: 2
##Part B
##Write a gradebook program that lets a teacher keep track of test averages for their students. Your program should begin by asking the teacher for a number of students in their class as well as the total number of tests that will be given to the class. Validate this information to ensure that the numbers entered are positive.
##
##Next, prompt the teacher to enter in scores for each student. Ensure that the values entered are positive—if they aren’t you will need to prompt them again. You may need to use nested loops for this; a “while” loop can be placed inside of a “for” loop as necessary.
##
##Once your program has collected all test scores for a student it should display that student’s average and move on to the next student. When all students have been calculated the program should compute the overall average score for the entire class.
##
##Here is a sample running of the program:
##
##How many students are in your class? -5
##Invalid number of students, try again.
##How many students are in your class? 3
##
##How many tests in this class? -10
##Invalid number of tests, try again.
##How many tests in this class? 2
##
##Ok, let’s begin . . .
##
##**** Student #1 ****
##Enter score for test #1: -50
##Invalid score, try again.
##Enter score for test #1: 50
##Enter score for test #2: 75
##Average score for student #1 is 62.50
##
##**** Student #2 ****
##Enter score for test #1: 100
##Enter score for test #2: 90
##Average score for student #2 is 95.00
##
##**** Student #3 ****
##Enter score for test #1: -10
##Invalid score, try again.
##Enter score for test #1: -20
##Invalid score, try again.
##Enter score for test #1: -30
##Invalid score, try again.
##Enter score for test #1: 90
##Enter score for test #2: 80
##Average score for student #3 is 85.00
##
##Average score for all students is: 80.83
##Here are a few tips as you get started.
##
##Begin by constructing a “for” loop to iterate over all students in the class.
##Once you’re inside of this “for” loop you will probably need another loop to handle inputting the scores for a particular student.
##Hint: Try to get your program to work first without any data validation. You can add this later once you figure out the general structure of the program.
##Keep in mind the difference between “for” and while” loops. “for” loops are used when you want to iterate over a known number of items; “while” loops can be used to keep the user stuck in place until they fulfill a particular condition. You will probably need to use a combination of these loops to solve this problem.
##Part C
##For Part C, you will write three different programs that identify prime numbers. A prime number is a number that has no positive divisors other than 1 and itself. For example, 5 is prime because the only numbers that evenly divide into 5 are 1 and 5. 6, however, is not prime because 1, 2, 3 and 6 are all divisors of 6.
##
##Program 1
##Your first program should prompt the user to enter in a positive number and cycle through its divisors to determine if the number is prime. Only accept positive numbers—if the user supplies a negative number or zero you should re-prompt them. Here is a demonstration of the program.
##
##Enter a positive number to test: 5
##
##2 is not a divisor of 5 . . . continuing
##3 is not a divisor of 5 . . . continuing
##4 is not a divisor of 5 . . . continuing
##
##5 is a prime number!
##Here’s another demo:
##
##Enter a positive number to test: 9
##
##2 is not a divisor of 9 . . . continuing
##3 is a divisor of 9 . . . stopping
##
##9 is not a prime number.
##Some notes on your program:
##
##1 is technically not a prime number.
##Once you find a number that evenly divides into your test number you do not need to continue testing additional numbers—the number cannot be prime.
##Hint: You cannot determine if a number is prime until you look at all potential divisors. Therefore you can’t report to the user that a number is prime within your loop structure.
##This program should be named as follows: lastname_firstname_4c_1.py
##
##Program 2
##Your second program for Part C should find all prime numbers between 1 and 1000.
##
##Make a copy of your first program and update it so that the program now finds all prime numbers between 1 and 1000. Here’s a sample running of the second program:
##
##2 is a prime number!
##3 is a prime number!
##5 is a prime number!
##7 is a prime number!
##11 is a prime number!
##
##. . . cut . . .
##
##977 is a prime number!
##983 is a prime number!
##991 is a prime number!
##997 is a prime number!
##This program should be named as follows: lastname_firstname_4c_2.py
##
##Program 3
##For your third program for Part C, make a copy of program 2 and update it so that the user can choose to examine a specific range of numbers for prime numbers. Here’s a sample running of your program.
##
##Start number: 5
##End number: -5
##Start and end must be positive.
##
##Start number: 5
##End number: 3
##End number must be greater than start number.
##
##Start number: 5
##End number: 23
##
##5
##7
##11
##13
##17
##19
##23
##Some notes on your program:
##
##You need to ensure that the start and end numbers are both postive.
##You also need to ensure that the start number is less than the end number.
##
##
##
################################################
##
##Functions Instructions
##
##Part 1
##For Part 1 you will write three line-drawing functions.
##
### function:   horizontal_line
### input:      a width value (integer)
### processing: prints a single horizontal line of the desired size
### output:     does not return anything
### function:   vertical_line
### input:      a shift value and a height value (both integers)
### processing: generates a single vertical line of the desired height. the line is
###             offset from the left side of the screen using the shift value
### output:     does not return anything
### function:   two_vertical_lines
### input:      a width value and a height value (both integers)
### processing: generates two vertical lines. the first line is along the left side of
###             the screen. the second line is offset using the "width" value supplied
### output:     does not return anything
##Here is a sample program that you can use to test your functions. The expected output is printed below the sample code:
##
##print("Horizontal line, width = 5:")
##horizontal_line(5)
##print()
##
##print("Horizontal line, width = 10:")
##horizontal_line(10)
##print()
##
##print("Horizontal line, width = 15:")
##horizontal_line(15)
##print()
##
##print("Vertical Line, shift = 0; height = 3:")
##vertical_line(0, 3)
##print()
##
##print("Vertical Line, shift = 3; height = 3:")
##vertical_line(3, 3)
##print()
##
##print("Vertical Line, shift = 6; height = 5:")
##vertical_line(6, 5)
##print()
##
##print("Two Vertical Lines, height = 3; width = 3:")
##two_vertical_lines(3, 3)
##print()
##
##print("Two Vertical Lines, height = 4; width = 5:")
##two_vertical_lines(4, 5)
##print()
##
##print("Two Vertical Lines, height = 5; width = 2:")
##two_vertical_lines(5, 2)
##Expected Output:
##
##Horizontal line, width = 5:
##*****
##
##Horizontal line, width = 10:
##**********
##
##Horizontal line, width = 15:
##***************
##
##Vertical Line, shift = 0; height = 3:
##*
##*
##*
##
##Vertical Line, shift = 3; height = 3:
##   *
##   *
##   *
##
##Vertical Line, shift = 6; height = 5:
##      *
##      *
##      *
##      *
##      *
##
##Two Vertical Lines, height = 3; width = 3:
##* *
##* *
##* *
##
##Two Vertical Lines, height = 4; width = 5:
##*   *
##*   *
##*   *
##*   *
##
##Two Vertical Lines, height = 5; width = 2:
##**
##**
##**
##**
##**
##Part 2
##Next, write 10 new functions that generate the digits 0-9 using your three line functions. The goal here is to render the digits as they would appear on a digital display:
##
##Digital display
##Each function should accept a “width” argument to control how wide the number should be. You can assume numbers will always be printed with a height of 5. For example, here is the function for the number 1:
##
### function:   number_1
### input:      a width value (integer)
### processing: prints the number 1 as it would appear on a digital display
###             using the supplied width value
### output:     returns nothing
##def number_1(width):
##	vertical_line(width-1, 5)
##And here’s a sample program that calls the function a few times:
##
##print("Number 1, width = 5: ")
##number_1(5)
##print()
##
##print("Number 1, width = 10: ")
##number_1(10)
##print()
##
##print("Number 1, width = 2: ")
##number_1(2)
##And here’s the expected output:
##
##Number 1, width = 5: 
##    *
##    *
##    *
##    *
##    *
##
##Number 1, width = 10: 
##         *
##         *
##         *
##         *
##         *
##
##Number 1, width = 2: 
## *
## *
## *
## *
## *
##Here’s a sample program that prints all of the numbers (0–9).
##
##number_0(5)
##print()
##
##number_1(5)
##print()
##
##number_2(5)
##print()
##
##number_3(5)
##print()
##
##number_4(5)
##print()
##
##number_5(5)
##print()
##
##number_6(5)
##print()
##
##number_7(5)
##print()
##
##number_8(5)
##print()
##
##number_9(5)
##And here’s the expected output:
##
##*****
##*   *
##*   *
##*   *
##*****
##
##    *
##    *
##    *
##    *
##    *
##
##*****
##    *
##*****
##*
##*****
##
##*****
##    *
##*****
##    *
##*****
##
##*   *
##*   *
##*****
##    *
##    *
##
##*****
##*
##*****
##    *
##*****
##
##*****
##*
##*****
##*   *
##*****
##
##*****
##    *
##    *
##    *
##    *
##
##*****
##*   *
##*****
##*   *
##*****
##
##*****
##*   *
##*****
##    *
##    *
##Part 3
##Write two new functions that simulate the addition and subtraction operators. Here’s some sample code:
##
##plus(5)
##
##print()
##
##minus(5)
##Which will generate . . .
##
##  *
##  *
##*****
##  *
##  *
##
##
##
##*****
##
##
##You can assume the height of these operators is the same as the height of your numbers (5 units).
##
##Part 4
##Write a function called “check_answer” which will determine if a given addition or subtraction problem was solved correctly. Here’s the IPO notation for the function:
##
### function:   check_answer
### input:      two numbers (number1 & number2, both integers); an answer (an integer)
###             and an operator (+ or -, expressed as a String)
### processing: determines if the supplied expression is correct.  for example, if the operator
###             is "+", number1 = 1, number2 = 2 and answer = 3 then the expression is correct
###             (1 + 2 = 3).
### output:     returns True if the expression is correct, False if it is not correct
##Here’s a sample program that you can use to test your function:
##
##answer1 = check_answer(1, 2, 3, "+")
##print(answer1)
##
##answer2 = check_answer(1, 2, -1, "-")
##print(answer2)
##
##answer3 = check_answer(9, 5, 3, "+")
##print(answer3)
##
##answer4 = check_answer(8, 2, 4, "-")
##print(answer4)
##And here’s the expected output:
##
##True
##True
##False
##False
##Part 5
##Move all of your functions into an external module. This can be done by creating a new .py file in the same folder as your source code file. You can then “import” the functions from this file by using the following syntax:
##
##import myfunctions
##. . . assuming that the file you created is named “myfunctions.py”. You can then call your functions in your main source code file using “dot syntax”, like this:
##
##myfunctions.check_answer(1, 1, 2, "+")
##Part 6
##Finally, put everything together and write a program that lets the user practice a series of random addition and subtraction problems. Begin by asking the user for a number of problems (only accept positive values) and a size for their numbers (only accept numbers between 5 and 10 for width). Then generate a series of random addition and subtraction problems—display the numbers to the user with your digital display functions. Then prompt the user for an answer and check the answer using your check_answer function. Your program should also keep track of how many correct questions the user answered during their game. Here’s a sample running of the program:
##
##How many problems would you like to attempt? -5
##Invalid number, try again
##
##How many problems would you like to attempt? 5
##How wide do you want your digits to be? 5-10: 3
##Invalid width, try again
##
##How wide do you want your digits to be? 5-10: 5
##
##Here we go!
##
##What is . . .
##
##*****
##    *
##*****
##    *
##*****
##
##  *
##  *
##*****
##  *
##  *
##
##    *
##    *
##    *
##    *
##    *
##
##= 4
##Correct!
##
##What is . . .
##
##*****
##    *
##*****
##*
##*****
##
##
##
##*****
##
##
##
##*****
##    *
##    *
##    *
##    *
##
##= -5
##Correct!
##
##What is . . .
##
##    *
##    *
##    *
##    *
##    *
##
##
##
##*****
##
##
##
##*****
##*
##*****
##    *
##*****
##
##= 0
##Sorry, that's not correct.
##
##What is . . .
##
##*****
##    *
##*****
##*
##*****
##
##  *
##  *
##*****
##  *
##  *
##
##    *
##    *
##    *
##    *
##    *
##
##= 3
##Correct!
##
##What is . . .
##
##*****
##    *
##*****
##*
##*****
##
##  *
##  *
##*****
##  *
##  *
##
##*****
##    *
##*****
##*
##*****
##
##= 4
##Correct!
##
##You got 4 out of 5 correct!
##
######################################
##
##Strings Instructions
##
##Part A
##In Python, there are three main rules for naming variables.
##
##The first character cannot be a number.
##Only letters, numbers, and the underscore character are allowed.
##Python keywords are reserved and cannot be used as variable names.*
##Write a program that prompts users to enter a potential variable name and tells them whether or not it is valid. Your program should consist of two functions. The first should take one argument—the potential variable name, validate the name, and return Boolean True if it is valid or False if it is not. The second, a main() function, should get input from the user, call the validator function and print “This is a valid variable name” or “This is not a valid variable name.”
##
##*Python’s keyword module can be used to test if a string is a keyword or not.
##
##import keyword
##keyword.iskeyword("elif") # True
##Here is a demo of the program.
##
##Enter your Python variable name: high_temp
##This is a valid variable name.
##Here is another demo.
##
##Enter your Python variable name: highTemp2
##This is a valid variable name.
##And another.
##
##Enter your Python variable name: 2_high_temp
##This is not a valid variable name.
##Part B
##Numerology considers the special relationship between a number and one or more coinciding events. It has been used throughout human history as a way to attach meaning to a name, object, or event using mathematics. Numerology is considered a “pseudoscience” since it has no basis in observable phenomena. Nevertheless, it makes for an interesting programming challenge!
##
##1	2	3	4	5	6	7	8	9
##A	B	C	D	E	F	G	H	I
##J	K	L	M	N	O	P	Q	R
##S	T	U	V	W	X	Y	Z	
##Your program should start by asking the user to type in their name and convert all the letters to uppercase. In the preceding table, each letter of the alphabet has a corresponding number. Using this table, add up the total of all the number values in the person’s name to arrive at a single whole number. If a user enters spaces or extra punctuation, you can ignore these characters. For example, for the name “Guido”:
##
##“G” = 7
##“U” = 3
##“I” = 9
##“D” = 4
##“O” = 6
##
##7 + 3 + 9 + 4 + 6 = 29
##
##Once you have the sum, the number must be reduced so that it is 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, or 22. In numerology, numbers are reduced by adding together their individual digits. For example, 29 reduced is 2 + 9, or, 11. Using this technique, continue to reduce the total until it is a number between 1 and 9, 11, or 22. Hint: You will need to convert the total to a string to iterate over it and convert its digits back to integers before you add them.
##
##Having arrived at the numerology for the name entered, we can now provide the user with “personality associations” for their particular number. Print out the corresponding text based on the following table.
##
##Number	Personality Associations
##1	initiating action, pioneering, leading, independent, attaining, individual
##2	cooperation, adaptability, consideration of others, partnering, mediating
##3	expression, verbalization, socialization, the arts, the joy of living
##4	a foundation, order, service, struggle against limits, steady growth
##5	expansiveness, visionary, adventure, the constructive use of freedom
##6	responsibility, protection, nurturing, community, balance, sympathy
##7	analysis, understanding, knowledge, awareness, studious, meditating
##8	practical endeavors, status oriented, power seeking, material goals
##9	humanitarian, giving nature, selflessness, obligations, creative expression
##11	higher spiritual plane, intuitive, illumination, idealist, a dreamer
##22	the Master Builder, large endeavors, powerful force, leadership
##Your final program should work like this.
##
##Enter your name: Guido
##					
##Your personality number is: 11
##
##Your personality associations are:
##higher spiritual plane, intuitive, illumination, idealist, a dreamer
##Part C
##For this program, you will be writing a series of functions that can be used as part of a “secret message encoder.” Here are the functions you will be writing as well as some sample code to use to test your work.
##
##Function to Add Letters
### function:   add_letters
### input:      a word to scramble (String) and a number of letters (integer)
### processing: adds a number of random letters (A-Z; a-z) after each letter 
###             in the supplied word. for example, if word="cat" and num=1 
###             we could generate any of the following:
###             cZaQtR
###             cwaRts
###             cEaett
### 
###             if word="cat" and num=2 we could generate any of the following:
###             cRtaHFtui
###             cnnaNYtjn
###             czAaAitym
###
### output:     returns the newly generated word
##def add_letters(word, num):
##
##	# function code goes here!
##Sample Program
##
### define original word
##original = "Hello!"
##
### loop to demonstrate the function
##for num in range(1, 5):
##
##    # scramble the word using 'num' extra characters
##    scrambled = add_letters(original, num)
##
##    # output
##    print("Adding", num, "random characters to", original, ". . .", scrambled)
##Sample Output
##
##Adding 1 random characters to Hello! . . . HdeulHlHom!t
##Adding 2 random characters to Hello! . . . HTLedklFNljioMH!bi
##Adding 3 random characters to Hello! . . . HHHZeZrflqSflzOiosNU!jBk
##Adding 4 random characters to Hello! . . . HFtRKeivFllRNlUlGTaooYwoH!JpXL
##Hint: You will need to use a loop to generate the required number of random characters and you will (obviously) need to use some random number functions as well. Think about the algorithm before you start coding! Draw out the steps you think you need to take on a piece of paper. For example: “Start with the first character in the source word. Then generate ‘num’ new random characters and concatenate these characters. Then move onto the next character in the source word and repeat the process.”
##
##Function to Remove Letters
##Once you have written the add_letters function you should begin to work on the next function (remove_letters) which will perform the reverse operation.
##
### function:   remove_letters
### input:      a word to unscramble (String) and the number of characters to remove (integer)
### processing: the function starts at the first position in the supplied word and keeps it.
###             it then removes "num" characters from the word. the process is repeated again
###             if the word contains additional characters - the next character is kept
###             and "num" more characters are removed.  For example, if word="cZaYtU" and
###             num=1 the function will generate the following:
###        
###             cat (keeping character 0, removing character 1, keeping character 2, removing
###                  character 3, keeping character 4, removing character 5)
###
### output:     returns the newly unscrambed word
##def remove_letters(word, num):
##
##	# function code goes here!
##Sample Program
##
##word1 = "HdeulHlHom!t"
##word2 = "HTLedklFNljioMH!bi"
##word3 = "HHHZeZrflqSflzOiosNU!jBk"
##word4 = "HFtRKeivFllRNlUlGTaooYwoH!JpXL"
##
##unscrambled1 = remove_letters(word1, 1)
##print("Removing 1 characer from", word1, ". . .", unscrambled1)
##
##unscrambled2 = remove_letters(word2, 2)
##print("Removing 2 characers from", word2, ". . .", unscrambled2)
##
##unscrambled3 = remove_letters(word3, 3)
##print("Removing 3 characers from", word3, ". . .", unscrambled3)
##
##unscrambled4 = remove_letters(word4, 4)
##print("Removing 4 characers from", word4, ". . .", unscrambled4)
##Sample Output
##
##Removing 1 characer from HdeulHlHom!t . . . Hello!
##Removing 2 characers from HTLedklFNljioMH!bi . . . Hello!
##Removing 3 characers from HHHZeZrflqSflzOiosNU!jBk . . . Hello!
##Removing 4 characers from HFtRKeivFllRNlUlGTaooYwoH!JpXL . . . Hello!
##Hint: String slicing may make your life a lot easier when writing this function!
##
##Function to Shift Characters
##Next, write a function called “shift_characters” that shifts the characters in a word up or down based on their ASCII table position—here’s the IPO (input, processing, output) notation and a sample program:
##
### function:   shift_characters
### input:      a word (String) and a number of characters to shift (integer)
### processing: shifts each character in the supplied word to another position in the ASCII
###             table. the new position is dictated by the supplied integer.  for example,
###             if word = "apple" and num=1 the newly generated word would be:
###
###             bqqmf
###
###             because we added +1 to each character. if we were to call the function with
###             word = "bqqmf" and num=-1 the newly generated word would be:
###           
###             apple
###
###             because we added -1 to each character, which shifted each character down by
###             one position on the ASCII table.
###
### output:     returns the newly generated word
##def shift_characters(word, num):
##	
##	# function code goes here!
##Sample Program
##
##word1 = "apple"
##
##newword1 = shift_characters(word1, 1)
##print(word1, "shifted by +1 is", newword1)
##
##unscrambled1 = shift_characters(newword1, -1)
##print(newword1, "shifted by -1 is", unscrambled1)
##
##
##word2 = "Pears are yummy!"
##
##newword2 = shift_characters(word2, 2)
##print(word2, "shifted by +2 is", newword2)
##
##unscrambled2 = shift_characters(newword2, -2)
##print(newword2, "shifted by -2 is", unscrambled2)
##Sample Output
##
##apple shifted by +1 is bqqmf
##bqqmf shifted by -1 is apple
##Pears are yummy! shifted by +2 is Rgctu"ctg"{woo{#
##Rgctu"ctg"{woo{# shifted by -2 is Pears are yummy!
##Hint: use the ord() and chr() functions!
##
##Encode/Decode
##Finally, you are going to write an “encoder/decoder” program that makes use of your three cryptographic functions. Begin by writing a program that continually asks the user to enter in an option—the user can either (e)ncode a word, (d)ecode a word or (q)uit the program.
##
##If the user chooses to encode a word you should do the following:
##
##Ask the user for a positive number between 1 and 5. Reprompt them if necessary.
##Next, ask them to enter in a phrase that they want to encode.
##Finally, apply the following algorithm to their word:
##Add ‘num’ random characters in between each letter of their word (using your add_letters) function
##Shift the word ‘num’ characters (using your shift_characters function)
##If the user chooses to decode a word you should do the following:
##
##Ask the user for a positive number between 1 and 5. Re-prompt them if necessary.
##Next, ask them to enter in a phrase that they want to encode.
##Finally, apply the following algorithm to their word:
##Subtract “num” random characters in between each letter of their word (using your remove_letters) function
##Shift the word DOWN by “num” characters (using your shift_characters function)
##Here’s a sample running of the program:
##
##(e)ncode, (d)ecode or (q)uit: e
##Enter a number between 1 and 5: 1
##Enter a phrase to encode: apple
##Your encoded word is: boqDqfmsfz
##
##(e)ncode, (d)ecode or (q)uit: d
##Enter a number between 1 and 5: 1
##Enter a phrase to decode: boqDqfmsfz
##Your decoded word is: apple
##
##(e)ncode, (d)ecode or (q)uit: e
##Enter a number between 1 and 5: 2
##Enter a phrase to encode: Hello, World!! :)
##Your encoded word is: JHmgn{nNYnukqFR.Fq"vEY\OqYFt\[n{lf|Y#mJ#kr"UT<cE+og
##
##(e)ncode, (d)ecode or (q)uit: d
##Enter a number between 1 and 5: 2
##Enter a phrase to decode: JHmgn{nNYnukqFR.Fq"vEY\OqYFt\[n{lf|Y#mJ#kr"UT<cE+og
##Your decoded word is: Hello, World!! :)
##
##(e)ncode, (d)ecode or (q)uit: q
##
#######################################
##
##Lists Instructions
##
##Part A
##Eratosthenes of Cyrene lived approximately 275–195 BC. He was the first to accurately estimate the diameter of the earth. For several decades he served as the director and chief librarian of the famous library in Alexandria. He was highly regarded in the ancient world, but unfortunately only fragments of his writing have survived.
##
##The algorithm described for this assignment is known as the “Sieve of Eratosthenes”. The algorithm is designed to find prime numbers within a given range. You are required to use the Sieve of Eratosthenes algorithm for this assignment. No other algorithm for finding prime numbers will be accepted, although there are plenty of others available.
##
##Getting Started
##Begin by inputting a range of numbers to test. Our goal is to examine these numbers and determine which of the numbers in this range are prime. Your lowest number will be 0 and your highest number will be n.
##
##Create a list of n + 1 values where n is the highest number you want to test. Populate each element in this list with the string, “P” for prime. We will start by assuming all numbers in the given range are prime. For example, if you were testing all numbers between 0 and 10, your list would look like this (the top row represents index positions).
##
##0	1	2	3	4	5	6	7	8	9	10
##P	P	P	P	P	P	P	P	P	P	P
##Your goal is to set all non-prime numbers in the list to “N” (for non-prime). You can do that by using the following algorithm. Start by setting the first two values (index positions 0 and 1) to “N”. This lets us record that 0 and 1 are not prime numbers. After this step your list should look like the following.
##
##0	1	2	3	4	5	6	7	8	9	10
##N	N	P	P	P	P	P	P	P	P	P
##Now, move on to the item in position #2 of the list. This item is currently set to “P”, meaning that the number is prime. We now need to mark all future items that are evenly divisible by two as “N”, not prime. You can do this by reading through the entire list starting at 4 (the first multiple of 2), 2 at a time, so that every element that is read contains an index which is a multiple of 2, and store an “N” for that element. This will result in a list in which all of the items whose index is a multiple of 2 will have a value of “N”. After this step your list should look as follows.
##
##0	1	2	3	4	5	6	7	8	9	10
##N	N	P	P	N	P	N	P	N	P	N
##Now, perform the exact same process for the element with an index of 3—there is currently a “P” in postion #3, so we are going to mark all multiples of 3 (starting with 6) with a value of “N”. If your program finds an element which is already “N”, there is nothing further to do for the item (i.e. position 6 will already be marked with an “N” at this point—we can simply skip this element and move on to the next one in the sequence, 9, and mark it with an “N”).
##
##You can perform the exact same process on the item with an index of 4—however, since 4 is already set to “N”, there is no need to check its multiples and your program could just move on to the next item, which has an index of 5.
##
##Processing and Output
##Here is the pattern as you move from one item in the list to the next: If that item has a value of “P”, perform the process. If it is already “N”, skip the process. Try to understand why you should skip this process when the element you are considering is already “N”.
##
##Now, repeat this process over and over. When you have finished, you will find that there are array items which still have a value of “P”. Those items’ index numbers are the prime numbers which you are seeking. Your program should print out all of the prime numbers which you have found in neatly aligned columns, with up to 10 prime numbers on every row as in the following example. This can be done by iterating over the list and checking the value of each item—if there is a “P” in this position, print it out as a prime number; if there is an “N” in this position you can skip it since it is not prime.
##
##Enter a number range: 250
##
##All prime numbers from 0 to 250
##
##     2     3     5     7    11    13    17    19    23    29
##    31    37    41    43    47    53    59    61    67    71
##    73    79    83    89    97   101   103   107   109   113
##   127   131   137   139   149   151   157   163   167   173
##   179   181   191   193   197   199   211   223   227   229
##   233   239   241
##On Efficiency
##Efficiency is important for this program. You do not need to perform the process described above on all items of the list for two different reasons.
##
##If an item in your list has already been set to “N”, what does this tell you about the multiples of that item’s index?
##Certain numbers don’t need to be tested. 800, for example, cannot have any multiples that are less than or equal to 1000. Generalize this idea to make your program even more efficient.
##Part B
##The programs you will be writing for Part B build on one another. You will want to attempt these parts in order but you will submit your work in one file at the end.
##
##Imagine that you are helping to build a store management system for your own restaurant. Given the following lists, write a program that asks the user for a product name. Next, find out if the restaurant sells that item and report the status to the user. Allow the user to continually inquire about product names until they elect to quit the program.
##
##Here are some lists to get you started. Go ahead and change the kind of food for your restaurant!
##
### product lists
##product_names = ["hamburger", "cheeseburger", "small fries"]
##product_costs = [0.99, 1.29, 1.49]
##And here’s a sample running of your program:
##
##(s)earch for product or (q)uit: s
##Enter a product name: hamburger
##We sell "hamburger" at 0.99 per unit
##
##(s)earch for product or (q)uit: s
##Enter a product name: salad
##Sorry, we don't sell "salad"
##
##(s)earch for product or (q)uit: Python
##Invalid option, try again
##
##(s)earch for product or (q)uit: q
##See you soon!
##Inventory
##Next, extend your program so that it keeps track of how many products the store currently has to sell. Default the store to have 10 hamburgers, 5 cheeseburgers, and 20 small fries. Hint: you might want to create a new list to store this data! Once you have this information in place you should modify your program to do the following.
##
##Update the search feature to include a report of how many products the store currently has.
##Add a new feature that lists all products, their prices, and the amount the restaurant has available to sell.
##Here’s a sample running of your program:
##
##(s)earch, (l)ist or (q)uit: s
##Enter a product name: hamburger
##We sell "hamburger" at 0.99 per unit
##We currently have 10 in stock
##
##(s)earch, (l)ist or (q)uit: l
##Product         Price  Quantity
##hamburger       0.99   10    
##cheeseburger    1.29   5     
##small fries     1.49   20    
##
##(s)earch, (l)ist or (q)uit: s
##Enter a product name: pikachu
##Sorry, we don't sell "pikachu"
##
##(s)earch, (l)ist or (q)uit: q
##See you soon!
##Adding Products
##Next, add in an “add” feature that lets users add a new product to the store. When you add a product you will need to ask the user for the name of the product, the cost of the product and how many items the store has available to sell. Validate this data—you cannot add a product that already exists and both the price and inventory amount must be positive. Here’s a sample running of the program:
##
##(s)earch, (l)ist, (a)dd or (q)uit: l
##Product                   Price  Quantity
##hamburger                 0.99   10    
##cheeseburger              1.29   5     
##small fries               1.49   20    
##
##(s)earch, (l)ist, (a)dd or (q)uit: a
##Enter a new product name: cheeseburger
##Sorry, we already sell that product. Try again.
##Enter a new product name: dbl cheeseburger
##Enter a product cost: 0
##Invalid cost. Try again.
##Enter a product cost: 1.49
##How many of these products do we have? -5
##Invalid quantity. Try again.
##How many of these products do we have? 100
##Product added!
##
##(s)earch, (l)ist, (a)dd or (q)uit: l
##Product                   Price  Quantity
##hamburger                 0.99   10    
##cheeseburger              1.29   5     
##small fries               1.49   20    
##dbl cheeseburger          1.49   100   
##
##(s)earch, (l)ist, (a)dd or (q)uit: s
##Enter a product name: dbl cheeseburger
##We sell "dbl cheeseburger" at 1.49 per unit
##We currently have 100 in stock
##
##(s)earch, (l)ist, (a)dd or (q)uit: q
##See you soon!
##Removing Products
##Next, add in a “remove” feature that lets users remove products from the database. Here’s a sample running of the program:
##
##(s)earch, (l)ist, (a)dd, (r)emove or (q)uit: l
##Product                   Price  Quantity
##hamburger                 0.99   10    
##cheeseburger              1.29   5     
##small fries               1.49   20    
##
##(s)earch, (l)ist, (a)dd, (r)emove or (q)uit: r
##Enter a product name: pikachu
##Product doesn't exist. Can't remove.
##
##(s)earch, (l)ist, (a)dd, (r)emove or (q)uit: r
##Enter a product name: small fries
##Product removed!
##
##(s)earch, (l)ist, (a)dd, (r)emove or (q)uit: l
##Product                   Price  Quantity
##hamburger                 0.99   10    
##cheeseburger              1.29   5     
##
##(s)earch, (l)ist, (a)dd, (r)emove or (q)uit: r
##Enter a product name: hamburger
##Product removed!
##
##(s)earch, (l)ist, (a)dd, (r)emove or (q)uit: l
##Product                   Price  Quantity
##cheeseburger              1.29   5     
##
##(s)earch, (l)ist, (a)dd, (r)emove or (q)uit: q
##See you soon!
##Modifying Products
##Add in the ability to modify a product. Users should be able to modify the name, cost or quantity of a product. Note that you will need to perform data validation as needed. Here’s a sample running of your program:
##
##(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate or (q)uit: l
##Product                   Price  Quantity
##hamburger                 0.99   10    
##cheeseburger              1.29   5     
##small fries               1.49   20    
##
##(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate or (q)uit: u
##Enter a product name: burger
##Product doesn't exist. Can't update.
##
##(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate or (q)uit: u
##Enter a product name: hamburger
##What would you like to update?
##(n)ame, (c)ost or (q)uantity: n
##Enter a new name: cheeseburger
##Duplicate name!
##Enter a new name: hamburger royale
##Product name has been updated
##
##(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate or (q)uit: l
##Product                   Price  Quantity
##hamburger royale          0.99   10    
##cheeseburger              1.29   5     
##small fries               1.49   20    
##
##(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate or (q)uit: u
##Enter a product name: cheeseburger
##What would you like to update?
##(n)ame, (c)ost or (q)uantity: c
##Enter a new cost: 0
##Invalid cost!
##Enter a new cost: 9.50
##Product cost has been updated
##
##(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate or (q)uit: l
##Product                   Price  Quantity
##hamburger royale          0.99   10    
##cheeseburger              9.50   5     
##small fries               1.49   20    
##
##(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate or (q)uit: u
##Enter a product name: small fries
##What would you like to update?
##(n)ame, (c)ost or (q)uantity: q
##Enter a new quantity: -500
##Invalid quantity!
##Enter a new quantity: 30
##Product quantity has been updated
##
##(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate or (q)uit: l
##Product                   Price  Quantity
##hamburger royale          0.99   10    
##cheeseburger              9.50   5     
##small fries               1.49   30    
##
##(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate or (q)uit: u
##Enter a product name: hamburger royale
##What would you like to update?
##(n)ame, (c)ost or (q)uantity: nothing
##Invalid option
##
##(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate or (q)uit: q
##See you soon!
##Product Reporting
##Finally, add in a reporting feature to your program that finds the highest priced product, the lowest priced product, and the total value of all inventory in the store (product cost * product quantity). Here’s a sample running of your program:
##
##(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: l
##Product                   Price  Quantity
##hamburger                 0.99   10    
##cheeseburger              1.29   5     
##small fries               1.49   20    
##
##(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: e
##Most expensive product:      1.49 (small fries)
##Least expensive product:     0.99 (hamburger)
##Total value of all products: 46.15
##
##(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: q
##See you soon!
##
##################################
##
##File Input and Output Instructions
##You just finished administering the final exam for all of the students in the “Introduction to Space and Time” class this semester. The exam was a 25 question multiple choice exam and it is your job to grade the exams. You have all of the scores stored in a series of text files.
##
##To begin, download the data files and store them in a folder on your computer. Then create a new Python program inside of this folder called “lastname_firstname_8.py.” Make sure your source code file is inside of the same folder as the data files you just downloaded.
##
##Next, write a program that lets the user type in the name of a file. Attempt to open the supplied file for read access. If the file exists you can print out a confirmation message. If the file doesn’t exist you should tell the user that the file cannot be found and prompt them again.
##
##Use a try/except block to do this (don’t just use a series of “if” statements—we want this program to be as “generic” as possible). You will not get credit for this part of the program if you write something like the following to identify valid data files:
##
##filename = input("Enter a filename: ")
##
##if filename == "class1":
##	# open class1.txt
##elif filename == "class2":
##	# open class2.txt
##else:
##	print ("Sorry, I can't find this filename")
##Here’s a sample running of the program:
##
##Enter a class file to grade (i.e. class1 for class1.txt): foobar
##File cannot be found.
##
##Enter a class file to grade (i.e. class1 for class1.txt): class1
##Successfully opened class1.txt
##Part 2
##Next, you will need to analyze the data contained within the file you just opened to ensure that it is in the correct format. Each data file contains a series of student responses in the following format:
##
##N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D
##or
##
##N12345678,B,,D,,C,B,,A,C,C,,B,A,B,A,,,,A,C,A,A,B,D,
##The first value is the student’s ID number. The following 25 letters are the student responses to the exam. All values are separated by commas. If there is no letter following a comma, this means the student skipped answering the question.
##
##Note that some lines of data may be corrupted! For example, this line of data does not have enough answers:
##
##N12345678,B,A,D,D,C,B
##And this line of data has too many answers:
##
##N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D,A,B,C,D,E
##Your task for this part of the program is to do the following:
##
##Report the total number of lines of data stored in the file.
##Analyze each line and make sure that it is “valid.”
##A valid line contains a comma-separated list of 26 values
##The N number for a student is the first item on the line. It should begin with the character “N” and be followed by 8 numeric characters.
##If a line of data is not valid you should report it to the user by printing out an error message. You should also count the total number of valid lines of data in the file.
##Hints: Use the split method to split apart the data from the file. You may need to use this method a few times along with a loop or two. Think about the order in which you need to split your items. For example, your file is organized so that one student’s record occupies an entire line in the file. Splitting first on the line break will isolate each student’s data. Then you will need to further split each item based on the separator character to pull out the responses for each student.
##
##Here is a sample running of your program for the first two data files. A complete listing of the expected output for all data files can be found in the downloadable package for this assignment.
##
##Enter a class to grade (i.e. class1 for class1.txt): class1
##Successfully opened class1.txt
##
##**** ANALYZING ****
##
##No errors found!
##
##**** REPORT ****
##
##Total valid lines of data: 20
##Total invalid lines of data: 0
##Enter a class to grade (i.e. class1 for class1.txt): class2
##Successfully opened class2.txt
##
##**** ANALYZING ****
##
##Invalid line of data: does not contain exactly 26 values:
##N00000023,,A,D,D,C,B,D,A,C,C,,C,,B,A,C,B,D,A,C,A,A
##
##Invalid line of data: N# is invalid
##N0000002,B,A,D,D,C,B,D,A,C,D,D,D,A,,A,C,D,,A,C,A,A,B,D,D
##
##Invalid line of data: N# is invalid
##NA0000027,B,A,D,D,,B,,A,C,B,D,B,A,,A,C,B,D,A,,A,A,B,D,D
##
##Invalid line of data: does not contain exactly 26 values:
##N00000035,B,A,D,D,B,B,,A,C,,D,B,A,B,A,A,B,D,A,C,A,C,B,D,D,A,A
##
##
##**** REPORT ****
##
##Total valid lines of data: 21
##Total invalid lines of data: 4
##Part 3
##Next, you are going to write code to grade the exams for a given section. The exam was a 25-question, multiple-choice exam. Here is a string that represents the answer key:
##
##answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
##Your program should use this key to compute a score for each valid line of data. Scores can be computed as follows:
##
##+4 points for every right answer
##0 points for every skipped answer
##-1 point for every incorrect answer
##You will also want to compute the following statistics for the entire class:
##
##The average score
##The highest score
##The lowest score
##The range of scores (the highest minus the lowest)
##The median value (Sort the grades in ascending order. If the # of students is odd you can take the middle of all the grades (i.e. [0, 50, 100]—the median is 50). If the # of students is even you can compute the mean by averaging the middle two values (i.e. [0, 50, 60, 100]—the median is 55).
##Hint: Once you’ve scored the students you should use a list to store individual student scores; you can then compute statistics after you’ve examined every student in the file.
##
##Here is a sample running of your program for the first two data files. A complete listing of the expected output for all data files can be found in the downloadable package for this assignment.
##
##Enter a class to grade (i.e. class1 for class1.txt): class1
##Successfully opened class1.txt
##
##**** ANALYZING ****
##
##No errors found!
##
##**** REPORT ****
##
##Total valid lines of data: 20
##Total invalid lines of data: 0
##
##Mean (average) score: 75.60
##Highest score: 91
##Lowest score: 59
##Range of scores: 32
##Median score: 73.0
##Enter a class to grade (i.e. class1 for class1.txt): class2
##Successfully opened class2.txt
##
##**** ANALYZING ****
##
##Invalid line of data: does not contain exactly 26 values:
##N00000023,,A,D,D,C,B,D,A,C,C,,C,,B,A,C,B,D,A,C,A,A
##
##Invalid line of data: N# is invalid
##N0000002,B,A,D,D,C,B,D,A,C,D,D,D,A,,A,C,D,,A,C,A,A,B,D,D
##
##Invalid line of data: N# is invalid
##NA0000027,B,A,D,D,,B,,A,C,B,D,B,A,,A,C,B,D,A,,A,A,B,D,D
##
##Invalid line of data: does not contain exactly 26 values:
##N00000035,B,A,D,D,B,B,,A,C,,D,B,A,B,A,A,B,D,A,C,A,C,B,D,D,A,A
##
##
##**** REPORT ****
##
##Total valid lines of data: 21
##Total invalid lines of data: 4
##
##Mean (average) score: 78.00
##Highest score: 100
##Lowest score: 66
##Range of scores: 34
##Median score: 76
##Part 4
##Finally, have your program generate a “results” file that contains the detailed results for each student in your class. Each line of this file should contain the student’s ID number, a comma, and then their grade. You should name this file based on the original filename supplied—for example, if the user wants to analyze “class1.txt” you should store the results in a file named “class1_grades.txt”.
##
##Here is a sample running of your program for the first two data files. A complete listing of the expected output for all data files can be found in the downloadable package for this assignment.
##
### this is what class1_grades.txt should look like
##  				
##N00000001,59
##N00000002,70
##N00000003,84
##N00000004,73
##N00000005,83
##N00000006,66
##N00000007,88
##N00000008,67
##N00000009,86
##N00000010,73
##N00000011,86
##N00000012,73
##N00000013,73
##N00000014,78
##N00000015,72
##N00000016,91
##N00000017,66
##N00000018,78
##N00000019,78
##N00000020,68
### this is what class2_grades.txt should look like
##  
##N00000021,68
##N00000022,76
##N00000024,73
##N00000026,72
##N00000028,73
##N00000029,87
##N00000030,82
##N00000031,76
##N00000032,87
##N00000033,77
##N00000034,69
##N00000036,77
##N00000037,75
##N00000038,73
##N00000039,66
##N00000040,73
##N00000041,91
##N00000042,100
##N00000043,86
##N00000044,90
##N00000045,67
##
##
############################################
##
##
##Dictionaries Instructions
##
##Part 1
##The National Weather Service provides XML feeds of current weather conditions. This page allows users to access data from about 1,800 locations across the United States and US Territories. For example, https://w1.weather.gov/xml/current_obs/KJRB.xml gives the current weather in XML format as observed in Lower Manhattan.
##
##Using Python’s urllib.request module, write a program that can access the weather data of at least four US cities available from the National Weather Service. It’s up to you which locations you use. Prompt the user again if they enter a city that is not part of your program. After you access the city’s data, convert it to a string for further processing.
##
##Your Weather Report
##
##Current observations are available for:
##- Chicago
##- Houston
##- Los Angeles
##- New York
##
##Enter the city you would like a weather report for: San Diego
##No data available. Please try another city: Los Angeles
##Accessing weather data . . . 
##
##The current weather has been accessed for Los Angeles
##Part 2
##The format of this weather data allows you to find specific information by the XML tag it is enclosed by. For example, the XML for wind direction looks like this: <wind_dir>North</wind_dir>. Regardless of the current reading, you can be confident it will always appear between <wind_dir> and </wind_dir>. View the web page source code of your city’s page to see the full XML structure.
##
##In Chrome: View > Developer > View Source
##In Firefox: Tools > Web Developer > Page Source
##In Safari: Preferences > Advanced > Show Develop menu in menu bar; Develop > Show Page Source
##Once you have read all the page data and converted it to a string, your task is to parse this data and extract from it the following six pieces of information.
##
##The location of the weather reading
##The current weather reading
##The current temperature reading (in degrees F)
##The current relative humidity (in %)
##The current wind conditions
##The date and time of the weather observation
##Each piece of information you extract from the XML code should be added to a Python dictionary of current weather data for the cities you choose to work with. Accordingly, the keys of each dictionary will include “location”, “weather”, “temperature”, “humidity”, “wind”, and “observation”; the value for each key will be the data you parsed from the XML document.
##
##Part 3
##Now that you have this information stored in a Python dictionary, prompt the user for what information they would like to receive. If they choose “temperature”, print the current temperature to the screen; if they choose “weather”, print out the general weather reading. Give feedback and prompt the user again if they ask for data that is not part of your program.
##
##Information available:
##- location
##- weather
##- temperature
##- humidity
##- wind
##- observation
##
##What weather information would you like? temperature
##The temperature in Los Angeles is 59.0 degrees F
##
##What weather information would you like? Or, to end, enter "done". humidity
##The humidity in Los Angeles is 87%
##
##What weather information would you like? Or, to end, enter "done". pressure
##That data is not available.
##
##What weather information would you like? Or, to end, enter "done". wind
##The wind in Los Angeles is West at 6.9 MPH (6 KT)
##
##What weather information would you like? Or, to end, enter "done". done
##Part 4
##Finally, give users the option to print the full weather report to an external text file, saved to the user’s computer. Iterate over every key and value in the dictionary and write these to the text file. Here is an example running of the full program.
##
##Your Weather Report
##
##Current observations are available for:
##- Chicago
##- Houston
##- Los Angeles
##- New York
##
##Enter the city you would like a weather report for: San Diego
##No data available. Please try another city: Los Angeles
##Accessing weather data . . . 
##
##The current weather has been accessed for Los Angeles
##
##Information available:
##- location
##- weather
##- temperature
##- humidity
##- wind
##- observation
##
##What weather information would you like? temperature
##The temperature in Los Angeles is 59.0 degrees F
##
##What weather information would you like? Or, to end, enter "done". humidity
##The humidity in Los Angeles is 87%
##
##What weather information would you like? Or, to end, enter "done". pressure
##That data is not available.
##
##What weather information would you like? Or, to end, enter "done". wind
##The wind in Los Angeles is West at 6.9 MPH (6 KT)
##
##What weather information would you like? Or, to end, enter "done". done
##
##Would you like to export the full weather report? (yes/no) yes
##The full weather report has been exported.
##Here is an example of what the exported weather report should look like.
##
##Part 5
##Write a new version of your program that generates a data visualization instead of an external text file. Within a separate function, create a Turtle drawing that uses current temperature, wind, and/or humidity information to affect the drawing in some way. For example, temperature could be used to change the color of your drawing and wind direction could be visualized with line or shape movement. You are welcome to creatively interpret how the drawing visualizes the weather data you use; drawings should be uniquely yours and demonstrate a thoughtful interpretation of information.
##
##
##
##
##
##                            
