price1 = float(input("Enter price of item 1 (energy drink): "))

qty1 = int(input("Enter quantity of item 1: "))



price2 = float(input("Enter price of item 2 (biscuits): "))

qty2 = int(input("Enter quantity of item 2: "))# Calculate total before and after a flat 10% discount

subtotal = (price1 * qty1) + (price2 * qty2)

discount = subtotal * 0.10

final_bill = subtotal - discount



print("Subtotal amount:", subtotal)

print("Money saved:", discount)

print("Final amount to pay:", final_bill)