from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

botFiles = []
midFiles = []
topFiles = []

botSoups = []
midSoups = []
topSoups = []

somasBot = []
somasMid = []
somasTop = []
somasAcostamento = []

for index in range (1, 6):

    file = open('laneDetBot' + str(index) + '.xml', 'r')
    botFiles.append(file)

    file = open('laneDetMid' + str(index) + '.xml', 'r')
    midFiles.append(file)

    file = open('laneDetTop' + str(index) + '.xml', 'r')
    topFiles.append(file)

    soup = BeautifulSoup(botFiles[index-1], 'lxml')
    botSoups.append(soup)
    soup = BeautifulSoup(midFiles[index-1], 'lxml')
    midSoups.append(soup)
    soup = BeautifulSoup(topFiles[index-1], 'lxml')
    topSoups.append(soup)

    somasBot.append(0)
    somasAcostamento.append(0)
    for intervals in botSoups[index-1].find_all ('interval'):
        somasBot[index-1] += float(intervals.get('meantimeloss'))
        somasAcostamento[index-1] += float(intervals.get('nvehentered'))

    somasMid.append(0)

    for intervals in midSoups[index-1].find_all ('interval'):
        somasMid[index-1] += float(intervals.get('meantimeloss'))

    somasTop.append(0)

    for intervals in topSoups[index-1].find_all ('interval'):
        somasTop[index-1] += float(intervals.get('meantimeloss'))

print (somasTop)
print (somasMid)
print (somasBot)
print (somasAcostamento)

dict = {'cima':somasTop, 'meio':somasMid, 'acostamento':somasBot}
dataFrame = pd.DataFrame (dict, index=somasAcostamento)
print(dataFrame)
dataFrame = dataFrame.astype (float)
ax = dataFrame.plot(title="Relação Entre Tempo Perdido e Numero de Motoristas Infratores")
ax.set_xlabel("Quantidade de carros que entraram no acostamento")
ax.set_ylabel("Tempo perdido no trânsito")
plt.show()
