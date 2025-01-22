#how to remove duplicates in an array

oldlist = ["a", "b","c","d","e","e","f","g",]
newlist = list(dict.fromkeys(oldlist)) # the "dict.fromkeys(oldlist)" creates a new dictionary using the data from the "oldlist" array
                                       # the list() makes a list using the the data from the new dictionary
print("Old array: ", oldlist)
print("New array: ", newlist) 