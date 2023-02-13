"""
 @file task.py
 @author Federico Leonardo
 @brief finds and return the elements that are in the first list but are missing in the second.

 Sorting the lists takes O(n log n) time, the overall time complexity of this solution would be O(n log n).
"""

#Define a function that receives two lists
def missing_elements(list1, list2):
    #Sort the lists, ascending by default
    list1.sort()
    list2.sort()

    i, j = 0, 0
    missing = []
    #Iterate the lists, from start to finish
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            missing.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            j += 1
        else:
            i += 1
            j += 1

    #If the first list is longer than the second
    #We have to iterate the rest of the list and append this numbers because they don't appear in the second list
    #Remember that the list was sorted ascending 
    while i < len(list1):
        missing.append(list1[i])
        i += 1

    return missing