#Welcoming the customer into the shop
print("Welcome to Knit & Co. Where we sell our customer's high-quality knits.")

#Obtaining the shoppers input
shopper_name = input("Please enter your name: ")
item = input("What kind of yarn would you like to buy?: ")
yarn_color = input("What color: ")
yarn_price = float(input("Price: $"))
yarn_quantity = int(input("How much do you want to buy?: "))

#Processing the data
total_price = yarn_price * yarn_quantity

#Receipt 
print()
print('=' * 30)
print('=' * 30)
print("Your receipt:\n")
print(" Name: " + shopper_name.title())
print(" Purchased item: " + yarn_color.capitalize() + " " + item.lower())
print(" Price: $" + str(yarn_price))
print(" Quantity: " + str(yarn_quantity))
print(" Total price: $" + str(total_price))
print('=' * 30)
print('=' * 30)