# Change the lookup procedure
# to now work with dictionaries.

def lookup(index, keyword):
    try:
        return index[keyword]
    except KeyError:
        return None
    
