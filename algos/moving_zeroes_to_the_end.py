"""
Write an algorithm, which takes an array and moves all zeros to the end while keeping the order of the rest of the elements.
Example:
moveZeros([false,1,0,1,2,0,1,3,"a"])
// returns[false,1,1,2,1,3,"a",0,0]

"""

def moveZeros(array):
    new_array = []
    zero_array = []
    for i in array:
        if i != 0 or i is False:
            new_array.append(i)
        else:
            zero_array.append(i)
    print(new_array + zero_array)


moveZeros([False,1,0,1,2,0,1,3,"a"])
