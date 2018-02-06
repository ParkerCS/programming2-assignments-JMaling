#FUNCTIONS AND IMPORTS (20PTS TOTAL)
# Be sure to comment all your functions as shown in notes
import import_me

#PROBLEM 1 (how many upper case - 4pts)
# Make a function takes a string as a parameter, then prints how many upper case letters are contained in the string.
# A loop that compares each letter to the .upper() or .lower() of itself will suffice.
def upperreader(str, uppercase=0):
    for i in str:
        if i == i.upper():
            uppercase += 1
    print("Number of Uppercase Letters = ", uppercase)


# PROBLEM 2 (Biggest, smallest, average - 4pts)
# Make a function which takes 3 numbers as parameters.
# The function then prints the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.
def average(a, b, c):
    if a > b and a > c:
        print("Largest = ", a)
    if b > a and b > c:
        print("Largest =", b)
    if c > a and c > b:
        print("Largest =", c)
    if a < b and a < c:
        print("Smallest = ", a)
    if b < a and b < c:
        print("Smallest =", b)
    if c < a and c < b:
        print("Smallest =", c)
    print("Average =", ((a + b + c) / 3))


# PROBLEM 4 (add me, multiply me - 4pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.
def sum_prod(a, b):
    product = a * b
    sum = a + b
    return product, sum


# PROBLEM 5 (Login - 4pts)
# Make a file called import_me.py in this same project
# Inside this new module/file, make a login function which works according to the flow diagram PasswordFlowchart.png in this folder
# Substitute your name for Rohan's, and use whatever generic password you want.


# PROBLEM 6 (main - 4pts)
# import the file import_me from Problem 5
# Create a main program using the format if __name__ == "__main__": 
# Place every call from problems 1 through 5 into this program.
if __name__ == "__main__":
    upperreader("ASDFGHGFDSASDFDSAasdfdsaASDSA")
    average(3, 1, 2)
    print(sum_prod(3, 4))
    import_me.password()
