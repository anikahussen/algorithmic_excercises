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
        


