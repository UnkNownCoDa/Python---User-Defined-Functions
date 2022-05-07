#A program to find frequency of an element in a list using user defined functions

#creating user defined function
def freq(List, element):
    count = 0
    for i in List:
        if i == element:
            count += 1
    return count

#getting user input
data = []
size = int(input("Enter size of list: "))
for i in range(0, size, 1):
    temp = input("Enter element: ")
    data.append(temp)

#getting element of needed frequency 
search = input("Enter element of needed frequency: ")

#calling user defined function and printing result
print(freq(data, search))


