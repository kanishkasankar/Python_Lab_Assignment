# Mini Project: Bill Generator
items = []
total = 0

print("===== BILL GENERATOR =====")
while True:
    name = input("Enter item name (or 'done' to finish): ")
    if name.lower() == "done":
        break
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))
    amount = price * quantity
    items.append((name, price, quantity, amount))
    total += amount

print("\\n--------- BILL ---------")
for name, price, quantity, amount in items:
    print(f"{name} | {price:.2f} x {quantity} = {amount:.2f}")
print("-----------------------")
print(f"Total amount: ₹{total:.2f}")
print("Thank you!")
