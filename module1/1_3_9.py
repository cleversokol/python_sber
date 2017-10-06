# First

# Second
def closest_mod_5(x):
    z = x % 5
    return x if z==0 else x+5-z

# Third
def closest_mod_5(x):
    return x if x%5==0 else x+5-x%5