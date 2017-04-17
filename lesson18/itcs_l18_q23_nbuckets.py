# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    counter = 0
    buckets = []
    while counter < nbuckets:
        buckets.append([])
        counter = counter + 1
    return buckets

