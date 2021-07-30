# author: Samaiya Howard
# date: 7/13/21

# --------------- Section 1 --------------- #

# 1 | String Methods
#
# 1 - Save your name to a variable named name.
#   a. Center that variable within 30 characters. Print it.
#   b. Print the variable in all upper case.
#   c. Print the variable in all lower case.
#   d. Print the variable capitalized (Look to documentation.)
name = 'samaiya Howard'
print(name.center(30,'*'))
print(name.upper())
print(name.lower())
print(name.capitalize(),'\n')

# 2 | String Methods
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Find the first instance of the letter a. Print that position.
#   b. Find the first instance of the letter b. Print that position.
#   c. Find the first instance of a word of your choice. Print that position.
text = input('Enter a sentence: ')
print(text.find('a'))
print(text.find('b'))
choosing = input('Enter a word of your choice: ')
choosing = str(choosing)
print(text.find(choosing))

# 3 | String Methods. 
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Find the first apperaence (position) of every vowel in text. Save them each to a variable.
#   b. Using a built-in function, print the position of the vowel that shows up last.
#   c. Using a built-in function, print the position of the vowel that shows up first.
text = input('Enter a sentence: ').lower()
a = 'a'
e = 'e'
i = 'i'
o = 'o'
u = 'u'
print("the position of a is:",text.find(a))
print("the position of e is:",text.find(e))
print("the position of i is:",text.find(i))
print("the position of o is:",text.find(o))
print("the position of u is:",text.find(u))

# Just trying b and c (just for fun sense I finished early.)(failed)
# vowel = a,e,i,o,u
# vowel = str(vowel)
# find_vowel = text.find(vowel)
# vowel_len = len(vowel)
# print(find_vowel)
# print(text[vowel_len - 1])
# print(text[vowel_len + 1])
# def vowels():
#     if (text == 'a' or text == 'e' or text == 'i' or  text == 'o' or text == 'u'):
#         return text
#     else:
#         return False
# vowels()

# 4 | String Indexing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Print the 0th letter of the text using string indexing.
#   b. Print the 1st, 2nd, and 3rd letters of the text using string indexing.
#   c. Print the last letter of the text using string indexing.
#       HINT: There are multiple ways of doing this. Is there a function that we can use that will find
#           the position of the last letter, or atleast one off from it?
text = input('Enter a sentence: ')
print(text[0])
print(text[1], text[2], text[3])
print(text[-1])

# 5 | String Slicing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Slice text from the 2nd position to the 5th. Print that.
#   b. Slice text from the 0th position to the 8th. Print that.
#   c. Slice text from 3rd position to end. Print that.
#   d. Slice text from the beginning to 5 positions before the last character. Print that.
#       HINT: Use a function to get the last position of the string.
text = input('Enter a sentence: ')
print(text[2:5])
print(text[:8])
print(text[3:])
len_text = len(text)
print(text[:len_text - 5])


# 6 | String Slicing
#
# 1 - Prompt input from the user, asking them to enter a sentence. Save it to a variable named text.
#   a. Print the text, but only every 2nd character.
#   b. Print the text, but only every 3rd character.
#   c. Print the text, but in reverse order.
text = input('Enter a sentence: ')
print(text[::2])
print(text[::3])
print(text[::-1])