# String and Text
# String is nothing but a bit of text which we want to display or "export" 

#  f-string --> f"string goes here {Variablel name goes here}"
# You can also format the string using .format() syntax

#Declaring and Initializing Variables
a = 1
b = " There There !!!! "

new = "data"

#Using f-string to format the string
x = f"{a}"
y = f"{b}"

#  Using Old way of formatting the string
new_string = x+y + "{}".format(new)

# Printing
print("It was a bad joke {}  still {}".format("But","Haha"))
print(new_string)

# we can also use indexing in the .format()

print("It was a Bad Joke {1} still {0}".format("Hahah","But"))
print("It was a Bad Joke {0} still {1}".format("Hahah","But"))

# Keyword arguments are also possible
print("It was a bad joke {but} still {ha}".format(but="But",ha="Hahaha"))

# Type Specifications are also allowed
# More parameters can be included within the curly braces of our syntax. Use the format code syntax {field_name: conversion}, 
# where field_name specifies the index number of the argument to the str.format() method, 
# and conversion refers to the conversion code of the data type.

print("%20s" % ('checkfordata', ))
print("%-20s" % ('dontknow', ))
print("%1s" % ('checkfor data', ))

# Example: %c– character  

type = 'bug'
 
result = 'troubling'
 
print('I wondered why the program was %s me. Then\
it dawned on me it was a %s .' %
      (result, type))

# Example: %i signed decimal integer and %d signed decimal integer(base-10) 
match = 12000
 
site = 'amazon'
 
print("%s is so useful. I tried to look\
up mobile and they had a nice one that cost %d rupees." % (site, match))

# Some another useful Type Specifying 
# %u unsigned decimal integer
# %o octal integer
# f – floating point display
# b – binary
# o – octal
# %x – hexadecimal with lowercase letters after 9
# %X– hexadecimal with uppercase letters after 9
# e – exponent notation
# You can also specify formatting symbols. The only change is using a colon (:) instead of %. For example, instead of %s use {:s} and instead of %d use (:d}

# Syntax : String {field_name:conversion} Example.format(value)
# Errors and Exceptions : 
# ValueError : Error occurs during type conversion in this method. 


# Demonstrate ValueError while
# doing forced type-conversions
 
# When explicitly converted floating-point
# values to decimal with base-10 by 'd'
# type conversion we encounter Value-Error.
# print("The temperature today is {0:d} degrees outside !"
#       .format(35.567))
 
# Instead write this to avoid value-errors
''' print("The temperature today is {0:.0f} degrees outside !"
                                            .format(35.567))'''
print("The temperature today is {0:.0f} degrees outside !"
                                            .format(35.567))
# Padding Substitutions or Generating Spaces
# Example 7: Demonstration of spacing when strings are passed as parameters
# By default, strings are left-justified within the field, and numbers are right-justified. We can modify this by placing an alignment code just following the colon.

# <   :  left-align text in the field
# ^   :  center text in the field
# >   :  right-align text in the field
# To demonstrate spacing when
# strings are passed as parameters
print("{0:4}, is the computer science portal for {1:8}!"
      .format("CheckDataCheck", "geeks"))
 
# To demonstrate spacing when numeric
# constants are passed as parameters.
print("It is {0:5} degrees outside !"
      .format(40))
 
# To demonstrate both string and numeric
# constants passed as parameters
print("{0:4} was founded in {1:16}!"
      .format("CheckDataCheck", 2009))
 
 
# To demonstrate aligning of spaces
print("{0:^16} was founded in {1:<4}!"
      .format("CheckDataCheck", 2009))
 
print("{:*^20s}".format("CheckData"))


print("Formatting Example with padding")
# Formatter Example
# which prints out i, i ^ 2, i ^ 3,
#  i ^ 4 in the given range
 
# Function prints out values
# in an unorganized manner
def unorganized(a, b):
    for i in range(a, b):
        print(i, i**2, i**3, i**4)
 
# Function prints the organized set of values
def organized(a, b):
    for i in range(a, b):
 
        # Using formatters to give 6
        # spaces to each set of values
        print("{:6d} {:6d} {:6d} {:6d}"
              .format(i, i ** 2, i ** 3, i ** 4))
 
# Driver Code
n1 = int(input("Enter lower range :-\n"))
n2 = int(input("Enter upper range :-\n"))
 
print("------Before Using Formatters-------")
 
# Calling function without formatters
unorganized(n1, n2)
 
print()
print("-------After Using Formatters---------")
print()
 
# Calling function that contains
# formatters to organize the data
organized(n1, n2)


print("Python format with dict")
# Using a dictionary for string formatting 
# Using a dictionary to unpack values into the placeholders in the string that needs to be formatted. We basically use ** to unpack the values. This method can be useful in string substitution while preparing an SQL query.


introduction = 'My name is {first_name} {middle_name} {last_name} AKA the {aka}.'
full_name = {
    'first_name': 'Tony',
    'middle_name': 'Howard',
    'last_name': 'Stark',
    'aka': 'Iron Man',
}
 
# Notice the use of "**" operator to unpack the values.
print(introduction.format(**full_name))


print("Python format with list")
# Python format() with list
# Given a list of float values, the task is to truncate all float values to 2-decimal digits. Let’s see the different methods to do the task.


# Python code to truncate float
# values to 2 decimal digits.
   
# List initialization
Input = [100.7689454, 17.232999, 60.98867, 300.83748789]
   
# Using format
Output = ['{:.2f}'.format(elem) for elem in Input]
   
# Print output
print(Output)