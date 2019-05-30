from bs4 import BeautifulSoup

#comAcostamento

#simulation times
timeValues = [int(index) for index in range(20, 6001, 20)]
#filePointers for the files
edgePointers = []
lanePointers = []
#file's soup List
edgeSoup = []
laneSoup = []

for time in timeValues:
    #file names
    auxEdges = "../comAcostamento/{}/edgesOutput_{}.xml".format(time, time)
    auxLanes = "../comAcostamento/{}/lanesOutput_{}.xml".format(time, time)
    #opening all files
    fpEdges = open(auxEdges, "r")
    edgePointers.append(fpEdges)
    fpLanes = open(auxLanes, "r")
    lanePointers.append(fpLanes)

for fp in edgePointers:
    soup = BeautifulSoup(fp, "lxml")
    edgeSoup.append(soup)

print(edgeSoup[299].prettify())




#
