"""
Напишите алгоритм, который берет массив и перемещает все нули в конец, сохраняя порядок остальных элементов.
Example:
moveZeros([false,1,0,1,2,0,1,3,"a"])
// returns[false,1,1,2,1,3,"a",0,0]

"""

########################### SOLUTION 1 (My Solution) #######################################################
# def moveZeros(array):
#     new_array = []
#     zero_array = []
#     for i in array:
#         if i != 0 or i is False:
#             new_array.append(i)
#         else:
#             zero_array.append(i)
#     print(new_array + zero_array)
#
#
# moveZeros([False,1,0,1,2,0,1,3,"a"])
########################### SOLUTION 2 ######################################
# def move_zeros(array):
#     for i in array:
#         if i == 0:
#             array.remove(i)
#             array.append(i)
#     return array

# print(move_zeros([False,1,0,1,2,0,1,3,"a"]))

# print(False == 0)
########################### SOLUTION 3 #################################
# def move_zeros(a):
#     a.sort(key=lambda v: v == 0 and v is not False)
#     return a
#
# print(move_zeros([False,1,0,1,2,0,1,3,"a"]))