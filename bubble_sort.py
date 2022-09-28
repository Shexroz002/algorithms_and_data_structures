"""""
Bubble was wroten in here by Shehrozbek
26.09.2022

"""

def bubble_sort(array:list):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array
print(bubble_sort([7,8,1,88,99,3,54,555,9]))
