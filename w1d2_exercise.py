# ITP Week 1 Day 2 Exercise

# We will replicate a number magic trick with Python! Below is the magic trick that we will convert! Below that is the python instructions, you will need to complete.

# Step 1: Pick a number from 1 - 9
# 7
# Step 2: Multiple by 2
# 14
# Step 3: Add 10 to the total
# 24
# Step 4: Divide by 2
# 12
# Step 5: Subtract by the original number
# Final Number: 5

# assign a variable "step_1" to a number of your choice between 1 - 9
# prompt the user so the equation uses their chosen number

step_1 = int(input("Pick a number from 1 to 9: "))

# assign a variable "step_2" to the product of step_1 and the number 2

step_2 = step_1 * 2

# assign a variable "step_3" to the sum of step_2 and the number 10

step_3 = step_2 + 10

# assign a variable "step_4" to the quotient of step_3 and the number 2

step_4 = step_3 / 2

# assign a variable "step_5" to the difference between step_4 and step_1

step_5 = step_4 - step_1

# print step_5 and you should see 5!

print(step_5)

# BONUS 2: can you REFACTOR using less variables?

step_1 = int(input("Pick a number from 1 to 9: "))

result = ((step_1 * 2) + 10) / 2 - step_1

print(result)
