import keyword

def potential_variable_name(variable_name):
    '''
    Input: potential variable (string)
    Processing: checks to see if the string input fullfills the Python variable requirements
    Output: return Boolean True for valid variable or False for invalid variable
'''
    

    for character in variable_name:
        if not character.isalnum() and character != "_" :
            return False
        elif character.isalnum() or character == "_":
            if keyword.iskeyword(variable_name):
                return False
            elif not keyword.iskeyword(variable_name):
                if variable_name[0].isdigit():
                    return False
                elif not variable_name[0].isdigit():
                    return True
                    
def main():
    variable_name = input("Enter your Python variable name: ")
    answer = potential_variable_name(variable_name)
    if answer == True:
        print ("This is a valid variable name.")
    elif answer == False:
        print ("This is not a valid variable name.")

main()
    
     
        
    

