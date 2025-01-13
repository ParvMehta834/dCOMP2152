# Sample Coding Questions 01 Week 01
# First and Last Name: Parvkumar Mehta

# Defining Variables: Define an array variable with the following elements 1, 4, 7, 9.
array_variable = [1, 4, 7, 9]

# Order of Operations: Fully-Bracketed Version of the Expression
a, b, c, d = 1, 2, 3, 4
# e = a - b ** c // d + a % c
fully_bracketed_e = ((a - ((b ** c) // d)) + (a % c))

# Formatting: Print temperature with formatting
temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))

# Common Functions: Ask user for their age, add 22, and display the result
userAge = int(input("Please enter your age: "))
userAge += 22
print(f"Now showing the shop items filtered by age: {userAge}")