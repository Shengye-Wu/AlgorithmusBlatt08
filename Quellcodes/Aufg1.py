"""
Selection Sort und Quicksort

"""

def selectionSort(array):
    """
     Traverse the given Array, pick by every step the smallest element
     and put it into the array to be returned
    :param array: the given array to be sorted
    :return: the sorted array
    """
    sortedArray = [0]*len(array) # simulate the array initialization
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        sortedArray[i] = array[min_idx]
    return sortedArray