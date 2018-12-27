#line drawing module

def horizontal_line(width):
    '''
    Create horizontal line based on width value parameter
    '''
    print ("*" * width)

def vertical_line(shift, height):
    '''
    Create vertical line based on the shift and height value paramaters
    '''
    for line in range(0, height):
        print (" " * ((shift) - 1)+"*")

def two_vertical_lines (width, height):
    '''
    Create two verical line based on width and height parameters
    '''
    for line in range(0, height):
            print ("*" + " " * (width - 2) + "*")
        

#----------------------------------------------------------------------#

#digital numbers module




def number_0 (width):
    ''' prints the number 0 as it would appear on a digital display
            using the supplied width value  '''
    print()
    horizontal_line(width)
    two_vertical_lines (width, 3)
    horizontal_line(width)
    print()


def number_1 (width):
    ''' prints the number 1 as it would appear on a digital display
            using the supplied width value  '''
    print()
    vertical_line(width, 5)
    print()

def number_2 (width):
    ''' prints the number 2 as it would appear on a digital display
            using the supplied width value  '''
    print()
    horizontal_line(width)
    vertical_line(width, 1)
    horizontal_line(width)
    vertical_line(0, 1)
    horizontal_line(width)
    print()
def number_3 (width):
    ''' prints the number 3 as it would appear on a digital display
            using the supplied width value  '''
    print()
    horizontal_line(width)
    vertical_line(width, 1)
    horizontal_line(width)
    vertical_line(width, 1)
    horizontal_line(width)
    print()

def number_4 (width):
    ''' prints the number 4 as it would appear on a digital display
            using the supplied width value  '''
    print()
    two_vertical_lines (width, 2)
    horizontal_line(width)
    vertical_line(width, 2)
    print()
    
def number_5 (width):
    ''' prints the number 5 as it would appear on a digital display
            using the supplied width value  '''
    print()
    horizontal_line(width)
    vertical_line(0, 1)
    horizontal_line(width)
    vertical_line(width, 1)
    horizontal_line(width)
    print()
def number_6 (width):
    ''' prints the number 6 as it would appear on a digital display
            using the supplied width value  '''
    print()
    horizontal_line(width)
    vertical_line(0, 1)
    horizontal_line(width)
    two_vertical_lines (width, 1)
    horizontal_line(width)
    print()
    
def number_7 (width):
    ''' prints the number 7 as it would appear on a digital display
            using the supplied width value  '''
    print()
    horizontal_line(width)
    vertical_line(width, 4)
    print()
def number_8 (width):
    ''' prints the number 8 as it would appear on a digital display
            using the supplied width value  '''
    print()
    horizontal_line(width)
    two_vertical_lines (width, 1)
    horizontal_line(width)
    two_vertical_lines (width, 1)
    horizontal_line(width)
    print()
def number_9 (width):
    ''' prints the number 9 as it would appear on a digital display
            using the supplied width value  '''
    print()
    horizontal_line(width)
    two_vertical_lines (width, 1)
    horizontal_line(width)
    vertical_line(width, 2)
    print()

#----------------------------------------------------------------------#

#operators module


def addition (width):

    ''' prints the addition symbol as it would appear on a digital display
            using the supplied width value  '''
    print()
    vertical_line(int(width)//2 + 1 , 2)
    horizontal_line(width)
    vertical_line(int(width)//2 + 1, 2)
    print()


def subtraction (width):

    ''' prints the subtraction symbol as it would appear on a digital display
            using the supplied width value  '''
    print()
    horizontal_line(width)
    print()

#----------------------------------------------------------------------#

#check answers module

def check_answer(number1,number2,answer,operator):
    '''processing: determines if the supplied expression is correct.'''
    
    expression = True
    if operator == "+":
        a = number1 + number2
        if answer == a:
            expression = True
        elif answer != a:
            expression = False
    elif operator == "-":
       a = number1 - number2
       if answer == a:
           expression = True
       elif answer != a:
           expression = False

    return expression

