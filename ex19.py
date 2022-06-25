# Functions and Variables
#  We can give our functions the valuse it needs to print them. We can give it straight numbers. We can give it variables. We can give it maths.
#  We can even combine maths and variables.

def call_fun_in_ways(num1,num2):
    print(num1+num2)

digit1 = 1
digit2 = 2

# calling call_fun_in_ways in 10 different ways
call_fun_in_ways(1, digit2)
call_fun_in_ways(digit1, 2)
call_fun_in_ways(digit1, digit2)

call_fun_in_ways(digit1+digit2, digit1-digit2)
call_fun_in_ways(digit1, digit2+digit1)
call_fun_in_ways(digit1+digit2, digit2)

call_fun_in_ways(1, 2)
call_fun_in_ways(1+2, 2)
call_fun_in_ways(1, 2+1)
call_fun_in_ways(1+2, 2+3)

# Note we can also take command line arguments and directly send tose args to this function.

