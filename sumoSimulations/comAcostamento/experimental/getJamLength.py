from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
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

#[cima: [valor0, ..., valor 5]]
#index = [vehAcostamento1, vehAcostamento2, vehAcostamento3]


for index in range (0, 6):

    file = open('laneDetBot' + str(index) + '.xml', 'r')
    botFiles.append(file)

    file = open('laneDetMid' + str(index) + '.xml', 'r')
    midFiles.append(file)

    file = open('laneDetTop' + str(index) + '.xml', 'r')
    topFiles.append(file)

    soup = BeautifulSoup(botFiles[index], 'lxml')
    botSoups.append(soup)
    soup = BeautifulSoup(midFiles[index], 'lxml')
    midSoups.append(soup)
    soup = BeautifulSoup(topFiles[index], 'lxml')
    topSoups.append(soup)

    somasBot.append(0)
    somasAcostamento.append(0)
    counter = 0
    for interval in botSoups[index].find_all('interval'):
        somasBot[index] += float(interval.get('jamlengthinvehiclessum'))
        somasAcostamento[index] += float(interval.get('nvehentered'))
        counter += 1

    somasBot[index] /= counter

    somasMid.append(0)
    counter = 0
    for interval in midSoups[index].find_all('interval'):
        somasMid[index] += float(interval.get('jamlengthinvehiclessum'))
        counter += 1

    somasMid[index] /= counter

    somasTop.append(0)
    counter = 0
    for interval in topSoups[index].find_all('interval'):
        somasTop[index] += float(interval.get('jamlengthinvehiclessum'))
        counter += 1
    somasTop[index] /= counter

dict = {'esquerda': somasTop, 'meio': somasMid, 'acostamento': somasBot}
dataFrame = pd.DataFrame (dict, index=somasAcostamento)
print (dict)
dataFrame = dataFrame.astype (float)
ax = dataFrame.plot(title="Relação Entre Comprimentos dos Congestionamentos e Número de Motoristas Infratores")
ax.set_xlabel("Número de carros que entraram no acostamento")
ax.set_ylabel("Soma dos comprimentos dos congestionamentos (número de veículos)")
plt.show()
