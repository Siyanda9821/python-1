stock1 = "vanilla"
stock2 = "chocolate"
stock3 = "tin roof"
stock4 = "cookie dough"


flavour = input("Enter your favourite ice cream flavour: ").lower()


# if flavour == stock1:
#     print("It exists")

# elif flavour == stock2:
#     print("It exists")

# elif flavour == stock3:
#     print("It exists")

# elif flavour == stock4:
#     print("It exists")

# else:
#     print("Sorry, we don't have that on stock")

if flavour == stock1 or flavour == stock2 or flavour == stock3 or flavour == stock4:
    print("We have the flavour in stock")
else:
    print("We don't have the flavour in stock")

# x = flavour.replace("&", " ").replace("  ", "")
# print(x)

flavours = ["chocolate", "tin roof", "cookie dough", "vanilla"]


if flavour in flavours:
    print("We have the flavour in stock")
else:
    print("We don't have the  flavour in stock")
