import line_drawing

def addition (width):

    ''' prints the addition symbol as it would appear on a digital display
            using the supplied width value  '''
    line_drawing.vertical_line(int(width)//2 + 1 , 2)
    line_drawing.horizontal_line(width)
    line_drawing.vertical_line(int(width)//2 + 1, 2)



def subtraction (width):

    ''' prints the subtraction symbol as it would appear on a digital display
            using the supplied width value  '''
    line_drawing.horizontal_line(width)
