# YOUR CODE HERE
numlist = list(range(2000, 3201))
divlist = []
numstring = ""
for number in numlist:
    # Checking if the number is divisible by 7 and not a multiple of 5 and adding it to divlist
    if((number%7==0) and (number%5!=0)):
        divlist.append(number)
        # Checking if the numstring is empty. If empty, it will take in the 1st number else it will add a comma and add the number
        if (numstring==""):
            numstring = str(number)
        else:
            numstring = numstring + ", {}".format(number)
            
# Printing the list of divisible numbers (divisible by 7 and not a multiple of 5)
print("\nPrinting the list containing numbers divisible by 7 and not a multiple of 5:\n")
print(divlist) 

# Printing the comma separate sequence of numbers (divisible by 7 and not a multiple of 5) 
print("\nPrinting the numbers containing numbers divisible by 7 and not a multiple of 5 as comma separated sequence:\n")
print(numstring) 

