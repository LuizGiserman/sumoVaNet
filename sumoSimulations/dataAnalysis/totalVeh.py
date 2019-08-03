from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#comAcostamento

#simulation times
timeValues = [int(index) for index in range(20, 10001, 20)]
#filePointers for the files
semPointers = []
comPointers = []
#file's soup List
#edgeSoup = []
semSoup = []
comSoup = []
#lane tags in a file
densities =[]
index = []

dict = {}

for time in timeValues:
    #file names
    semAcostamento = "../semAcostamento/lc2013/{}/lanesOutput_{}.xml".format(time, time)
    comAcostamento = "../comAcostamento/lc2013/{}/lanesOutput_{}.xml".format(time, time)
    #opening all files
    #fpEdges = open(auxEdges, "r")
    #edgePointers.append(fpEdges)
    fpSem = open(semAcostamento, "r")
    fpCom = open(comAcostamento, "r")

    semPointers.append(fpSem)
    comPointers.append(fpCom)

#creating all of the lane soups
for fp in semPointers:
    soup = BeautifulSoup(fp, "lxml")
    semSoup.append(soup)

for fp in comPointers:
    soup = BeautifulSoup(fp, "lxml")
    comSoup.append(soup)


index = 0
dictArrived = {}
semArrived = 0
comArrived = 0
for time in timeValues:
    semArrived, comArrived = 0, 0

    #Getting the values in each file
    for lane in semSoup[index].find_all('lane'):
        arrived = lane.get('arrived')
        if (arrived != '0'):
            semArrived += int(arrived)

    for lane in comSoup[index].find_all('lane'):
        arrived = lane.get('arrived')
        if (arrived != '0'):
            comArrived += int(arrived)

    if (index == 0):
        dictArrived['semAcostamento'], dictArrived['comAcostamento'] = [semArrived], [comArrived]
    else:
        semAux, comAux = dictArrived['semAcostamento'], dictArrived['comAcostamento']
        semAux.append(semArrived)
        comAux.append(comArrived)
        dictArrived['semAcostamento'], dictArrived['comAcostamento'] = semAux, comAux

    index += 1

# print (dictArrived)

dataFrame = pd.DataFrame(dictArrived, index=timeValues)
print (dataFrame)

dataFrame = dataFrame.astype(float)
ax = dataFrame.plot(title="Veículos que Concluíram o Percurso (LC2013)")
ax.set_xlabel("Tempo de simulação (ms)")
ax.set_ylabel("Número de veículos")
plt.show()

# data_frame_waiting_times = data_frame_waiting_times.astype(float)
# ax = data_frame_waiting_times.plot(title='Waiting Time sem acostamento (LC2013)')
# ax.set_xlabel("Tempo de simulação (ms)")
# ax.set_ylabel("Waiting Time (ms)")
# plt.show()

# ad.set_xlabel("Tempo de simulação (ms)")
# ad.set_ylabel("Densidade (veh/km)")

# plt.show()

#Traffic volume at the end of the lane / edge (#/h) = 3600 * left / period
#Traffic volume at the begin of the lane / edge (#/h) = 3600 * entered / period
#
# density
# waitingTime
# left
# entered
# period
