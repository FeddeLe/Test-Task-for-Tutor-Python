"""
 @file task_2.py
 @author Federico Leonardo
 @brief Removes zeros from the array preserving the order
"""
def remove_zeros(arr):
    next_non_zero = 0
    #Iterate the array searching for the non-zero element
    #If the element is non zero then swap and increment the position
    #The zeros in the array will be in the right of the array so we return the array from start to the next_non_zero position
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[next_non_zero], arr[i] = arr[i], arr[next_non_zero]
            next_non_zero += 1
    return arr[:next_non_zero]