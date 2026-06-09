backlogs = int(input("Enter number of backlogs: "))
#check for zero backlogs
if backlogs == 0:
    print("Scholarship Approved")
else:
    print("Scholarship Denied: You have active backlogs.")