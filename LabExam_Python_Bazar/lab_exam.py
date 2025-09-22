# Display a welcome message using print().
print("Hello and Welcome to my lab exam output :D\n")

# Step: 2
# This creates a variable for later use
name = "Cyrus Troy" # string
age = 19 # Int
GPA = 2.2 # Decimal -> Float

# Step: 3
# Display what data type the variables on step 2 is
print("the data type of name is:", type(name))
print("the data type of age is:", type(age))
print("the data type of GPA is:", type(GPA))

print()

# Step: 4
# Asks the user whats their age using input() function
UserAge = input("whats' your age? \n>>") # default string

# Convert UserAge to int
UserAge = int(UserAge)

# Add 5 years or 5 to int
UserAge = UserAge + 5

# Display the new age
print("Your age on the next 5 years is:", UserAge)

# Step 5: just a comment

# This file/program is for my 1st sem output
# Created in september 22 2025


# Multi line comment using """
"""
         #####                                                          
        #     # #   # #####  #    #  ####     ##### #####   ####  #   # 
        #        # #  #    # #    # #           #   #    # #    #  # #  
        #         #   #    # #    #  ####       #   #    # #    #   #   
        #         #   #####  #    #      #      #   #####  #    #   #   
        #     #   #   #   #  #    # #    #      #   #   #  #    #   #   
         #####    #   #    #  ####   ####       #   #    #  ####    #   
                                                                        
"""

print(f"Hello my name is {name}")
print(f"My age is: {age}")
print(f"My average GPA is: {GPA}")

print("my average grade if:", GPA)