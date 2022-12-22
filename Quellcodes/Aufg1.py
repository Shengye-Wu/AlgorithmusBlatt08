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

array = [7,5,8,1]
array=selectionSort(array)
print(array)