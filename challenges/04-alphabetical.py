# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize(string):
    sorted_string = sorted(string)
    string = "".join(sorted_string)
    print(string)

alphabetize("dca")
