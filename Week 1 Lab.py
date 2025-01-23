#Week 1 Lab: List Comprehensions

#Problem 1: Generate a list of all the numbers from 1-1000 that are divisible by 7
#Algorithm: Add a number to the list for every number from 7-1001 (since range goes to n-1)
# only if that number is divisible by 7
div_by_sev = [n for n in range(7,1001) if n%7==0]
print("Problem #1 Output:", div_by_sev)
print()

#Problem 2: Generate a list of all the numbers from 1-1000 that have the digit 3 in them
#Algorithm: Add a number to the list for every number from 7-1001 only if that number has 3 in it.
# We will check if the number has 3 by converting the number to a string and seeing if it contains 3
threes = [i for i in range(3,1001) if '3' in str(i)]
print("Problem #2 Output:", threes)
print()

#Problem 3: Remove all of the vowels in a string (can assume y is not a vowel)
#Algorithm: Add each letter from the string to a list if that letter isn't contained in aeiou
#(convert all the letters to lowercase in case the string has an uppercase) Then join them all in the end
string= "hello world"
vowelless_list = ''.join([char for char in string if char.lower() not in 'aeiou']) # I used help from tutorjoes for ''.join and "char for char"
print("Problem #3 Output:", vowelless_list)
print()

#Problem 4: Find all the words in a string that are less than 4 letters
#Algorithm: Divide up the string into individual words and add them to a list only if the length of the word is less than 4
string = "This is my string for my lab."
less_than_four = [word for word in string.split() if len(word)<4] #I used w3schools to find .split()
#I used perplexity ai to help me debug/find my mistake: discovered the terminology "word for word"
print("Problem #4:", less_than_four)
print()

#Problem 5: Use a dictionary comprehension that maps each word in a sentence to its length.
#Algorithm: Divide a string up into individual words. Order the words by length of individual words.
#I should use the word as the key because there are multiple words with the same amount of letters.
string2 = "This is my second string for my lab. One two three four."
my_dictionary = {word:len(word) for word in string2.split()} # I used geeks for geeks to research and get the structure for a dictionary comprehension
print("Problem #4:", my_dictionary)
print()

#Additional problem: Use a nested list comprehension to find all the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
#Algorithm: Make a list that takes away everything divided by 2, then everything divided by 3... and then make a list that is whatever isn't in that final list which wil only have prime numbers.
list = [n for n in range(1,1001) if n % 2 != 0]
list2 = [ n for n in list if n % 3 != 0]
list3 = [n for n in list2 if n % 4 != 0]
list4 = [n for n in list3 if n % 5 != 0]
list5 = [n for n in list4 if n % 6 != 0]
list6 = [n for n in list5 if n % 7 != 0]
list7 = [n for n in list6 if n % 8 != 0]
list8 = [n for n in list7 if n % 9 != 0]
final_list = [n for n in range (1,1001) if n not in list8]
print("Bonus Problem:", final_list)


