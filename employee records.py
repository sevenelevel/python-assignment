blocked_ids = [101, 102, 103, 104]
emp_id = int(input("Enter employee ID: "))

# Check if item does NOT exist inside the list
if emp_id not in blocked_ids:
    print("Access Granted: Valid Employee.")
else:
    print("Access Denied: ID is blocked.")