# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

def measure_udacity(string_list):
    udacious_level = 0
    for entry in string_list:
        if entry[0] == 'U':
            udacious_level += 1
    return udacious_level



print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2
