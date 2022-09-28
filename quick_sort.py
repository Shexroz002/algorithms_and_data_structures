"""
Quick Sort algoritm was wroten in here by Shexrozbek
27.09.2022

"""
from random import randrange

def quick_sort(array):
    if len(array)<2:
        return array
    else:
        pivot = array.pop(randrange(len(array)))
        min_array = [i for i in array if i<=pivot]
        max_array = [i for i in array if i>pivot]
        return quick_sort(min_array) + [pivot] + quick_sort(max_array)
    
if __name__ == "__main__":
    print(quick_sort([7,-5,6,9,1,75,2,55,66]))