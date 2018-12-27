file_size = float(input("Enter a file size in kilobytes (KB): "))


# Conversion 
bytes = file_size * 1024
bits = bytes * 8
megabytes = file_size / 1024
gigabytes = megabytes / 1024

#formatting conversion outputs

formatted_bytes = format (bytes, ",.1f")
formatted_bits = format (bits, ",.1f")
formatted_megabytes = format (megabytes, ",.1f")
formatted_gigabytes = format (gigabytes, ",.1f")

byte_amount = format (formatted_bytes, ">40s")
bit_amount = format (formatted_bits, ">40s")
megabyte_amount = format (formatted_megabytes, ">40s")
gigabyte_amount = format (formatted_gigabytes, ">40s")


#formatting units of measuement

bit_units = format("... in bits", "<20s")
byte_units = format("... in bytes", "<20s")
megabyte_units = format("... in megabytes", "<20s")
gigabyte_units = format("... in gigabyte", "<20s")

#Print out calculations 

print (file_size, "KB is ...")


print (bit_units, bit_amount, "bits")
print (byte_units, byte_amount, "bytes")
print (megabyte_units, megabyte_amount, "MB")
print (gigabyte_units, gigabyte_amount, "GB")

#                                       Error No. 1
#Syntax Error ----------------------------------------------------------------

#The following line would result in a syntax error because I forgot
#to add an additional closing #parenthesis for the float function.
#The float and input function could not occur at the same #time
#without having two pairs of parenthesis.

#file_size = float(input("Enter a file size in kilobytes (KB): ")

#                                       Error No. 2
#Syntax Error ------------------------------------------------------------------

#The following line would result in a syntax because there is no comma
#separating the two arguments: the float I am trying to format
#and the directions on how to format it. 

#formatted_gigabytes = format (gigabytes ",.1f")


#                                      Error No. 3
#Semantic Error ------------------------------------------------------------

#The following line would result in a semantic error. 

#bits = bytes / 8


#When assigning the variable, bits, to its #conversion from bytes to bits,
#I accidently used the #floating division operator instead of the
#multiplication operator. A bit is 8 times a byte, so I
#should have entered bits = bytes * 8.

#This line:

#The line resulted in:
#... in bits                                         256,000.0 bits

#instead of:
#... in bits                                      16,384,000.0 bits


#                                   Error No. 4
#Semantic Error ------------------------------------------------------------

#The following line resulted in a semantic error. 
#print (bit_units, formatted_bits, "bits")


#This is because the argument, formatted_bits,
#is not #the variable that I had formatted to have a right alignment.
#Instead I had put a previous #variable into the print argument. 
#So this line:


#The line resulted in:
#2000.0 KB is ...
#... in bits          16,384,000.0 bits

#instead of:
#20000 KB ...

#... in bits                                         16,384,000.0 bits

#I should have used the variable, bit_amount, which I had formatted this way:

#bit_amount = format (formatted_bits, ">40s")

#                                Error No. 5
#RunTime Error-------------------------------------------------------------

#The following line is a Run Time error because the format function
#does not take more than #two arguments.
#I meant to print, rather than format.
#The program did run but gave me a #Traceback error statement when running. 

#  format (gigabyte_units, gigabyte_amount, "GB")


#                               Error No. 6
#RunTime Error------------------------------------------------------------

#The following line caused a Run Time error because I entered an argument
#“.1s”. It should #have been: “.1f ,not only because
#".1" is meant to format a float to only have 1 decimal point
#place, but also because the variable, bytes, is a float.
#The program did run, but resulted in a 
# valueError statement: Unknown format code 's' for object of type 'float’. 

#   formatted_bytes = format (bytes, ".1s")







