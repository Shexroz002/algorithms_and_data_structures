
def selection_sort(list):
    new_list = []
    while len(list) !=0:
        print(list[0])
        max_value = list[0]
        for i in range(len(list)):
            if max_value < list[i]:
                max_value = list[i]
        list.remove(max_value)
        new_list.append(max_value)
    return new_list
list = [77,88,5,44,64,87,-5,-97,7702,0, 4]
print(selection_sort(list))