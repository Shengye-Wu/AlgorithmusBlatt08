import matplotlib.pyplot as plt
import numpy as np      # um zufällige arrays zu generieren
import time             # zur zeitmessung
import seaborn as sns   # zum plotten

import selection_sort as s
import quick_sort as q

q_times = []
array_sizes =  [10, 100, 500, 1000, 1500, 2000, 2500, 3000, 5000, 7500, 10000]

"""
----------------------------Laufzeit Messen--------------------------------
"""
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
------------------------Plotten zu Schätzen----------------------
"""

"""
According to O-Notation the running time is approximately T(n) = C * nlogn
Now calculate C with the data form the last group, where other polynom terms can be neglected
"""
# Quick sort
n_nlogn = array_sizes * np.array(np.log(array_sizes)) # nlogn
C =  q_times / n_nlogn[-1] # C = T(n) / nlogn
t_asympt = C * n_nlogn # T(n)_asympt = C * nlogn

x = array_sizes
y1 = q_times
y2 = t_asympt

plt.plot(x, y1 , color= "blue", linestyle='dashed', marker= "o", label= "actual time")
plt.plot(x, y2 , color= "orange", linestyle='dashed', marker= "o", label= "estimated time")
plt.xlabel("Size of the Input Array")
plt.ylabel("Running time in Seconds (quick sort)")
plt.legend()
plt.show()
