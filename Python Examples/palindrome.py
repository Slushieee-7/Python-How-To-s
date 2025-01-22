#here is another example on how to reverse a string or a word in python
text = "A nut for a jar of tuna" [::-1] #we call this method "slicing", 
                                        #wherein this means that the counter would start at the end of the string and end at the start of the string
                                        #-1 indicates that the counter would move a step backward
print("The palindrome of your word is: " + text)

# if we use a function to call that slicer:
def sliceEm(x): # we define the function first 
    return x[::-1] #if called, return x and apply te slicer

newtext = sliceEm("Womp womp")
print("This is your new text: " + newtext)
