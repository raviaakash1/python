# More Variables and Prinitng
# formatted string :;  String are very much relevant to every programmer, so formatting the string like for example if we want to add the value
# of a variable to a string then in those cases we can use string formatter which is provided by python. Sample:
#       f before double quotes (") is used to indicate that this is a formattable string and we need to use {} if we want to add the variable
#       data into this string. FOr Example:
#           var1 = 12
#           str1 = f"Printing the value of the var1 {var1}"

x = 10

string = f"This is the value of x {x}"

print(string)

# Study Drill
# COnvert inches to cm and pounds to kg

# cm to inches

centi_meter = 12 # in cm
inches = 12 * 2.54 #1 inch = 2.54 cm 

pounds = 12 # pounds
kgs = 12 * 0.453592 # 1 pound = 0.453592

print(f"Height {centi_meter}cm or {inches}in \nWeight {pounds}lbs or {kgs}kg")

