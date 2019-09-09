from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#constant Variables
maxValue = 50000
simulationTimes = [int(index) for index in range(200, 50001, 200)]

filesTop = ["../semAcostamento/lc2013/50000/detectorTop.xml", "../comAcostamento/lc2013/50000/detectorTop.xml"]
filesmid = ["../semAcostamento/lc2013/50000/detectormid.xml", "../comAcostamento/lc2013/50000/detectormid.xml"]
fileBot = "../comAcostamento/lc2013/50000/detectorBot.xml"
soupsTop = []
soupsmid = []

soupBot = BeautifulSoup ( open (fileBot, "r"), "lxml" )

#creating soups
for fileName in filesTop:
    fp = open(fileName, "r")
    soup = BeautifulSoup(fp, "lxml")
    soupsTop.append(soup)

for fileName in filesmid:
    fp = open(fileName, "r")
    soup = BeautifulSoup(fp, "lxml")
    soupsmid.append(soup)

#TOP LANE
##Getting data
dictTop = {'Sem Acostamento': [], 'Com Acostamento': []}
index = 200
for soup in soupsTop:
    
    #Getting the values in each file
    for interval in soup.find_all ('interval'):
        if(index <= maxValue): #first file
            meanTimeValues = dictTop['Sem Acostamento']
            meanTimeValues.append (interval.get ('meantraveltime'))
            dictTop['Sem Acostamento'] = meanTimeValues
        else: #second file
            meanTimeValues = dictTop['Com Acostamento']
            meanTimeValues.append (interval.get ('meantraveltime'))
            dictTop['Com Acostamento'] = meanTimeValues

        index += 200

#MID LANE
##Getting data
dictmid = {'Sem Acostamento': [], 'Com Acostamento': []}
index = 200
for soup in soupsmid:

    for interval in soup.find_all ('interval'):
        if(index <= maxValue): #first file
            meanTimeValues = dictmid['Sem Acostamento']
            meanTimeValues.append (interval.get ('meantraveltime'))
            dictmid['Sem Acostamento'] = meanTimeValues
        else: #second file
            meanTimeValues = dictmid['Com Acostamento']
            meanTimeValues.append (interval.get ('meantraveltime'))
            dictmid['Com Acostamento'] = meanTimeValues

        index += 200

#BOT LANE
##Getting data
dictBot = {'Sem Acostamento: CIMA': [], 'Sem Acostamento: BAIXO': [], 'Faixa do Acostamento': []}
dictBot['Sem Acostamento: CIMA'] = dictTop['Sem Acostamento']
dictBot['Sem Acostamento: BAIXO'] = dictmid['Sem Acostamento']

for interval in soupBot.find_all ('interval'):
    meanTimeValues = dictBot['Faixa do Acostamento']
    meanTimeValues.append(interval.get ('meantraveltime'))
    dictBot['Faixa do Acostamento'] = meanTimeValues


dataFrame = pd.DataFrame(dictBot, index=simulationTimes)
# print (dataFrame)

dataFrame = dataFrame.astype(float)
ax = dataFrame.plot(title="Faixa do Acostamento Comparada com as da Outra Simulação")
ax.set_xlabel("Tempo de simulação (ms)")
ax.set_ylabel("Tempo médio (ms)")
plt.show()



