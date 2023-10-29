# 29/10/23


#             Starting 


# print ("Hello World!")

# print("   /\ ")
# print("  /  \ ")
# print(" /")
# print("/")
# print("\ ")
# print(" \ ")
# print("  \ ")
# print("   \ ")
# print("    \ ")
# print("     /")
# print("    /")
# print("\  /")
# print(" \/")
#
# print("**      **")
# print(" * *  * *")
# print("  * ** *")
# print("   *  *")
# print("     *")

# -------------------------------------------------------------------------------------------------------------------------

                    # Varibles and Data Types

#Here we used two variables name and age and used them in the print statements, to avoid the reptitive effort of recorrexting them if i needed to change name or age.
# NEW LEARNING: if you have to use + sign, i.e. cocatenate then the variable must be a string as you can't concatenate a string to string, not an int, so to avoid this problem we can , instead of + sign.

# name="Gundeep"
# age = "20"

# print("There once was a man named",name) # we can either use , or + 
# print("he was",age,"years old.")

# name = "Sukhman"#This an intresting thing as reassining name here changes the name after this point only the above values are not changed.
# print("He really likes the name " + name)
# print("but he didn't liked being " + age + ".")


# Datatypes include string, int, and boolean


# -------------------------------------------------------------------------------------------------------------------------

            #  STRINGS


# # simply printing
# print("xyz")


# # printing with a new line
# print("Giraffe\nAcamdemy")


# # all the characters after the backslash mean that we want to print it literally
# # otherwise we would not be able to print " in a string
# print("Giraffe\"Academy")


# # printing a string using a variable
# phrase ="Giraffe Academy"
# print(phrase)


# # concatenating a string
# phrase="Giraffe Acamedy"
# print(phrase + " is a for dumb people")


# # Using functions for strings
# # we use functions to :
# #             modify strings
# #             to get information of strings
#
# phrase="Giraffe Academy"
# print(phrase.lower())
# print(phrase.upper())
# print(phrase.upper().isupper())


# # length function
# phrase="Giraffe Academy"
# print(len(phrase))


# # To print individual characters
# phrase="Giraffe Academy"
# print(phrase[5])


# # Index function
# # We can use this to locate the characters
# phrase="Giraffe Academy"
# print(phrase.index("a"))


# # Replace function
# phrase="Giraffe Academy"
# print(phrase.replace("Academy","Institute"))



# -------------------------------------------------------------------------------------------------------------------------


#                              PLAYING WITH NUMBERS

# #       simply printing numbers
# print(2)


# #         We can also perform simple arithmetic ops
# print(3*4+5)
# print(3*(4+5))
# print(10%3) #modulus


# #          Using variables
# my_num=5
# print(my_num)


# #            Converting the number into string
# my_num=5
# print(str(my_num))
# print(str(my_num)+" is my favourite number")
# the previous thing would not have been possible if we didn't convert the number into string


# #                       MATHS OPERATORS


# # abs-> absolute value
# my_num = -3
# print(abs(my_num))


# #  Power
# print(pow(3, 4))


# #  Max
# print(max(4, 6))


# #   Min
# print(min(4, 6))


# #   Round function
# print(round(3.55))


#                   Importing libraries

from math import *

# print(floor(3.7))


# print(ceil(3.8))


# print(sqrt(36))

# -----------------------------------------------------------------------------------------------------------------------------------------------


# # Getting input from users

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hi "+ name+"! You are " + age)

### -------------------------------------------------------------------------------------------------------------------------

##Building a basic calculator(adding two numbers)

# a=float(input("Enter first number: "))
# b=float(input("Enter second number: "))
# sum=a+b
# print("Sum of",a,"and",b,"is",sum)

### ------------------------------------------------------------------------------------------------------------------------

##Mad libs game
