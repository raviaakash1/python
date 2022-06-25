# Prompting and Passing
from sys import argv

script, user_name, last_name = argv
prompt = 'ravi@Linux0&979837@341: '
print(f"Hi {user_name}, I'm the {script} script. ")
print("I'd liek to ask you a few questions.")
print("Do you like Ice Creams ?")
likes = input(prompt)

print(f"Where Do you live {user_name}?")
lives = input(prompt)

print(f"What kind of system you have {user_name}")
computer = input(prompt)

print(f"""
Alright, user {user_name} {last_name} so you said {likes} about liking ice creams.
You live in {lives}. Not sure where it is.
And you have a system {computer}. Nice.
""")