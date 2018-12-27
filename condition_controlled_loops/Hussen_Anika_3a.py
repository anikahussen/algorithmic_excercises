r = 1

while r < 10:
    c = 1
    while c < 10: 
        x = r * c
        formatted_x = format(str(x), ">4s")
        print(formatted_x, end=' ') #numbers stay on the same line
        c += 1 #move back out to the outer while loop before the value hits 10 | keep adding 1 while less than 10
    print()
    r += 1 #keep adding 1 while less than 10

