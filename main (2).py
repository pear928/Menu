#small, med, and large having diff price
# each will have 2 toppings by default (no extra cost)
# if they want more toppings each will cost extra
# for crust 1 , 2 doesn't cost extra but 3 costs extra

total_bill = 0

#asking for pizza size
pizza_size = {1: ["small", 10], 2: ["medium", 12], 3: ["large", 14]}
print(
    "Welcome to Param's Restaurant! Your options for pizza size are: \n1 - Small - $10 \n2 - Medium - $12 \n3 - Large - $14\nYou can choose any two toppings for free.\n"
)
customer_size = int(
    input("What size of pizza would you like? \nYour choice is: "))

total_bill += pizza_size[customer_size][1]

#asking for type of crust
type_of_crust = {1: ["thin", 0], 2: ["deep dish", 0], 3: ["cheese-stuffed", 2]}
customer_crust = int(
    input(
        "\n\nWhat type of crust would you like? \n1 - Thin - $0 \n2 - Deep dish - $1 \n3 - Cheese-stuffed - $2 \nYour choice is: "
    ))

total_bill += type_of_crust[customer_crust][1]

#asking for amount of cheese
amount_of_cheese = {1: ["less", 0], 2: ["regular", 0], 3: ["extra", 1]}
customer_cheese = int(
    input(
        "\n\nHow much cheese would you like? \n1 - Less  \n2 - Normal \n3 - Extra (+$1) \nYour choice is: "
    ))

total_bill += amount_of_cheese[customer_cheese][1]

# #asking about toppings
# number_of_toppings = input(
#     "\nWould you like to only have your two free toppings, or add extra? \n1 - Free toppings \n2 - Extra toppings. \nYour choice is: "
# )
toppings_list = {
    1: "pepperoni",
    2: "pineapple",
    3: "bell peppers",
    4: "olives",
    5: "jalapenos",
    6: "onions",
    7: "basil",
    8: "mushroom",
    9: "tomatoes",
    10: "anchovies",
}

print(f"\nList of toppings available:")
for i in range (1, len(toppings_list)):
    print(f"{i} - {toppings_list[i]}")
    
list_of_toppings = []
list_of_toppings.append(toppings_list[int(input("\nWhat is the first topping that you would like on your pizza? "))])
    
list_of_toppings.append(toppings_list[int(input("What is the second topping that you would like on your pizza? "))])

extra_topping_input = input(
    "Would you like to add an extra topping for a price of $2? \nY - Yes \nN - No \nYour choice is: "
).lower()

if extra_topping_input == "y":
    more_customer_toppings = int(input(
        "How many additional toppings would you like? Maximum is 7 more. "))

    for _ in range(more_customer_toppings): 
        list_of_toppings.append(toppings_list[int(input("Which topping would you like to add? "))])
        total_bill += 2
    print(f"Your toppings are: ")
    for i in range(len(list_of_toppings)):
        print(list_of_toppings[i])

else:
    print(f"Your toppings are: ")
    for i in range(len(list_of_toppings)):
        print(list_of_toppings[i])




soft_drinks = {
    1: ["Fanta", 1],
    2: ["Pepsi", 1],
    3: ["Coke", 1],
    4: ["Sprite", 1]
}
customer_soft_drink = int(input("\nWhich soft drink would you like? \n1 - Fanta - $1 \n2 - Pepsi - $1 \n3 - Coke - $1 \n4 - Sprite - $1 \nYour choice is: "))
total_bill += 1

print(f"\nYour final order is: a {pizza_size[customer_size][0]} size pizza with {type_of_crust[customer_crust][0]} crust, with {amount_of_cheese[customer_cheese][0]} cheese and {list_of_toppings}, with a side drink of {soft_drinks[customer_soft_drink][0]}.")
print("Your total bill is: " + str(total_bill))
user_payment = int(input("How much money will you be paying? "))
change = user_payment - total_bill
print("Your change is: " + str(change))