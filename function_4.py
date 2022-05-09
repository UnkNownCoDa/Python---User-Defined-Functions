#a program to store roll and name of n students of a class and display roll of all those students whose names
#are written in all capital letters

#creating user defined function
def displayRoll(data):
    for i in data:
        if i.isupper(): #checking if the name of student is in all caps
            print(data[i])


#getting input from user
students = {}
size = int(input("Enter number of students: "))
for i in range(0, size, 1):
    name = input("Enter name of student: ")
    roll = int(input("Enter roll no of student:"))
    students[name] = roll

#calling user defined function
displayRoll(students)