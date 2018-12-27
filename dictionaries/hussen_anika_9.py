def weather_reporting_function():

    import urllib.request



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



    chosen_city = input("Enter the city you would like a weather report for: ").title().strip()

    while not chosen_city in available_cities.keys():
        chosen_city = input("No data available. Please try another city: ")


    if chosen_city in available_cities:
        open_file = urllib.request.urlopen(available_cities[chosen_city])
        reading_file = open_file.read() # read the page as bytes
        source_code = str(reading_file) # convert to string
        open_file.close()




    print ("Accessing weather data . . .")
    print()
    print("The current weather has been accessed for", chosen_city)





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
         "temperature": temperature_in_F,
         "humidity": hum_in_perc,
         "wind": wind_string,
         "observation": observation_time_date

        }



    #Asking for specific info

    print("Information available:")
    print()
    print("- location")
    print("- weather")
    print("- temperature")
    print("- humidity")
    print("- wind")
    print("- observation")
    print()

    initial_inquiry = input("What weather information would you like? ")
    while not initial_inquiry in current_weather_data.keys() :
        print("That data is not available.")
        print()
        initial_inquiry = input("What weather information would you like? ")

    if initial_inquiry == "location":
            print("The specific location in", chosen_city, "you are accessing weather data from is", current_weather_data["location"])
            print()
            weather_inquiry = input('What weather information would you like? Or, to end, enter "done". ')
          
            
    elif initial_inquiry == "weather":
        print("The weather in", chosen_city, "is", current_weather_data["weather"])
        print()
        weather_inquiry = input('What weather information would you like? Or, to end, enter "done". ')

        
    elif initial_inquiry == "temperature":
        print("The temperature in", chosen_city, "is", current_weather_data["temperature"])
        print()
        weather_inquiry = input('What weather information would you like? Or, to end, enter "done". ')


    elif initial_inquiry == "humidity":
        print("The humidity in", chosen_city, "is", current_weather_data["humidity"])
        print()
        weather_inquiry = input('What weather information would you like? Or, to end, enter "done". ')

            
    elif initial_inquiry == "wind":
        print("The wind in", chosen_city, "is", current_weather_data["wind"])
        print()
        weather_inquiry = input('What weather information would you like? Or, to end, enter "done". ')

        
    elif initial_inquiry == "observation":
        full_observation_line = current_weather_data["observation"]
        observ_wo_statement = full_observation_line[16:]
        print("The weather in", chosen_city, "was last updated on", observ_wo_statement)
        print()
        weather_inquiry = input('What weather information would you like? Or, to end, enter "done". ')

        
            


    while not weather_inquiry in current_weather_data.keys() and weather_inquiry != "done":
        print("That data is not available.")
        print()
        break

    while weather_inquiry != "done":
        if weather_inquiry == "location":
            print("The specific location in", chosen_city, "you are accessing weather data from is", current_weather_data["location"])
            print()
            weather_inquiry = input('What weather information would you like? Or, to end, enter "done". ')
            
        elif weather_inquiry == "weather":
            print("The weather in", chosen_city, "is", current_weather_data["weather"])
            print()
            weather_inquiry = input('What weather information would you like? Or, to end, enter "done". ')
            
        elif weather_inquiry == "temperature":
            print("The temperature in", chosen_city, "is", current_weather_data["temperature"])
            print()
            weather_inquiry = input('What weather information would you like? Or, to end, enter "done". ')

        elif weather_inquiry == "humidity":
            print("The humidity in", chosen_city, "is", current_weather_data["humidity"])
            print()
            weather_inquiry = input('What weather information would you like? Or, to end, enter "done". ')
            
        elif weather_inquiry == "wind":
            print("The wind in", chosen_city, "is", current_weather_data["wind"])
            print()
            weather_inquiry = input('What weather information would you like? Or, to end, enter "done". ')
            
        elif weather_inquiry == "observation":
            full_observation_line = current_weather_data["observation"]
            observ_wo_statement = full_observation_line[16:]
            print("The weather in", chosen_city, "was last updated on", observ_wo_statement)
            print()
            weather_inquiry = input('What weather information would you like? Or, to end, enter "done". ')

    #reporting request after break when entering done
    print()
    report_request = input("Would you like to export the full weather report? (yes/no) ")
    if report_request == "yes":
        writing_file = open(chosen_city+" Weather Report", 'w')
        writing_file.write("Weather for"+" "+chosen_city+"\n"+"\n")

        for key, value in current_weather_data.items():
            titled_key = key.title()
            writing_file.write(titled_key+":"+" "+ value+"\n")
        writing_file.close()
        print("The full weather report has been exported.")
        
    elif report_request == "no":
        print("Thank you for using the Weather Reporting Program.")



weather_reporting_function()
