# Input marks for 3 subjects out of 100
marks1 = float(input("Enter marks for Math out of 100: "))
marks2 = float(input("Enter marks for biology out of 100: "))
marks3 = float(input("Enter marks for chemistry out of 100: "))

# Calculate total, average, and percentage
total = marks1 + marks2 + marks3
average = total / 3
percentage = (total / 300) * 100

# Print results
print("Total Marks:", total)
print("Average Marks:", average)
print("Percentage:", percentage)