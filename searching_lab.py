#  ALICE IN WONDERLAND SPELL CHECKER
import re

# This function takes in a line of text and returns a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open("search_files/dictionary.txt")
dict_list = []
for line in file:
    words = split_line(line)
    for word in words:
        dict_list.append(word)
# print(dict_list)
file.close()

print("--- Linear Search ---")
file = open("search_files/AliceInWonderLand200.txt")
line_number = 0
for line in file:
    line = line.strip()
    words = split_line(line)
    line_number += 1
    for word in words:
        key = word.upper()
        i = 0
        while i < (len(dict_list) - 1) and dict_list[i] != key:
            i += 1
        if i >= len(dict_list) - 1:
            print("Line ", line_number, "Possible Misspelled Word: ", word)
file.close()

print("--- Binary Search ---")
file = open("search_files/AliceInWonderLand.txt")
line_number = 0
found = False
for line in file:
    line = line.strip()
    words = split_line(line)
    line_number += 1
    for word in words:
        lower_bound = 0
        upper_bound = len(dict_list) - 1
        key = word.upper()
        found = False
        while lower_bound <= upper_bound and not found:
            middle_pos = (lower_bound + upper_bound) // 2
            if dict_list[middle_pos].upper() < key:
                lower_bound = middle_pos + 1
            elif dict_list[middle_pos].upper() > key:
                upper_bound = middle_pos - 1
            else:
                found = True
        # print(word.upper())
        if not found:
            print("Line ", line_number, "Possible Misspelled Word: ", key)