import random
from time import sleep
import requests
import psutil

states_and_capitals = {
    "Alabama" : "Montgomery",
    "Alaska" : "Juneau",
    "Arizona" : "Phoenix",
    "Arkansas" : "Little Rock",
    "California" : "Sacramento",
    "Colorado" : "Denver",
    "Connecticut" : "Hartford",
    "Delaware" : "Dover",
    "Florida" : "Tallahassee",
    "Georgia" : "Atlanta",
}

def try_int(prompt):
    """Takes a user input and verifies that it is an integer"""
    while True:
        number = input(prompt)
        try:
            number = int(number)
            return number
        except ValueError:
            print("\nPlease enter a valid number.")
            sleep(1)
            continue

def pool_price(age):
    """Takes a user's age and returns the pool entrance price"""
    if age < 2:
        return 0
    elif age > 1 and age < 11:
        return 3
    elif age > 10 and age <= 60:
        return 6
    elif age > 60:
        return 4

def state_capital(random_number):
    """Takes a state and prints the capital state"""
    while True:
        state = input("\nPlease enter a state: ")
        if state in states_and_capitals:
            break
        else:
            print("\nPlease enter a valid state.")
            sleep(1)
            continue
    if random_number == 1:
        if state == "Alabama":
            capital = "Montgomery"
        elif state == "Alaska":
            capital = "Juneau"
        elif state == "Arizona":
            capital = "Phoenix"
        elif state == "Arkansas":
            capital = "Little Rock"
        elif state == "California":
            capital = "Sacramento"
        elif state == "Colorado":
            capital = "Denver"
        elif state == "Connecticut":
            capital = "Hartford"
        elif state == "Delaware":
            capital = "Dover"
        elif state == "Florida":
            capital = "Tallahassee"
        elif state == "Georgia":
            capital = "Atlanta"
    elif random_number == 2:
        capital = states_and_capitals.get(state)
    elif random_number == 3:
        match state:
            case "Alabama":
                capital = "Montgomery"
            case "Alaska":
                capital = "Juneau"
            case "Arizona":
                capital = "Phoenix"
            case "Arkansas":
                capital = "Little Rock"
            case "California":
                capital = "Sacramento"
            case "Colorado":
                capital = "Denver"
            case "Connecticut":
                capital = "Hartford"
            case "Delaware":
                capital = "Dover"
            case "Florida":
                capital = "Tallahassee"
            case "Georgia":
                capital = "Atlanta"
    print(f"\nThe capital of {state} is {capital}.")
    sleep(5)

def divisible_five():
    """Takes a number and checks if it is divisible by 5"""
    number = try_int("\nEnter a number: ")
    if number % 5 == 0:
        print("\nYour number is divisible by 5.")
    else:
        print("\nYour number is not divisible by 5.")
    sleep(5)

def main():
    """Main function"""
    print("Hello.")
    while True:
        print('''
1. Check if a number is divisible by 5
2. Print a state capital
3. Check the entrance price of a certain public pool based on age
4. See how many times 'Hugo' appears in the HTML code for The world's fastest framework for building websites
5. See the number of processes running on your system''')
        pick_option = try_int("\nEnter your choice: ")
        if pick_option == 1:
            divisible_five()
        elif pick_option == 2:
            state_capital(random.randint(1,3))
        elif pick_option == 3:
            user_age = try_int("\nEnter your age: ")
            print(f"\nIt will cost you ${pool_price(user_age)} to go to this pool, as you are {user_age} years old.")
            sleep(5)
        elif pick_option == 4:
            gohugo = requests.get("https://gohugo.io/")
            gohugo_html = gohugo.text
            count = gohugo_html.count("Hugo")
            print(f"\nThe substring 'Hugo' appears {count} times in the HTML source of https://gohugo.io.")
            sleep(5)
        elif pick_option == 5:
            num_processes = len(list(psutil.process_iter()))
            print(f"\nNumber of running processes: {num_processes}")
            sleep(5)
        else:
            print("\nPlease enter a valid number.")
            sleep(1)



if __name__ == "__main__":
    main()