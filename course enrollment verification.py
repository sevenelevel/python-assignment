available_courses = ["java", "python", "web design"]
choice = input("Enter course to join: ")

if choice in available_courses:
    print("Enrollment successful!")
else:
    print("Course not  available.")