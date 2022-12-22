import matplotlib.pyplot as plt
import numpy as np      # um zufällige arrays zu generieren
import time             # zur zeitmessung
import quick_sort as q

# Laufzeit in C: Siehe Screenshot time_in_c.png
# Unit: ms, correspond to array_sizes
c_times_ms = [0.0006,0.0055,0.0332,0.0715,0.0977,0.1478,0.4277,0.1938,0.3188,0.4607,0.6547]
c_times = [x / 1000 for x in c_times_ms]
array_sizes =  [10, 100, 500, 1000, 1500, 2000, 2500, 3000, 5000, 7500, 10000]
q_times = []
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

x = array_sizes
y1 = q_times
y2 = c_times

plt.plot(x, y1 , color= "blue", linestyle='dashed', marker= "o", label= "python quicksort time (s)")
plt.plot(x, y2 , color= "orange", linestyle='dashed', marker= "o", label= "c quicksort time (s)")
plt.xlabel("Size of the Input Array")
plt.ylabel("Running time in Seconds")
plt.legend()
plt.show()

