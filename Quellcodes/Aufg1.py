"""
Selection Sort und Quicksort

Prinzip vom
"""

def selectionSort(array):
    """
     Selection Sort: Erstelle ein neues Array, läuft schrittweise durch
     das eingegebene Array um das kleinste Elem davon auszuwählen, löschen
     und ins neue Array hinzufügen.
     Notiert, dass in unserem Code kein neues Array erstellt ist, stattdessen
     wird die ersten Stellen [0:i] als bereits sortierten Teil betrachtet.
    :param array:
    :return:
    """
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array