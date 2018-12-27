# Ask the user for an initial deposit amount
initial_deposit = float(input("How much would you like to initially invest or deposit to your savings account? (ie. 100) "))

# Ask the user for an interest rate annually
annual_interest_rate = float(input("Now, enter your projected annual interest rate (ex. for 5%, enter 0.05): "))


# Convert annual interest to monthly interest

monthly_interest_rate = annual_interest_rate / 12



# Calculate Ending Balances/Total 

ending_balance1 = initial_deposit + (initial_deposit * monthly_interest_rate)
ending_balance2 = ending_balance1 + (ending_balance1 * monthly_interest_rate)
ending_balance3 = ending_balance2 + (ending_balance2 * monthly_interest_rate)

ending1 = format (ending_balance1, ".2f")
ending2 = format (ending_balance2, ".2f")
ending3 = format (ending_balance3, ".2f")




# Assign Starting Balances 

starting_balance1 = initial_deposit
starting_balance2 = ending_balance1
starting_balance3 = ending_balance2

starting1 = format (starting_balance1, ".2f")
starting2 = format (starting_balance2, ".2f")
starting3 = format (starting_balance3, ".2f")




# Calculate monthly interest

interest_month1 = starting_balance1 * monthly_interest_rate
interest_month2 = starting_balance2 * monthly_interest_rate
interest_month3 = starting_balance3 * monthly_interest_rate

interest1 = format (interest_month1, ".2f")
interest2 = format (interest_month2, ".2f")
interest3 = format (interest_month3, ".2f")


#Assigning month numbers to variables
month1 = "1"
month2 = "2"
month3 = "3"


# Format (padding) for table

column1 = format ("Month", "10s")
column2 = format ("Starting Balance", "30s")
column3 = format ("Interest", "15s")
column4 = format ("Ending Balance", "30s")

mon1 = format(month1, "10s")
mon2 = format(month2, "10s")
mon3 = format(month3, "10s")

strt1 = format (starting1, "30s")
strt2 = format (starting2, "30s")
strt3 = format (starting3, "30s")

intrst1 = format (interest1, "15s")
intrst2 = format (interest2, "15s")
intrst3 = format (interest3, "15s")

end1 = format (ending1, "30s")
end2 = format (ending2, "30s")
end3 = format (ending3, "30s")



print ("Calculating")
print ("...")
print("...")
print ("...")

print (column1, column2, column3, column4)
print (mon1, strt1, intrst1, end1)
print (mon2, strt2, intrst2, end2)
print (mon3, strt3, intrst3, end3)



