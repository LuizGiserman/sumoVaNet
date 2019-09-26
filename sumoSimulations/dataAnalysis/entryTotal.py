from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#comAcostamento

#simulation times
timeValues = [int(index) for index in range(20, 84001, 20)]
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
dictDeparted = {}
semDeparted = 0
comDeparted = 0
for time in timeValues:
    semDeparted, comDeparted = 0, 0

    #Getting the values in each file
    for lane in semSoup[index].find_all('lane'):
        id = lane.get('id')
        if (id == "1_0" or id == "1_1"):
            semDeparted += int(lane.get('departed'))

    for lane in comSoup[index].find_all('lane'):
        id = lane.get('id')
        if (id == "1_0" or id == "1_1"):
            comDeparted += int(lane.get('departed'))

    if (index == 0):
        dictDeparted['semAcostamento'], dictDeparted['comAcostamento'] = [semDeparted], [comDeparted]
    else:
        semAux, comAux = dictDeparted['semAcostamento'], dictDeparted['comAcostamento']
        semAux.append(semDeparted)
        comAux.append(comDeparted)
        dictDeparted['semAcostamento'], dictDeparted['comAcostamento'] = semAux, comAux

    index += 1

# print (dictDeparted)

dataFrame = pd.DataFrame(dictDeparted, index=timeValues)
print (dataFrame)

dataFrame = dataFrame.astype(float)
ax = dataFrame.plot(title="Veículos que Sairam do Enlace 2 (LC2013)")
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
#Traffic volume at the begin of the lane / edge (#/h) = 3600 * departed / period
#
# density
# waitingTime
# left
# departed
# period
