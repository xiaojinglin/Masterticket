ticket_price = 10
ticket_remaining = 100
name = ''
quantity = 0
total = 0
print(f"There is {ticket_remaining} ticket left!")
name = input("Please enter your name: ")
while True:
    quantity = input(f"{name}, How many tickets would you like to purchase? ")
    if not quantity.isnumeric():
        print(f"You should enter a digit number")
        continue
    quantity = int(quantity)
    if quantity>ticket_remaining:
        print(f"We only have {ticket_remaining} tickets left.")
        continue
    else:
        break
total = ticket_price * quantity
print(f"You have purchase {quantity} tickets, the total is ${total}.")
while True:
    enter = input(f"Enter y to confirm your order, c to cancel: ")
    if enter == 'y':
        print("Thank you for your purchase!")
        break
    elif enter == 'c':
        print("Your order has been cancelled")
        break
    else:
        enter = print("Invalid Input")
        continue
