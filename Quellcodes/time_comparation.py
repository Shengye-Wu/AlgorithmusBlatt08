import matplotlib.pyplot as plt
import numpy as np      # um zufällige arrays zu generieren
import time             # zur zeitmessung
import seaborn as sns   # zum plotten

import selection_sort as s
import quick_sort as q

s_times, q_times = [], []
array_sizes =  [10, 100, 500, 1000, 1500, 2000, 2500, 3000, 5000, 7500, 10000]

"""
----------------------------Laufzeit Messen--------------------------------
"""

# messung für verschiedenen array-längen
for size in array_sizes:
    # ziehe ein zufälliges array
    np.random.seed(0)
    array = np.random.randint(low=0, high=1000000, size=size)
    start = time.time()
    # hier sortieren mit selection sort - wie geht das?
    s.selectionSort(array)
    end = time.time()
    s_times.append(end-start) # die zeit in sekunden
print(s_times)

    # und dann jetzt noch für quicksort :)
for size in array_sizes:
    # ziehe ein zufälliges array
    np.random.seed(0)
    array = np.random.randint(low=0, high=1000000, size=size)
    start = time.time()
    # hier sortieren mit selection sort - wie geht das?
    q.quickSort(array)
    end = time.time()
    q_times.append(end-start) # die zeit in sekunden
print(q_times)


"""
------------------------Plotten zu Vergleichen----------------------
"""
# array-sizes = [10, 100, 500, 1000, 1500, 2000, 2500, 3000, 5000, 7500, 10000]
x = array_sizes
y = s_times
z = q_times

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, color= "red", linestyle='dashed', marker= "o", label= "selection sort")
ax.set_xlabel("Size of the Input Array", fontsize = 14)
ax.set_ylabel("Running time in Seconds (selection sort)")

ax2 = ax.twinx()
ax2.plot(x, z, color= "blue", linestyle='dashed', marker= "o", label= "quick sort")
ax2.set_ylabel("Running time in Seconds (quick sort)")
fig.legend(loc=1)

plt.show()
