GREETING = "Hello, "
# Starting a name with a "_" simbol will not add it to import
# Name will not be available after
# from outmodule import *
_GREETING = "Hello, "

class BadName(Exception):
    pass

def greet(name):
    if name[0].isupper():
        return GREETING + name
    else:
        raise BadName(name + " is inappropriate name")

# __all__ allows us to tell what will be imported to other file if we
# type there from ourmodule import *
# So, GREETING variable will NOT be imported
__all__ = ["BadName", "greet"]