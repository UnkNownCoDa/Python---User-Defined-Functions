#program to display only those words that begin with 'a' or 'A' in a string using user defined functions

#creating user defined function
def displayStr(string):
    for i in string.split(): #splitting the words 
        if i[0] == 'a' or i[0] == 'A': #checking the first element
            print(i)

#getting data from user
data = input("Enter string: ")

#calling the function
displayStr(data)