#Reilly Kurth
#3/19/2025
#program 5

course_info = {}

while True:
    course_ID = input("Enter course ID (or type STOP to finish): ")
    if course_ID == "STOP":
        break
    course_name = input(f"Enter course name for {course_ID}: ")
    course_info[course_ID] = course_name

subject = input("Enter a subject to search for (like COS): ")

found = False
for course_ID, course_name in course_info.items():
    if course_ID.startswith(subject):
        print(f"{course_ID}: {course_name}")
        found = True
if not found:
    print(f"No course found for subject: {subject}")



