message = "Welcome to my Python Learning Journey!"
print(message)
name = input("What is your name? ")
age = int(input("How old are you? "))
print(f"Hello, {name}!")
print(f"Next year, you will be {age + 1} years old.")

# --- Problem 2: Canteen Bill Calculator ---
item_name = input("What item did you buy? ")
price = int(input("What is the price per item? "))
quantity = int(input("How many did you buy? "))

total_bill = price * quantity

print(f"You ordered {quantity} {item_name}(s).")
print(f"Your total bill to pay is: ₹{total_bill}")

# === Problem 3: Daily Study & Rrecord Tracker ===
record_hours = float(input("How many hours did you spend writing records today? "))
college_hours = float(input("How many hours did you spend in college classes? "))

total_hours = record_hours + college_hours

print(f"Great job today! You dedicated {total_hours} hours to your academics.")