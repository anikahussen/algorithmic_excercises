
def weather_visualization():

    import urllib.request
    import turtle
    import random

    available_cities = {
        "New York City": 'https://w1.weather.gov/xml/current_obs/KJRB.xml',
        "Los Angeles": 'https://w1.weather.gov/xml/current_obs/display.php?stid=KLAX',
        "Boston": 'https://w1.weather.gov/xml/current_obs/display.php?stid=KBOS',
        "Chicago": 'https://w1.weather.gov/xml/current_obs/display.php?stid=KDPA'}


    print("Your Weather Report")
    print()
    print("Current observations are available for: ")
    print("- Chicago")
    print("- Boston")
    print("- Los Angeles")
    print("- New York City")
    print()



    chosen_city = input("Enter the city you would like to see the weather visualization of: ").title().strip()

    while not chosen_city in available_cities.keys():
        chosen_city = input("No data available. Please try another city: ")


    if chosen_city in available_cities:
        open_file = urllib.request.urlopen(available_cities[chosen_city])
        reading_file = open_file.read() # read the page as bytes
        source_code = str(reading_file) # convert to string
        open_file.close()




    print ("Accessing weather data/visualization . . .")
    print()
    print("The current weather visualization has been accessed for", chosen_city)





    #Find weather data


    #Location
    loc_start_index = source_code.find("<location>") + 10
    loc_end_index = source_code.find("</location>")

    location_name = source_code[loc_start_index:loc_end_index]


    #Weather
    weather_start_index = source_code.find("<weather>") + 9
    weather_end_index = source_code.find("</weather>")

    weather_now = source_code[weather_start_index:weather_end_index]


    #Temperature
    temp_start_index = source_code.find("<temp_f>") + 8
    temp_end_index = source_code.find("</temp_f>")

    temp_in_F = source_code[temp_start_index:temp_end_index]
    temperature_in_F = temp_in_F + " degrees F"



    #Humidity
    hum_start_index = source_code.find("<relative_humidity>") + 19
    hum_end_index = source_code.find("</relative_humidity>")

    humidity_og = source_code[hum_start_index:hum_end_index]

    hum_in_perc = humidity_og+"%"




    #Wind

    #---direction

    wind_direction_strt_index = source_code.find("<wind_dir>") + 10
    wind_direction_end_index = source_code.find("</wind_dir>")

    wind_direction = source_code[wind_direction_strt_index:wind_direction_end_index]


    #---speed mph

    wind_mph_strt_index = source_code.find("<wind_mph>") + 10
    wind_mph_end_index = source_code.find("</wind_mph>")

    wind_mph = source_code[wind_mph_strt_index:wind_mph_end_index]

    final_wind_mph = wind_mph+" MPH"

    #---speed knot

    wind_knot_strt_index = source_code.find("<wind_kt>") + 9
    wind_knot_end_index = source_code.find("</wind_kt>")

    wind_knot = source_code[wind_knot_strt_index:wind_knot_end_index]

    final_wind_knot = "("+wind_knot+" KT"+")"

    #wind string
    wind_string_strt_index = source_code.find("<wind_string>") + 13
    wind_string_end_index = source_code.find("</wind_string>")

    wind_string = source_code[wind_string_strt_index:wind_string_end_index]




    #Date and Time
    datetime_start_index = source_code.find("<observation_time>") + 34
    datetime_end_index = source_code.find("</observation_time>")

    date_and_time = source_code[datetime_start_index:datetime_end_index]

    #Observation
    observe_start_index = source_code.find("<observation_time>") + 18
    observe_end_index = source_code.find("</observation_time>")

    observation_time_date = source_code[observe_start_index:observe_end_index]

    #JUST Date and time
    datetime_start_index = source_code.find("<observation_time>") + 34
    datetime_end_index = source_code.find("</observation_time>")

    date_and_time = source_code[datetime_start_index:datetime_end_index]



    #Date
    date_time_list = date_and_time.split(", ")
    date = date_time_list[0]
    #Time
    time = date_time_list[1]


    #Gathered Weather Data List 
    current_weather_data = {
         "location": location_name,
         "weather": weather_now,
         "temperature": temp_in_F, #changed to numeric value
         "humidity": humidity_og, #changed to numeric value
         "wind": wind_string,
         "wind_dir": wind_direction, #separate values for wind
         "wind_speed_mph": wind_mph,#separate values for wind, just numeric
         "observation": observation_time_date

        }



    #Temperature

    if float(current_weather_data["temperature"]) <= 32:
        turtle.fillcolor("blue")
    elif float(current_weather_data["temperature"]) > 32 and float(current_weather_data["temperature"]) < 69:
        turtle.fillcolor("yellow")
    elif float(current_weather_data["temperature"]) >= 70:
        turtle.fillcolor("red")

    turtle.begin_fill()
    #Shape Setup
    radius = 100
    turtle.setup(1000,1000)
    turtle.circle(radius)

    turtle.end_fill()


    #Wind Direction
    if current_weather_data["wind_dir"] == "North":
        turtle.penup()
        turtle.goto(0,radius)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(radius*2)

    elif current_weather_data["wind_dir"] == "South":
        turtle.penup()
        turtle.goto(0,radius)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(radius*2)

    elif current_weather_data["wind_dir"] == "East":
        turtle.penup()
        turtle.goto(0,radius)
        turtle.pendown()
        turtle.forward(radius*2)
    elif current_weather_data["wind_dir"] == "West":
        turtle.penup()
        turtle.goto(0,radius)
        turtle.pendown()
        turtle.left(180)
        turtle.forward(radius*2)
    elif current_weather_data["wind_dir"] == "Northeast":
        turtle.penup()
        turtle.goto(0,radius)
        turtle.pendown()
        turtle.left(45)
        turtle.forward(radius*2)
    elif current_weather_data["wind_dir"] == "Northwest":
        turtle.penup()
        turtle.goto(0,radius)
        turtle.pendown()
        turtle.left(135)
        turtle.forward(radius*2)
    elif current_weather_data["wind_dir"] == "Southeast":
        turtle.penup()
        turtle.goto(0,radius)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(radius*2)
    elif current_weather_data["wind_dir"] == "Southwest":
        turtle.penup()
        turtle.goto(0,radius)
        turtle.pendown()
        turtle.right(135)
        turtle.forward(radius*2)
    elif current_weather_data["wind_dir"] == "Variable":
        turtle.penup()
        turtle.goto(0,radius)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(radius*2)
        
        turtle.fillcolor("green")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()

    #Wind Speed (mph)
    turtle.left(90)
    if float(current_weather_data["wind_speed_mph"]) != 0.0: #when speed is not 0
        visible_speed = (float(current_weather_data["wind_speed_mph"]))*10 #multiplying by 10 to make length more visible
        turtle.forward(visible_speed + 10) #make longer to make for visible

        float_wind_speed = float(current_weather_data["wind_speed_mph"])

        turtle.penup()
        turtle.left(180)
        divide = (visible_speed // (int(float_wind_speed)))
        
        #whole number speed
        for i in range((int(float_wind_speed))):
            turtle.left(90)
            turtle.pendown()
            turtle.forward(10)
            turtle.penup()
            turtle.left(180)
            turtle.forward(10)
            turtle.left(90)
            turtle.forward(divide)

        
        #remaining decimal speed   
        turtle.left(90)
        turtle.pendown()
        remain_decimal = (float(current_weather_data["wind_speed_mph"])) - (int(float_wind_speed))
        
        turtle.forward(remain_decimal*10)   #multiple by 10 to make value visible



    #IF SPEED IS 0.0 NO ADDITIONAL/SPEED MARKS LINE WILL SHOW###
        


    #Reset direction#  
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(0)


    #humidity

    for i in range(int(current_weather_data["humidity"])+1):
        #x coordinates 
        x_range =[]
        for i in range(-400,-(radius)):
            x_range.append(i)
        for i in range(radius+1, 400):
            x_range.append(i)

        #y coordinates
        y_range =[]
        for i in range(-400, 1):
            y_range.append(i)
        for i in range((radius*2)+1, 400):
            y_range.append(i)
        #randomize coordinates
        x_position = random.choice(x_range)
        y_position = random.choice(y_range)

        #color
        if int(current_weather_data["humidity"]) <= 45:
            turtle.fillcolor("lightblue")
        elif int(current_weather_data["humidity"]) > 45 and int(current_weather_data["humidity"]) < 55:
            turtle.fillcolor("white")
        elif int(current_weather_data["humidity"]) >= 55:
            turtle.fillcolor("pink")

        turtle.begin_fill()
        
        turtle.penup()
        turtle.goto(x_position,y_position)
        turtle.pendown()
        #drawing squares
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(5)

        turtle.end_fill()


weather_visualization()
