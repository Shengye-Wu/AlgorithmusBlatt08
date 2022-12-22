"""
Aufg 1: Selection Sort und Quicksort implementieren
"""
def selectionSort(array):
    """
     Traverse by every step the unsorted part of the given Array,
     pick the smallest element and put it into the sorted part
    :param array: the given array to be sorted
    :return: the sorted array
    """
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

def quickSort(array):
    if len(array) <= 1:
        # Start of Recursion: singleton array is sorted
        return array
    pivot = array[0]
    # Take the first number of the array as the pivot value
    llist, mlist, rlist = [], [], []
    # Define empty lists to store elements greater than/less than/equal to the base value
    for i in range(0, len(array)):
        # Traverse the array and categorize the elements into three parts
        if array[i] < pivot:
            llist.append(array[i])
        elif array[i] > pivot:
            rlist.append(array[i])
        else:
            mlist.append(array[i])
    return quickSort(llist) + mlist + quickSort(rlist) # Recursive call: put all sorted parts together
