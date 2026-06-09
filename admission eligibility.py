marks = float(input("Enter your exam marks percentage: "))
clean_record = input("Do you have a clean record? (yes/no): ")

if marks >= 85 or clean_record == "yes":
    print("Admission Approved")
else:
    print("Admission Rejected")