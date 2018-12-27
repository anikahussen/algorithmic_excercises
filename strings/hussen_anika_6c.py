import random
import string

#---------------------------------ADD LETTERS---------------------------#
def add_letters(word, num):
    '''
    Input:  a word to scramble (String) and a number of letters (integer)
    Processing: adds a number of random letters (A-Z; a-z) after each letter 
    Output: return scrambled word
'''
    scrambled_word = ""
            
    for char in word:
            scrambled_word += char
            generate = 0
            while generate < num:
                    random_num = random.randint(65, 122)
                    if random_num <= 90 or random_num >= 97:
                            letter = chr(random_num)
                            scrambled_word += letter
                            generate += 1
    return scrambled_word

#Test

#word = "Hello!"
#for num in range(1, 5):
        #scrambled_word = add_letters(word, num)
        #print("Adding", num, "random characters to", word, ". . .", scrambled_word)
      

#---------------------------------REMOVE LETTERS---------------------------#
    
def remove_letters (word, num):
    '''
    Input: a word to unscramble (String) and the number of characters to remove (integer)
    Processing: the function starts at the first position in the supplied word and keeps it.
    Output: return unscrambled word
'''
    if num > 0:
        unscrambled_word = word[::num+1]
        return unscrambled_word
    elif num < 0:
        return "Error"
    elif num == 0:
            return word

#Test

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


#---------------------------------SHIFTED LETTERS---------------------------#

def shift_characters(word, num):
    '''
    Input: a word (String) and a number of characters to shift (integer)
    Processing: shifts each character in the supplied word to another position in the ASCII
    Output: return shifted word
    '''
    
    shifted_word = ""
    for char in word:
        shifted_ord = ord(char) + num
        shifted_char = chr(shifted_ord)
        shifted_word += shifted_char
    return shifted_word
                
 
#Test

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
##
##
##                
 
     

#---------------------------------Encoder/Decoder---------------------------#
option = input("(e)ncode a word, (d)ecode or (q)uit: ")
while option != "e" and option != "d" and option != "q":
    print("Invalid input. Please enter e, d, or q")
    option = input("(e)ncode a word, (d)ecode or (q)uit: ")
while option != "q":
    
    if option == "e":
        num = int(input("Enter a number between 1 and 5: "))
        while num < 0:
            print ("Invalid input. Please enter a positive value.")
            num = int(input("Enter a number between 1 and 5: "))
        word = input("Enter a phrase to encode: ")
        encode_step_1 = add_letters(word, num)
        encoded_word = shift_characters(encode_step_1, num)
        print(encoded_word)
        print()
        option = input("(e)ncode a word, (d)ecode or (q)uit: ")
        
    elif option == "d":
        num = int(input("Enter a number between 1 and 5: "))
        while num < 0:
            print ("Invalid input. Please try again.")
            num = int(input("Enter a number between 1 and 5: "))
        word = input("Enter a phrase to decode: ")
        decoded_step_1 = remove_letters(word, num)
        num *= -1
        decoded_word = shift_characters(decoded_step_1, num)
        print(decoded_word)
        print()
        option = input("(e)ncode a word, (d)ecode or (q)uit: ")
