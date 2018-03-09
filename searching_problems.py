'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''
import re

# This function takes in a line of text and returns a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
file = open("search_files/super_villains.txt")
all_words = []
for line in file:
    words = split_line(line)
    for word in words:
        all_words.append(word)
# print(all_words)

#1.  (7pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.  (read the file line by line to accomplish this task)
word_list = []
max_val = 0
file = open("search_files/dictionary.txt")
for line in file:
    words = split_line(line)
    for word in words:
        word_list.append(word)
print(word_list)
for word in word_list:
    if len(word) > max_val:
        max_val = len(word)
print("Longest Word = ", max_val, "Letters")

#2.  (7pts)  Write code which finds
#  The total word count AND average word length of "AliceInWonderLand.txt"
file = open("search_files/AliceInWonderLand.txt")
word_list = []
letter_count = 0
word_count = 0
avg_len = 0
for line in file:
    words = split_line(line)
    for word in words:
        word_list.append(word)
for word in word_list:
    word_count += 1
for word in word_list:
    letter_count += len(word)
avg_len = (letter_count / word_count)
print("Word Count = ", word_count)
print("Average Length of Word = ", round(avg_len))


# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?
cheshire_count = 0
cheshirecat_count = 0
for line in file:
    words = split_line(line)
    for word in words:
        word_list.append(word)
for word in word_list:
    if word == "Cheshire":
        cheshire_count += 1
for i in range(len(word_list)):
    if word_list[i].upper() == "CHESHIRE" and word_list[i + 1].upper() == "CAT":
        cheshirecat_count += 1
print(cheshire_count)
print(cheshirecat_count)

#### OR #####

#3  (13pts)Find the most frequently occurring 
#  seven letter word in "AliceInWonderLand.txt"

# CHALLNENGE PROBLEM  (for fun, not for credit).  
#  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.




