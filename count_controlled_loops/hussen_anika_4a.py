ASCII = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
text = input("Enter a text to analyze: ")



ascii_counter = 0
total_counter = 0

for character in text:
        total_counter += 1
        for i in ASCII:
            if i == character:
                ascii_counter += 1 
        

no_ascii_counter = total_counter - ascii_counter


print()
print ("Total number of characters: ", total_counter)
print ("Total number of ASCII characters: ", ascii_counter)
print("Total number of non-ASCII characters: ", no_ascii_counter)    
