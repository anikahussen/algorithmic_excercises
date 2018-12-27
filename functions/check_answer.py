
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

