# Functions can return something

# Making a Calculator for better understanding


def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1/num2


if __name__ == "__main__":
    while True:
        user_choice = int(input(
            """
                Enter your choice:
                    1.  add
                    2.  substract
                    3. multiply
                    4. Divide
                    5/ Quit App
            """
        ))

        if user_choice == 5:
            break

        prompt = " >"

        user_inp1 = int(input(f"Enter 1st digit {prompt}"))
        user_inp2 = int(input(f"Enter 2nd digit {prompt}"))

        print(add(user_inp1, user_inp2) if user_choice == 1 else None)
        print(substract(user_inp1,user_inp2) if user_choice == 2 else "", end  = " ")
        print(multiply(user_inp1, user_inp2) if user_choice == 3 else "", end = " ")
        print(division(user_inp1, user_inp2) if user_choice == 4 else "", end = " ")


        