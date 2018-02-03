# LOOPS (16pts TOTAL)
import random

# PROBLEM 1 (Fibonacci - 4pts)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.
x = 1
y = 1
z = 0
for i in range(14):
    z = x + y
    x = y
    y = z
    print(z)


# PROBLEM 2 (Dice Sequence - 6pts)
# You roll five six-sided dice, one by one.
# What is the probability that the value of each die
# is greater than OR EQUAL TO the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.
success = 0
failure = 0
iterations = 10000
for i in range(iterations):
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    die3 = random.randrange(1,7)
    die4 = random.randrange(1,7)
    die5 = random.randrange(1,7)
    if die1 >= die2 >= die3 >= die4 >= die5:
        success += 1
    if die1 < die2 or die2 < die3 or die3 < die4 or die4 < die5:
        failure += 1
prob_success = success / iterations
prob_fail = failure / iterations
print("Probability of Success =", round((prob_success * 100), 3), "%")
# print("Probability of Failure =", round((prob_fail * 100), 3), "%")


# PROBLEM 3 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve.
A = 1
B = 1
C = 1
D = 1
num_list = [A, B, C, D]
new_num_list = [D, C, B, A]
