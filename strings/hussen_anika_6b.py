
def numerology_fortune():
    numerology_counter = 0
    name = input("Enter your name: ").upper()
    for character in name:
        if character.isalpha(): #ignore spaces and punctuation
            if character == "A" or character == "J" or character == "S":
                numerology_counter += 1
            elif character == "B" or character == "K" or character == "T":
                numerology_counter += 2
            elif character == "C" or character == "L" or character == "U":
                numerology_counter += 3
            elif character == "D" or character == "M" or character == "V":
                numerology_counter += 4
            elif character == "E" or character == "N" or character == "W":
                numerology_counter += 5
            elif character == "F" or character == "O" or character == "X":
                numerology_counter += 6
            if character == "G" or character == "P" or character == "Y":
                numerology_counter += 7
            elif character == "H" or character == "Q" or character == "Z":
                numerology_counter += 8
            elif character == "I" or character == "R":
                numerology_counter += 9


    while numerology_counter > 9 and numerology_counter != 11 and numerology_counter != 22: #setting not numerological value
        str_numerology_counter = str(numerology_counter)
        first_digit = str_numerology_counter[0]
        last_digit = str_numerology_counter[-1]

        numerology_counter = int(first_digit) + int(last_digit)

    personality_number = numerology_counter
        
    print()
    print("Your personality number is:", personality_number)
    print()
        
    if personality_number == 1:
        print("Your personality associations are: ")
        print ("initiating action, pioneering, leading, independent, attaining, individual")
    elif personality_number == 2:
        print("Your personality associations are: ")
        print ("cooperation, adaptability, consideration of others, partnering, mediating")
    elif personality_number == 3:
        print("Your personality associations are: ")
        print ("expression, verbalization, socialization, the arts, the joy of living")
    elif personality_number == 4:
        print("Your personality associations are: ")
        print ("a foundation, order, service, struggle against limits, steady growth")
    elif personality_number == 5:
        print("Your personality associations are: ")
        print ("expansiveness, visionary, adventure, the constructive use of freedom")
    elif personality_number == 6:
        print("Your personality associations are: ")
        print("responsibility, protection, nurturing, community, balance, sympathy")
    elif personality_number == 7:
        print("Your personality associations are: ")
        print ("analysis, understanding, knowledge, awareness, studious, meditating")
    elif personality_number == 8:
        print("Your personality associations are: ")
        print ("practical endeavors, status oriented, power seeking, material goals")
    elif personality_number == 9:
        print("Your personality associations are: ")
        print ("humanitarian, giving nature, selflessness, obligations, creative expression")
    elif personality_number == 11:
        print("Your personality associations are: ")
        print ("higher spiritual plane, intuitive, illumination, idealist, a dreamer")
    elif personality_number == 22:
        print("Your personality associations are: ")
        print ("the Master Builder, large endeavors, powerful force, leadership")


numerology_fortune()
