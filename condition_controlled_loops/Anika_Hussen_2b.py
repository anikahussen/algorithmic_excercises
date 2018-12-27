
#ask user for birth month and day in numerical data, so mathematical operation
#can be used 
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input ("Enter your birth day (1-31): "))

#go through each month and separate the dates by thte two zodiacs they have
if birth_month == 1:
    if birth_day <= 20:
        zodiac = "Capricorn"
    else:
        zodiac = "Aquarius"

if birth_month == 2:
    if birth_day <= 19:
        zodiac = "Aquarius"
    else:
        zodiac = "Pisces"

if birth_month == 3:
    if birth_day <= 20:
        zodiac = "Pisces"
    else:
        zodiac ="Aries"

if birth_month == 4:
    if birth_day <= 20:
        zodiac = "Aries"
    else:
        zodiac = "Taurus"

if birth_month == 5:
    if birth_day <= 21:
        zodiac = "Taurus"
    else:
        zodiac = "Gemini"

if birth_month == 6:
    if birth_day <= 21:
        zodiac = "Gemini"
    else:
        zodiac = "Cancer"

if birth_month == 7:
    if birth_day <= 22:
        zodiac = "Cancer"
    else:
        zodiac = "Leo"

if birth_month == 8:
    if birth_day <= 22:
        zodiac = "Leo"
    else:
        zodiac = "Virgo"

if birth_month == 9:
    if birth_day <= 23:
        zodiac = "Virgo"
    else:
        zodiac = "Libra"

if birth_month == 10:
    if birth_day <= 23:
        zodiac = "Libra"
    else:
        zodiac = "Scorpio"

if birth_month == 11:
    if birth_day <= 22:
        zodiac = "Scorpio"
    else:
        zodiac = "Sagittarius"

if birth_month == 12:
    if birth_day <= 21:
        zodiac = "Sagitarrius"
    else:
        zodiac = "Capricorn"

#print the zodiac the program stops at 
print ("You are a", zodiac + ".")
print ( ) #space in between print statements 


#if statements for daily fortune/horoscope for each zodiac    
if zodiac == "Capricorn":
    print ("Keep your eyes on the goal,")
    print ("but do not get carried away with fantasies.")

if zodiac == "Aquarius":
    print ("Take initiative to change your dull routine and pursue something wilder.")


if zodiac == "Pisces":
    print ("You will feel overwhelming stress,")
    print ("but soon you will recieve a suprising and well-deserved reward. ")

if zodiac == "Aries":
    print ("Don't be afraid to keep in contact with the exciting people you will meet.")
    print ("It might just result in long term relationships.")

if zodiac == "Taurus":
    print("You are feeling inclined to stay at home forever.")
    print ("Get out of your comfort zone and join social hobby groups.")

if zodiac == "Gemini":
    print ("Reach out to your family and friends.")
    print ("You might just meet someone or build relationships that you will prize forever.")

if zodiac == "Cancer":
    print ("A life decision will lead to a financial improvement.")

if zodiac == "Leo":
    print ("Take an unexpected turn and go to a gathering, fair or party with your friends.")
    print ("You might learn something crucial about the people around you.")

    
if zodiac == "Virgo":
    print ("Delve into your secret desire to learn about the obscure topics like alchemy or numerology.")

if zodiac == "Libra":
    print ("You are feeling rebellious today and you should get out of your shell")
    print ("and take on a daring activity like skydiving.")
    

if zodiac == "Scorpio":
    print ("Take a breath of fresh air and recharge your mind from all the exhausting work you have had.")

if zodiac == "Sagittarius":
    print ("Take time and reflect on your life.")
    print ("Keep track of failures and successes to be informed for what's to come.")



