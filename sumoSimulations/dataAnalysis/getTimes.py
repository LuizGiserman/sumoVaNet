from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

length = 997.0

simulationTimes = [int(index) for index in range(200, 50001, 200)]

filesComAcostamento = ["../comAcostamento/lc2013/50000/laneDetTop.xml", "../comAcostamento/lc2013/50000/laneDetMid.xml", "../comAcostamento/lc2013/50000/laneDetBot.xml"]
filesSemAcostamento = ["../semAcostamento/lc2013/50000/laneDetTop.xml", "../semAcostamento/lc2013/50000/laneDetMid.xml"]

soupsComAcostamento = []
soupsSemAcostamento = []

for file in filesComAcostamento:
    fp = open (file, "r")
    soup = BeautifulSoup (fp, "lxml")
    soupsComAcostamento.append(soup)

for file in filesSemAcostamento:
    fp = open (file, "r")
    soup = BeautifulSoup (fp, "lxml")
    soupsSemAcostamento.append(soup)


dictComAcostamento = {'(com)Faixa de cima' : [], '(com)Faixa do meio': [], '(com)Faixa do acostamento': []}

for index in range(0, len(soupsComAcostamento)):
    for interval in soupsComAcostamento[index].find_all ('interval'):
        meanSpeed = interval.get('meanspeed')
        meanTravelTime = length/(60 * float(meanSpeed))
        if(index == 0):
            dictComAcostamento['(com)Faixa de cima'].append(meanTravelTime)
        elif(index == 1):
            dictComAcostamento['(com)Faixa do meio'].append(meanTravelTime)

        elif (index == 2):
            dictComAcostamento['(com)Faixa do acostamento'].append(meanTravelTime)

dictSemAcostamento = {'(sem)Faixa de cima' : [], '(sem)Faixa de baixo': []}

for index in range(0, len(soupsSemAcostamento)):
    for interval in soupsSemAcostamento[index].find_all ('interval'):
        meanSpeed = interval.get('meanspeed')
        meanTravelTime = length/(60*float(meanSpeed))
        if(index == 0):
            dictSemAcostamento['(sem)Faixa de cima'].append(meanTravelTime)
        elif(index == 1):
            dictSemAcostamento['(sem)Faixa de baixo'].append(meanTravelTime)
dictDosDois = {**dictComAcostamento, **dictSemAcostamento}
print (dictDosDois)

# print (dictSemAcostamento)
# print (len(dictSemAcostamento['Faixa de cima']))
# print (len(simulationTimes))
dataFrame = pd.DataFrame(dictDosDois, index=simulationTimes)
dataFrame = dataFrame.astype (float)
ax = dataFrame.plot(title="Simulação sem acostamento", color=[(1, 0.6, 0.2), (0.7, 0.6, 0.2), (0.7, 0.3, 0.1), (0.2, 0.60, 0.07), (0.2, 0.40, 0.07)])
ax.set_xlabel("Tempo de simulação (ms)")
ax.set_ylabel("Tempo médio (m)")
plt.show()
