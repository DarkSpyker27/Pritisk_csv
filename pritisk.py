import numpy as np
import matplotlib.pyplot as plt
import csv
import matplotlib.patches as mpatches
import pandas as pd
from datetime import datetime
from tabulate import tabulate

def substring_after(s, delim):
    return s.partition(delim)[-1]

sistoicni = []
hiperstoicni = []
prevlkiTlak = []
dates = []
 
file = open("test.csv", "r")
data = list(csv.DictReader(file, delimiter=";"))
file.close()

##data["date"] = pd.to_datetime(data["date"])
sistoicni = [int(row["Sistoicni"]) for row in data]
hiperstoicni = [int(row["Hiperstoicni"]) for row in data]

for x in sistoicni:
    if x >= 140:
        prevlkiTlak.append(x)

print(prevlkiTlak)

date = [str(row['date']) for row in data]

for i in range(len(date)):
    dates.append(date[i].split(".11.2022")[0])
 
dnevi = [eval(i) for i in dates]

plt.rcParams["figure.figsize"] = [10, 5]
plt.rcParams["figure.autolayout"] = True
plt.grid(True)
plt.title("Diastolični tlak-Aleks_Brenčič")
dan_sistoicni = range(len(dnevi))
plt.plot(sistoicni,'g-o', label = 'sistoicni')
plt.xticks(dan_sistoicni, dnevi)
plt.axhline(y=140, c='red', linestyle='dashed', label="Upperlimit")
plt.legend()
plt.rcParams["figure.figsize"] = (10,5)
plt.xlabel('Dnevi')
plt.ylabel('sistoicni')

fig2 = plt.figure("Figure 2")
plt.grid(True)
plt.title("Hiperstoicni tlak-Aleks_Brenčič")
dan = range(len(dnevi))
plt.plot(dan,hiperstoicni,'g-o', label = 'hiperstoicni')
plt.xticks(dan, dnevi)
plt.axhline(y=85, c='red', linestyle='dashed', label="Upperlimit")
plt.legend()
plt.rcParams["figure.figsize"] = (10,5)
plt.xlabel('Dnevi')
plt.ylabel('Hiperstoicni')
plt.show()
