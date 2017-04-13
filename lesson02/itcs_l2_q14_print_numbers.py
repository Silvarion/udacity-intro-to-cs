# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(num):
    if num > 0:
        counter=1
        while counter <= num:
            print counter
            counter = counter + 1
    else:
        print "Please use a positive number"



print_numbers(3)
#>>> 1
#>>> 2
#>>> 3
