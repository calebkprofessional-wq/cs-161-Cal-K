def main(): #main function

    user_name = input("Enter your name: ") #asks for user name. stores string value in variable
    print(f"\nHello {user_name}") #prints the users name

    user_age = input("\nEnter your age: ") #asks for user age. stores string value in variable
    #print(user_age + 5) this doesn't work because you are trying to add a string and an integer
    print(f"\nYou are {user_age}") #prints user age

    how_many = input("\nEnter how many years you would like to add to your age: ") #asks user how many years they would like to add to their age
    total =  int(how_many) + int(user_age) #get total age by adding the two numbers
    string_total = str(total) #turns the total into a string
    statement = "\nYou will be " + string_total + " years old in " + how_many + " years." #final statement
    print(statement) #prints the final statement

    number_hours = float(input("\nEnter the number of hours you worked this week: ")) #gets the number of hours the user worked in a week and turns it into a float
    wage = float(input("\nEnter your hourly wage: ").strip().strip("$")) #gets the user's hourly wage and turns it into a float

    tax = {11600 : 0.1, 47150 : 0.12, 100525 : 0.22, 191650 : 0.24, 243725 : 0.32, 609350 : 0.35} #tax brackets, {gross income : percent taxed}
    gross_weekly = number_hours * wage #gets the gross weekly income by multiplying the hours by the wage
    pre_tax = gross_weekly * 50.0 #multiplies that value by 50 to get the gross annual income

    for key in tax.keys(): #iterates through the gross incomes in the tax brackets dictionary
        if pre_tax <= key: #if the gross annual income is less than or equal to the current gross income
            tax_bracket = tax[key] #final tax bracket is the tax bracket for the current gross income
            break #end the loop

    final_tax = pre_tax * tax_bracket #calculates final tax by multiplying the percent taxed by the gross income
    post_tax = pre_tax - final_tax #calculates post-tax income by subtracting the final tax from the gross income

    print(f''' 
Your weekly income is ${gross_weekly}.
Your gross annual income will approximately be ${pre_tax}.
You will owe approximately ${final_tax} in taxes.
Your income after tax will be ${post_tax}.''') #final print statement


main() #runs main function
