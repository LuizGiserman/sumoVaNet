from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#comAcostamento

#simulation times
timeValues = [int(index) for index in range(20, 6001, 20)]
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
    auxEdges = "../comAcostamento/{}/edgesOutput_{}.xml".format(time, time)
    auxLanes = "../semAcostamento/{}/lanesOutput_{}.xml".format(time, time)
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
dataFrame = pd.DataFrame()
s = pd.Series()
dictLocal = {}
for count in range(len(laneSoup)):
    densities = []
    ids = []
    for lane in laneSoup[count].find_all('lane'):
        #density value per id
        density = lane.get('density')
        id = lane.get('id')
        #replace None with zero
        if (density == None):
            density = 0
        #list of densities and ids
        densities.append(density)
        ids.append(id)
        ##### creating the dict ####
        ## dict needs to be of type {id: list of density values for that id in all files, in order, ...} ##
        if (count == 0):
            aux = [density]
            dictLocal[str(id)] = aux
        else:
            auxiliar = dictLocal[str(id)]
            #add density from current lane to the list
            auxiliar.append(density)
            #update the dict with the updated list
            dictLocal[str(id)] = auxiliar


#dataFrame
dataFrame = pd.DataFrame(dictLocal, index=timeValues)

#print dict
print("{}\n\n".format(dictLocal))





#dataFrame.replace({None : 0}, inplace=True)
print(dataFrame)
dataFrame = dataFrame.astype(float)
ax = dataFrame.plot(title='Densidade')
ax.set_xlabel("Tempo de simulação (ms)")
ax.set_ylabel("Densidade (veh/km)")
plt.show()



#Traffic volume at the end of the lane / edge (#/h) = 3600 * left / period
#Traffic volume at the begin of the lane / edge (#/h) = 3600 * entered / period
#
# density
# waitingTime
# left
# entered
# period
