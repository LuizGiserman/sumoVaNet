from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

simulationTimes = [int(index) for index in range(200, 84501, 200)]

filesComAcostamento = ["../comAcostamento/lc2013/50000/detectorTop.xml", "../comAcostamento/lc2013/50000/detectorBot.xml"]
filesSemAcostamento = ["../semAcostamento/lc2013/50000/detectorTop.xml", "../semAcostamento/lc2013/50000/detectormid.xml"]

soupsComAcostamento = []
soupsSemAcostamento = []

for file in filesComAcostamento:
    fp = open(file, "r")
    soup = BeautifulSoup (fp, "lxml")
    soupsComAcostamento.append(soup)

for file in filesSemAcostamento:
    fp = open(file, "r")
    soup = BeautifulSoup (fp, "lxml")
    soupsSemAcostamento.append(soup)

dictComAcostamento = {'Faixa de cima': [], 'Faixa do acostamento' : []} #'Faixa do meio': [], 'Faixa do acostamento': []}
#comAcostamento_3_faixas
count = 0
print (len(soupsComAcostamento))
for index in range(0, len(soupsComAcostamento)):

    for interval in soupsComAcostamento[index].find_all ('interval'):

        localValue = [interval.get('meantraveltime')]
        if (index == 0):
            dictComAcostamento['Faixa de cima'].append(localValue)
        # elif (index == 1):
        #     dictComAcostamento['Faixa do meio'].append(localValue)
        elif (index == 1):
            count +=1
            dictComAcostamento['Faixa do acostamento'].append(localValue)
print (dictComAcostamento)
print(len(simulationTimes))
# dataFrame = pd.DataFrame(dictComAcostamento, index=simulationTimes)
# print(count)
# dataFrame = dataFrame.astype (float)
# ax = dataFrame.plot(title="Simulação sem acostamento")
# ax.set_xlabel("Tempo de simulação (ms)")
# ax.set_ylabel("Tempo médio (ms)")
# plt.show()
