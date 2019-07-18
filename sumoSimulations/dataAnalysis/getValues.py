from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#comAcostamento

#simulation times
timeValues = [int(index) for index in range(20, 10001, 20)]
#filePointers for the files
edgePointers = []
lanePointers = []
#file's soup List
#edgeSoup = []
laneSoup = []
#lane tags in a file
densities =[]
index = []

dict = {}

for time in timeValues:
    #file names
    auxEdges = "../semAcostamento/lc2013/{}/edgesOutput_{}.xml".format(time, time)
    auxLanes = "../semAcostamento/lc2013/{}/lanesOutput_{}.xml".format(time, time)
    #opening all files
    #fpEdges = open(auxEdges, "r")
    #edgePointers.append(fpEdges)
    fpLanes = open(auxLanes, "r")
    lanePointers.append(fpLanes)

#creating all of the lane soups
for fp in lanePointers:
    soup = BeautifulSoup(fp, "lxml")
    laneSoup.append(soup)

#finding every density in all of the files
dictDensities = {}
dict_wait_times = {}
for count in range(len(laneSoup)):
    densities = []
    waiting_times=[]
    for lane in laneSoup[count].find_all('lane'):
        #density value per id
        density = lane.get('density')
        wait_time = lane.get('waitingtime')
        id = lane.get('id')
        #print("{} : {}".format(id, wait_time))
        #replace None with zero
        if (density == None):
            density = 0
        if (wait_time == None):
            wait_time = 0
        #list of densities and waitingTime
        densities.append(density)
        waiting_times.append(wait_time)
        ##### creating the dict ####
        ## dict needs to be {id: [density values for that id in all files, in order],  ...} ##
        if (count == 0):
            dictDensities[str(id)] = [density]
            dict_wait_times[str(id)] = [wait_time]
        else:
            #In this tuple, both auxiliar variables turn into a list, since dict[id] is storing a list created in the if
            auxiliarDensity, auxiliar_wait_time = dictDensities[str(id)], dict_wait_times[str(id)]
            #add density and waiting time from current lane to the list
            auxiliarDensity.append(density)
            auxiliar_wait_time.append(wait_time)
            #update the dict with the updated list
            dictDensities[str(id)], dict_wait_times[str(id)] = auxiliarDensity, auxiliar_wait_time


#Dataframes
data_frame_densities = pd.DataFrame(dictDensities, index=timeValues)
data_frame_waiting_times = pd.DataFrame(dict_wait_times, index=timeValues)
#print dicts
# print("{}\n\n".format(dictDensities))
# print("{}\n\n".format(dict_wait_times))



# print(data_frame_waiting_times)
print (data_frame_densities)
# data_frame_waiting_times.'1_0' = pd.to_numeric(data_frame_waiting_times.'1_0')
#
data_frame_waiting_times = data_frame_waiting_times.astype(float)
ax = data_frame_waiting_times.plot(title='Waiting Time sem acostamento (LC2013)')
ax.set_xlabel("Tempo de simulação (ms)")
ax.set_ylabel("Waiting Time (ms)")
plt.show()
#
# print(data_frame_densities)
data_frame_densities = data_frame_densities.astype(float)
ad = data_frame_densities.plot(title='Densidade (LC2013)')
ad.set_xlabel("Tempo de simulação (ms)")
ad.set_ylabel("Densidade (veh/km)")

plt.show()

#Traffic volume at the end of the lane / edge (#/h) = 3600 * left / period
#Traffic volume at the begin of the lane / edge (#/h) = 3600 * entered / period
#
# density
# waitingTime
# left
# entered
# period
