service_charge = 2
ticket_price = 10
ticket_remaining = 100


def amount(num_of_ticket):
    return (ticket_price * num_of_ticket) + service_charge


while ticket_remaining >= 1:
    print(f"There is {ticket_remaining} ticket left!")
    name = input("What's your name: ")
    while True:
        num_tickets = input(f"{name}, How many tickets would you like to purchase? ")
        if not num_tickets.isnumeric():
            print(f"You should enter a digit number")
            continue
        num_tickets = int(num_tickets)
        if num_tickets > ticket_remaining:
            print(f"We only have {ticket_remaining} tickets left.")
            continue
        else:
            break
    amount = amount(num_tickets)
    print(f"You have purchase {num_tickets} tickets, the total is ${amount}.")
    while True:
        enter = input(f"Enter y to confirm your order, c to cancel: ")
        if enter == 'y':
            print("Thank you for your purchase!")
            ticket_remaining -= num_tickets
            break
        elif enter == 'c':
            print("Your order has been cancelled")
            break
        else:
            enter = print("Invalid Input")
            continue    