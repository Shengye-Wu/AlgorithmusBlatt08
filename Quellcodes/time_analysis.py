import numpy as np      # um zufällige arrays zu generieren
import time             # zur zeitmessung
import seaborn as sns   # zum plotten
import selection_sort as ss
import quick_sort as qs

s_times, q_times = [], []
arrar_sizes =  [10, 100, 500, 1000, 1500, 2000, 2500, 3000, 5000, 7500, 10000] # messung für verschiedenen array-längen
for size in arrar_sizes:
    # ziehe ein zufälliges array
    np.random.seed(0)
    array = np.random.randint(low=0, high=1000000, size=size)
    start = time.time()
    # hier sortieren mit selection sort - wie geht das?
    ss.selectionSort(array)
    end = time.time()
    s_times.append(end-start) # die zeit in sekunden
print(s_times)

    # und dann jetzt noch für quicksort :)
for size in arrar_sizes:
    # ziehe ein zufälliges array
    np.random.seed(0)
    array = np.random.randint(low=0, high=1000000, size=size)
    start = time.time()
    # hier sortieren mit selection sort - wie geht das?
    qs.quickSort(array)
    end = time.time()
    q_times.append(end-start) # die zeit in sekunden
print(q_times)