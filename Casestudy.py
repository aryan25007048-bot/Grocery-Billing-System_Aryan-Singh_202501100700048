# Input prices of three different items
item1 = float(input("Enter the price of item 1: "))
item2 = float(input("Enter the price of item 2: "))
item3 = float(input("Enter the price of item 3: "))

# Calculate total cost
total = item1 + item2 + item3

# Apply 10% discount if total exceeds $50
if total > 50:
    discount = total * 0.10
    final_amount = total - discount
else:
    final_amount = total

# Display the final payable amount
print("Final payable amount: $", final_amount)
