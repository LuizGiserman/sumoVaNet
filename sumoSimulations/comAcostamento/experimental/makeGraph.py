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
totalnVehSim = []

for index in range (1, 7):

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
    totalnVehSim.append(0)
    for intervals in botSoups[index-1].find_all ('interval'):
        if(index != 6):
            somasBot[index-1] += float(intervals.get('meantimeloss'))
            somasAcostamento[index-1] += float(intervals.get('nvehentered'))
            totalnVehSim[index-1] += float(intervals.get('nvehentered'))
			

    somasMid.append(0)

    for intervals in midSoups[index-1].find_all ('interval'):
        somasMid[index-1] += float(intervals.get('meantimeloss'))
        totalnVehSim[index-1] += float(intervals.get('nvehentered'))

    somasTop.append(0)

    for intervals in topSoups[index-1].find_all ('interval'):
        somasTop[index-1] += float(intervals.get('meantimeloss'))
        totalnVehSim[index-1] += float(intervals.get('nvehentered'))
 #somasX eh o tempo perdido total na simulacao toda na faixa X.


print ("\nSomasCima(h):")
print ('[', end='')
for index in range(1, 7):
    if (index != 6):
        print ('{0:.2f}'.format(somasTop[index-1] / 3600), end=',')
    else:
        print ('] | Simulacao com todos os veículos sendo comportados: [ {0:.2f} ]'.format(somasTop[index-1] / 3600))

print ("SomasMeio(h):")
print ('[', end='')
for index in range(1, 7):
    if (index != 6):
        print ('{0:.2f}'.format(somasMid[index-1] / 3600), end=',')
    else:
        print ('] | Simulacao com todos os veículos sendo comportados: [ {0:.2f} ]'.format(somasMid[index-1] / 3600))

print ("SomasAcostamento(h):")
print ('[', end='')
for index in range(1, 7):
    if (index != 6):
        print ('{0:.2f}'.format(somasBot[index-1] / 3600), end=',')
    else:
        print ('] | Simulacao com todos os veículos sendo comportados: [ {0:.2f} ]'.format(somasBot[index-1] / 3600))

print ('\nnVeh no Acostamento:')
print (somasAcostamento)

somasTot = []
for index in range (1, 7):
    somasTot.append(somasTop[index-1] + somasBot[index-1] + somasMid[index-1])


print ("\n\nSomas Todas as Faixas(h):")
print ('[', end='')
for index in range(1, 7):
    if (index != 6):
        print ('{0:.2f}'.format(somasTot[index-1] / 3600), end=',')
    else:
        print ('] | Simulacao com todos os veículos sendo comportados: [ {0:.2f} ]'.format(somasTot[index-1] / 3600))
print ('Num Veh total:')
print (totalnVehSim)

somasTotaux = []
somasTotaux.append(somasTot[-1])
somasTotaux += somasTot[0:-1]
somasTot = somasTotaux

somasBotaux = []
somasBotaux.append(somasBot[-1])
somasBotaux += somasBot[0:-1]
somasBot = somasBotaux

somasAcostamentoaux = []
somasAcostamentoaux.append(somasAcostamento[-1])
somasAcostamentoaux += somasAcostamento[0:-1]
somasAcostamento = somasAcostamentoaux

somasTopaux = []
somasTopaux.append(somasTop[-1])
somasTopaux += somasTop[0:-1]
somasTop = somasTopaux

somasMidaux = []
somasMidaux.append(somasMid[-1])
somasMidaux += somasMid[0:-1]
somasMid = somasMidaux


print ("\n\nSomas Todas as Faixas(h):")
print ('[', end='')
for index in range(1, 7):
    print ('{0:.2f}'.format(somasTot[index-1] / 3600), end=',')

dict = {'somasTudo':somasTot, 'cima':somasTop, 'meio':somasMid, 'acostamento':somasBot}
dataFrame = pd.DataFrame (dict, index=somasAcostamento)
print(dataFrame)
dataFrame = dataFrame.astype (float)
ax = dataFrame.plot(title="Relação Entre Tempo Perdido e Numero de Motoristas Infratores")
ax.set_xlabel("Quantidade de carros que entraram no acostamento")
ax.set_ylabel("Tempo perdido no trânsito (s)")
plt.show()
