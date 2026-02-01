#Comments are above important lines

"""
"Average function" part of the assignment, since I went over the expectations in the actual code:

1.
-------------------------
def average(one, two, three):
    return (one + two + three)/3

print(average(7, 5, 9)) : prints 7.0
print(average(6, 6, 7)) : prints 6.3333333333
-------------------------
2.
-------------------------
print(average(6, 6, 7))

def average(one, two, three):
    return (one + two + three)/3

This does not run, as the function needs to be defined before it is called for the first time.
-------------------------
3.
-------------------------
def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

print(average(7, 5, 9))
print(average(6, 6, 7))
print(num1)

This script does not run, as the parameter "num1" is not a defined variable.
-------------------------
"""

from time import sleep



def average():
    """Averages any number of numbers, then prints the output"""

    print("\nYou will now enter a series of numbers. An average will be taken of these numbers.")
    print("Enter 'break' whenever you are done entering numbers.")
    total_numbers = 0.0
    total = 0.0

    while True:
        current_number = input("\nEnter a number: ").strip()
        if current_number.lower() == "break":
            break
        else:
            try:
                current_number = float(current_number)
            except ValueError:
                print("\nPlease enter a valid number.")
                continue
        total_numbers += 1.0
        total += current_number

    print(f"\nOk. You entered {int(total_numbers)} numbers. The sum of these numbers is {total}. Your average, that being {total}/{int(total_numbers)}, is {total/total_numbers}. Have a nice day.")
    sleep(5)

def dog_years(dog_age):
    """Takes a dog's age and returns the age in human years"""

    #This is the equation that was give. In part 6, you state that 3 should convert into 22.3, when it converts into 28.
    human_age = 24 + (dog_age - 2) * 4

    return human_age

def car_price(purchase_price, car_type, number_years):
    """Takes the purchase price, car type, and number of years in the future to check the price of a car, then prints a price"""

    match car_type:
        case "italian":
            multiplier = 0.05
            up_or_down = "up"
        case "german":
            multiplier = 0.05
            up_or_down = "down"
        case "japanese":
            multiplier = 0.07
            up_or_down = "down"


    #I am assuming here that you meant that the price increases/decreases in a compounding fashion, not a simple fashion

    current_price = purchase_price
    for i in range(number_years):
        change = current_price * multiplier
        if up_or_down == "up":
            current_price += change
        elif up_or_down == "down":
            current_price -= change

    print(f"\nThe value of a {car_type} car bought at ${purchase_price} will be ${current_price} after {number_years} years.")
    sleep(5)

def icecream_cone_price(scoops):
    """Takes a number of scoops and calculates/prints the price of a cone"""

    print(f"\nA {scoops}-scoop icecream cone will cost you ${scoops * 1.5 + 2.25}")
    sleep(5)



def main():
    """Main function. Defines overall behavior of the program"""

    while True:
        print('''\nHello. How can I help you today?

1. Average a series of numbers.
2. Calculate your dogs age in human years.
3. Calculate the price of your car in x years.
4. Calculate the price of an icecream cone.
5. End the script.''')
        choice = input(f"\nPlease enter a valid number from 1 through 5: ").strip()
        try:
            choice = int(choice)
        except ValueError:
            print("\nPlease enter a valid choice.")
            continue

        if choice == 1:
            average()

        elif choice == 2:

            while True:
                dog_age = input("\nEnter your dog's age: ").strip()
                try:
                    dog_age = int(dog_age)
                    break
                except ValueError:
                    print("\nPlease enter a valid number (no decimals).")

            dog_name = input("\nEnter your dog's name: ").strip()

            print(f"\nYour {dog_name} is {dog_years(dog_age)} years old.")
            sleep(5)

        elif choice == 3:

            #I would have rather included these loops in the function itself, but I wanted to follow the assignment directions here

            while True:
                purchase_price = input("\nEnter the purchase price of the car: ").strip('$').strip()
                try:
                    purchase_price = float(purchase_price)
                    break
                except ValueError:
                    print("\nPlease enter a valid price.")
                    continue

            while True:
                car_type = input("\nEnter the type of the car: ").lower().strip()
                if car_type not in ["italian", "german", "japanese"]:
                    print("\nPlease enter a valid car type.")
                    continue
                else:
                    break

            while True:
                number_years = input("\nHow many years after purchasing are you looking to check the price? ").strip()
                try:
                    number_years = int(number_years)
                    break
                except ValueError:
                    print("\nPlease enter a valid number.")
                    continue

            car_price(purchase_price, car_type, number_years)

        elif choice == 4:

            while True:
                scoops = input("\nHow many scoops of icecream do you want? ").strip()
                try:
                    scoops = int(scoops)
                    break
                except ValueError:
                    print("\nPlease enter a valid number.")
                    continue

            icecream_cone_price(scoops)


        elif choice == 5:
            quit()

        else:
            print("\nPlease enter a valid choice.")
            continue

main()






