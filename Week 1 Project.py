import datetime
import calendar

class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"\n{self.name} is a {self.species}, and is {self.age} years old."

my_dog = Pet("Flower", "dog", 12)
my_cat = Pet("Soda", "cat", 4)

pet_list = []

def pets():
    print(f"\nHello, my name is Caleb. I have two pets. Their names are {my_dog.name} and {my_cat.name}.")
    print(f"{my_dog}{my_cat}")

    while True:
        cont = input("\nDo you have any pets? (y/n) ").lower().strip()
        if cont == "n":
            print("\nOk...")
            return
        elif cont == "y":
            print("\nOk, cool.")
            break
        else:
            print("\nThat is not a valid input.")
            continue

    while True:
        num_pets = input("\nHow many pets do you have? ")
        try:
            num_pets = int(num_pets)
            break
        except ValueError:
            print("\nPlease enter a number.")
            continue

    for i in range(num_pets):
        name = input("\nWhat is your pet's name? ")
        species = input("\nWhat is your pet's species? ")
        age = input("\nWhat is your pet's age? ")
        pet = Pet(name, species, age)
        print(f"{pet}")
        pet_list.append(pet)

    print(f"\nYou have {len(pet_list)} pets.")
    for i in pet_list:
        print(i)



def month():
    current = datetime.datetime.now()
    now = datetime.date.today()
    this_month = now.month
    this_year = now.year
    __, num_days = calendar.monthrange(this_year, this_month)
    seconds = num_days * 86400

    print(f"\nIt is currently {current.strftime("%A")}, {current.strftime("%B")} {current.strftime("%d")}, {current.strftime("%Y")}. The current time is {current.strftime("%H")}:{current.strftime("%M")}:{current.strftime("%S")}:{current.strftime("%f")}")
    print(f"\nThere are {seconds} seconds in {current.strftime("%B")}.")

def eggs():
    while True:
        num_eggs = input("\nHow many eggs do you have? ")
        try:
            num_eggs = int(num_eggs)
            break
        except ValueError:
            print("\nPlease enter a number.")
            continue
    dozens = num_eggs // 12
    rest = num_eggs % 12

    print(f"\nYou have {dozens} dozen eggs, with {rest} extra.")


def main():
    while True:
        print('''
Hello. Would you like to: 

1. Talk about pets?
2. Discuss the current month?
3. Figure out how many dozens of eggs you have?''')
        answer = input("\nPlease enter your answer as a number from 1 through 3: ")
        try:
            answer = int(answer)
        except ValueError:
            print("\nPlease enter a number")
            continue
        if int(answer) < 1 or int(answer) > 3:
            print("\nPlease enter a number from 1 through 3.")
            continue
        elif int(answer) == 1:
            pets()
        elif int(answer) == 2:
            month()
        elif int(answer) == 3:
            eggs()

main()
