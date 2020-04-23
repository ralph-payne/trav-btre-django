# A List is a collection which is ordered and changeable. Allows duplicate members.
# A list is basically an array; it's formatted like an array and has a lot of the array methods

# Create list
numbers = [1,2,3,4,5]

print(type(numbers)) # Prints <class 'list'>
print(numbers) # [1, 2, 3, 4, 5]

# Create list using a constructor. This is a different (less popular way of doing it)
numbers_two = list((6,7,8,9,0))
print(numbers_two) # [6, 7, 8, 9, 0]

# Notice that you can include different types into lists (i.e. the list doesn't all have to be ints or strings
words = ['canonical', 'disingenuous', 'equanimity', 'neoteny', 125]

print(words) # ['canonical', 'disingenuous', 'equanimity', 'neoteny', 125]
print(type(words)) # <class 'list'>

# Print out using square brackets notation
print(words[0]) # canonical

# Get length of list
print(len(words)) # 5

# Append something to the list using append
# Note, In JavaScript you would use push(). In Python, you use append()
words.append('egalitarian')
print(words) # ['canonical', 'disingenuous', 'equanimity', 'neoteny', 125, 'egalitarian']

# Remove from a list
words.remove('equanimity')
print(words) # ['canonical', 'disingenuous', 'neoteny', 125, 'egalitarian']

# Insert into a specific position
words.insert(2, 'heuristics')
# 'heuristics now appears in position 2 of the list
print(words) # ['canonical', 'disingenuous', 'heuristics', 'neoteny', 125, 'egalitarian']

# Remove from a certain position (using pop)
words.pop(3)
# 'neotony' has now been removed
print(words) # ['canonical', 'disingenuous', 'heuristics', 125, 'egalitarian']

# Reverse a list
words.reverse()
print(words) # ['egalitarian', 125, 'heuristics', 'disingenuous', 'canonical']

# Sort the list to order the strings alphabetically
words.remove(125) # You will have to remove the int to make this word
words.sort()
print(words) # ['canonical', 'disingenuous', 'egalitarian', 'heuristics']

# Reverse sort
# This will sort the list the other way
words.sort(reverse=True)
print(words) # ['heuristics', 'egalitarian', 'disingenuous', 'canonical']