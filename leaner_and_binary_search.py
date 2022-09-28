"""""
Leaner search and Binary was wroten in here by Shehrozbek
26.09.2022

"""

def leaner_search(list,item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return None

def binary_search(list,item):
    low = 0
    heigh = len(list)-1
    while low<heigh:
        mid=(low+heigh)//2
        result = list[mid]
        if result == item :
            return mid
        if result > item :
            heigh = mid-1
        else:
            low = mid + 1

    return None

list = [7,8,9,10,11,25,65,789,1230]
item = 11
print(leaner_search(list,item))
print(binary_search(list,item))
