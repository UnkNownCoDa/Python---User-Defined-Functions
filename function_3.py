#a program to swap every element which is a multiple of 7 with the next element in a tuple

def swap_7(info):
    data = list(info)
    check = 1
    
    for i in range(0, len(data)-1, 1):
        if data[i] % 7 == 0 and check == 1:
            data[i], data[i+1] = data[i+1], data[i]
            check = 0
        else:
            check = 1
        
    if data[-1] % 7 == 0 and check == 1:
        data[0], data[-1] = data[-1], data[0]

    return tuple(data)    

data = eval(input("Enter elements: "))
swappedData = swap_7(data)
print(swappedData)