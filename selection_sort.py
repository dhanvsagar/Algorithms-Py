
"""
Selection Sort
Set first element as min, compare to other elements
if its lesser, swap and continue
"""

def sort(list):
    for i in range(len(list)):
        min = i
        for j in range(i, len(list)):
            if list[j] < list[i]:
                min = j
                tmp = list[j]
                list[j] = list[i]
                list[i] = tmp
        print(list)
    return list


a = [11, 2, 1, 1024, 999, 3, 11, 32, 3, 12, 4]
print(sort(a))