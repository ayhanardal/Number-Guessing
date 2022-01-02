import random

top_of_range = input("Type a top number : ")

try_point = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
elif top_of_range < 0:
    print("Please type a number larger than 0 next time.")
    quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)

while True:
    try_point += 1
    user_guess = input("Make a guess : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess < random_number:
        print("Raise!")
    else:
        print("Reduce!")

print("You try : "+ str(try_point))

while True:
    exit = input("Type 'exit' for exit : ").lower()
    if exit == "exit":
        quit()
    else:
        continue
