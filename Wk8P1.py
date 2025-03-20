#Reilly Kurth
#3/18/2025
#Program 1

full_name = input("Enter a full name (first middles and last):")

name = full_name.split()

for string in name:
    print(string[0].upper(), sep= '', end='')
    print('.', sep= "", end= '')
