# Variables and Names
# A variable is nopthing but a name for something. we usually give variables name which are meaningful to what we will be doing or what kind of 
# data we will be storing in that variable. So that it becomes easier for us to identify what is the purpose of that variable

# If you get stck with this exercise, remember the trick you have been taught so far of finding difference s and focusing on details
#   1. Write a comment above each line explaining to yourself in English what it does
#   2. Read your .py file backwards
#   3. Read your .py file outloud, even saying the characters

car = 100
space_in_car = 4
drivers = 30
passengers = 90
cars_not_driven = car - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passenger_in_car = passengers/cars_driven

print("There are ",car, "cars available .")
print("There are only",drivers, "drivers avaiable.")
print("There will be ",cars_not_driven," empty cars today.")
print("We can transport ",carpool_capacity," people today")
print("We have ",passengers," to carpool today")
print("We need to put about ",average_passenger_in_car," in each car")


# Study Drill
# car_pool_capacticy was either not decalred in the program or was named wrongly
# 1. it depends upon if you want the data to be float or integer removing 4.0 to 4 just changes the data type thats all and precision is lost
# Others are just details which are not that relevant
