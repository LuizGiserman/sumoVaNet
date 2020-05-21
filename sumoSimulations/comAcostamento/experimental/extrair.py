from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

meanTimeLossTop = []
meanTimeLossMid = []
meanTimeLossBot = []

finalMeanTimeLossTop = []
finalMeanTimeLossMid = []
finalMeanTimeLossBot = []

sumJamLengthTop = []
sumJamLengthMid = []
sumJamLengthBot = []

finalSumJamLengthTop = []
finalSumJamLengthMid = []
finalSumJamLengthBot = []

nVehSeen = []
finalnVehSeen = []
nVehAcostamento = []
finalnVehAcostamento = []
porcentagemVeiculosAcostamento = []
#rodada z

numero_rodadas = 10
numero_configuracoes = 7
simulacao = 2
for z in range(numero_rodadas):

    dirAtual = 'simulacoes'+ str(simulacao) + '/rodada' + str(z) +'/'

    meanTimeLossBot.append([])
    meanTimeLossMid.append([])
    meanTimeLossTop.append([])

    sumJamLengthBot.append([])
    sumJamLengthMid.append([])
    sumJamLengthTop.append([])

    nVehSeen.append([])
    nVehAcostamento.append([])

    for index in range (0, numero_configuracoes):

        #bot
        file = open (dirAtual + 'laneDetBot' + str(index) + '.xml', 'r')
        soup = BeautifulSoup(file, 'lxml')
        meanTimeLossBot[z].append(float(soup.interval.get('meantimeloss')))
        sumJamLengthBot[z].append(float(soup.interval.get('jamlengthinvehiclessum')))
        nVehAcostamento[z].append(float(soup.interval.get('nvehseen')))
        nVehSeen[z].append(float(soup.interval.get('nvehseen')))
        file.close()

        #mid
        file = open (dirAtual + 'laneDetMid' + str(index) + '.xml', 'r')
        soup = BeautifulSoup(file, 'lxml')
        meanTimeLossMid[z].append(float(soup.interval.get('meantimeloss')))
        sumJamLengthMid[z].append(float(soup.interval.get('jamlengthinvehiclessum')))
        nVehSeen[z][index] += float(soup.interval.get('nvehseen'))
        file.close()

        #top
        file = open (dirAtual + 'laneDetTop' + str(index) + '.xml', 'r')
        soup = BeautifulSoup(file, 'lxml')
        meanTimeLossTop[z].append(float(soup.interval.get('meantimeloss')))
        sumJamLengthTop[z].append(float(soup.interval.get('jamlengthinvehiclessum')))
        nVehSeen[z][index] += float(soup.interval.get('nvehseen'))
        file.close()

finalMeanTimeLossBot = np.average(meanTimeLossBot, axis=0)
mtlBotstd = np.std(meanTimeLossBot, axis=0)
finalMeanTimeLossMid = np.average(meanTimeLossMid, axis=0)
mtlMidstd = np.std(meanTimeLossMid, axis=0)
finalMeanTimeLossTop = np.average(meanTimeLossTop, axis=0)
mtlTopstd = np.std(meanTimeLossTop, axis=0)

finalSumJamLengthBot = np.average(sumJamLengthBot, axis=0)
sjlBotstd = np.std (sumJamLengthBot, axis=0)
finalSumJamLengthMid = np.average(sumJamLengthMid, axis=0)
sjlMidstd = np.std (sumJamLengthMid, axis=0)
finalSumJamLengthTop = np.average(sumJamLengthTop, axis=0)
sjlTopstd = np.std (sumJamLengthTop, axis=0)

finalnVehSeen = np.average (nVehSeen, axis=0)
finalnVehAcostamento = np.average (nVehAcostamento, axis=0)

# print (finalMeanTimeLossBot)
# print (finalMeanTimeLossMid)
# print (finalMeanTimeLossTop)
# print (finalSumJamLengthBot)
# print (finalSumJamLengthMid)
# print (finalSumJamLengthTop)
# print (finalnVehSeen)
# print (finalnVehAcostamento)
for (seen, acostamento) in zip(finalnVehSeen, finalnVehAcostamento):
    porcentagemVeiculosAcostamento.append(100 * (acostamento/seen))

stdSomaTodasFaixasJL = (np.square(sjlBotstd) + np.square(sjlMidstd) + np.square(sjlTopstd))**0.5
somaTodasFaixasJL = np.add(finalSumJamLengthTop, finalSumJamLengthMid, finalSumJamLengthBot)
dictTimeLoss = {'esquerda': finalMeanTimeLossTop, 'meio': finalMeanTimeLossMid, 'acostamento': finalMeanTimeLossBot}
dictTimeLossStd = {'esquerda': mtlTopstd, 'meio':mtlMidstd, 'acostamento': mtlMidstd}

dictSumJamLength = {'esquerda': np.true_divide(finalSumJamLengthTop, 10**6), 'meio': np.true_divide(finalSumJamLengthMid, 10**6), 'acostamento': np.true_divide(finalSumJamLengthBot, 10**6)}
dictSumJamLengthStd = {'esquerda': np.true_divide(sjlTopstd, 10**6), 'meio': np.true_divide(sjlMidstd, 10**6), 'acostamento': np.true_divide(sjlBotstd, 10**6)}

dataFrameTimeLoss = pd.DataFrame (dictTimeLoss, index=porcentagemVeiculosAcostamento)
dataFrameJamLength = pd.DataFrame (dictSumJamLength, index=porcentagemVeiculosAcostamento)

dataFrameTimeLoss = dataFrameTimeLoss.astype (float)
dataFrameJamLength = dataFrameJamLength.astype (float)

product = []

for p1, p2 in zip (finalnVehAcostamento, finalMeanTimeLossBot):
    product.append(p1*p2)

print (finalnVehAcostamento)
print (porcentagemVeiculosAcostamento)
ax = dataFrameTimeLoss.plot(title="Tempo médio perdido no trânsito por veículo", marker='o', yerr=dictTimeLossStd)
ax.set_xlabel("Carros que entraram no acostamento (%)")
ax.set_ylabel("Tempo médio perdido por veículo (s)")
# plt.savefig('graficos/timeLoss.eps', format='eps', dpi=1200)
plt.show()
# ax = dataFrameJamLength.plot(title="Comprimento do congestionamento", marker='o', yerr=dictSumJamLengthStd)
# # plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
# ax.set_xlabel("Carros que entraram no acostamento (%)")
# ax.set_ylabel("Somas dos comprimentos dos congestionamento (veículos * 10e6)")
# # plt.savefig('graficos/jamLength.eps', format='eps', dpi=1200)
