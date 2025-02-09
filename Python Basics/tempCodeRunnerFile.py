#using dictionary mapping (which are defining each cases possible)
def letter_a():
    return "A"
def letter_b():
    return "B"
def letter_c():
    return "C"
def letter_d():
    return "D"
def default():
    return "Unknown letter"

def dict(value):
    switcher = {
        1: letter_a,
        2: letter_b,
        3: letter_c,
    }
    # Get the function from switcher dictionary
    return switcher.get(value, default)()
    # Execute the function

print(dict(2)) #outputs the function of letter_b which is "B"