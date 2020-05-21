from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

semMeanTimeLossMid = []
semMeanTimeLossTop = []

semJamLengthMid = []
semJamLengthTop = []

comMeanTimeLossBot = []
comMeanTimeLossMid = []
comMeanTimeLossTop = []

comJamLengthBot = []
comJamLengthMid = []
comJamLengthTop = []

comCo2 = []
semCo2 = []

nVehSeen = []
nVehAcostamento = []

fuelSem = []
fuelCom = []

dirSem = 'semAcostamento/uk/novo/'
dirCom = 'comAcostamento/uk/novo/'

for z in range(5):

    #sem
    file = open (dirSem + 'SAlaneDetMid' + str(z) + '.xml', 'r')
    soup = BeautifulSoup(file, 'lxml')
    semMeanTimeLossMid.append(float(soup.interval.get('meantimeloss')))
    semJamLengthMid.append(float(soup.interval.get('jamlengthinvehiclessum')))
    file.close()

    file = open (dirSem + 'SAlaneDetTop' + str(z) + '.xml', 'r')
    soup = BeautifulSoup(file, 'lxml')
    semMeanTimeLossTop.append(float(soup.interval.get('meantimeloss')))
    semJamLengthTop.append(float(soup.interval.get('jamlengthinvehiclessum')))
    file.close()

    file = open (dirSem + 'CAemissions' + str(z), 'r')
    soup = BeautifulSoup(file, 'lxml')
    semCo2.append(0)
    fuelSem.append(0)
    for lane in soup.find_all('lane'):
        semCo2[z] += float(lane.get('co2_perveh'))/10**6
        fuelSem[z] += float(lane.get('fuel_perveh'))/10**3
    #com
    file = open (dirCom + 'CAlaneDetBot' + str(z) + '.xml', 'r')
    soup = BeautifulSoup(file, 'lxml')
    comMeanTimeLossBot.append(float(soup.interval.get('meantimeloss')))
    comJamLengthBot.append(float(soup.interval.get('jamlengthinvehiclessum')))
    nVehSeen.append(float(soup.interval.get('nvehseen')))
    nVehAcostamento.append(float(soup.interval.get('nvehseen')))
    file.close()

    file = open (dirCom + 'CAlaneDetMid' + str(z) + '.xml', 'r')
    soup = BeautifulSoup(file, 'lxml')
    comMeanTimeLossMid.append(float(soup.interval.get('meantimeloss')))
    comJamLengthMid.append(float(soup.interval.get('jamlengthinvehiclessum')))
    nVehSeen[z] += float(soup.interval.get('jamlengthinvehiclessum'))
    file.close()

    file = open (dirCom + 'CAlaneDetTop' + str(z) + '.xml', 'r')
    soup = BeautifulSoup(file, 'lxml')
    comMeanTimeLossTop.append(float(soup.interval.get('meantimeloss')))
    comJamLengthTop.append(float(soup.interval.get('jamlengthinvehiclessum')))
    nVehSeen[z] += float(soup.interval.get('jamlengthinvehiclessum'))
    file.close()

    file = open (dirCom + 'CAemissions' + str(z), 'r')
    soup = BeautifulSoup(file, 'lxml')
    comCo2.append(0)
    fuelCom.append(0)
    for lane in soup.find_all('lane'):
        comCo2[z] += float(lane.get('co2_perveh'))/10**6
        fuelCom[z] += float(lane.get('fuel_perveh'))/10**3

print (comMeanTimeLossBot)
print (comMeanTimeLossMid)
print (comMeanTimeLossTop)
print (semMeanTimeLossMid)
print (semMeanTimeLossTop)
print (comCo2)
print (semCo2)
print (nVehSeen)
print (nVehAcostamento)

porcentagem = 100*( np.average(nVehAcostamento) / np.average(nVehSeen) )
print ("Porcentagem de Veiculos que invadiram o acostamento:{}".format(porcentagem))

comSum = np.average(comMeanTimeLossBot) + np.average(comMeanTimeLossMid) + np.average(comMeanTimeLossTop)
stdComSum = (np.square(np.std(comMeanTimeLossBot)) + (np.std(comMeanTimeLossMid)**2) + (np.std(comMeanTimeLossTop)**2))**0.5
semSum = np.average(semMeanTimeLossMid) + np.average(semMeanTimeLossTop)
stdSemSum =  (np.std(semMeanTimeLossMid)**2) + (np.std(semMeanTimeLossTop)**2)**0.5

print ("\nSoma dos TimeLoss (todas as faixas)\ncomAcostamento : {:.2f}+-{:.2f}\nsemAcostamento : {:.2f}+-{:.2f}".format(comSum, stdComSum, semSum, stdComSum))
print ("\nTimeLoss por faixa:")
print ("\nX\tComAcostamento\tSemAcostamento")
print ("esquerda\t{:.2f}+-{:.2f} s\t{:.2f}+-{:.2f} s".format(np.average(comMeanTimeLossTop), np.std(comMeanTimeLossTop), np.average(semMeanTimeLossTop), np.std(semMeanTimeLossTop)))
print ("meio\t\t{:.2f}+-{:.2f} s\t{:.2f}+-{:.2f} s".format(np.average(comMeanTimeLossMid), np.std(comMeanTimeLossMid), np.average(semMeanTimeLossMid), np.std(semMeanTimeLossMid)))
print ("acostamento\t{:.2f}+-{:.2f} s\t{} s\n\n".format(np.average(comMeanTimeLossBot), np.std(comMeanTimeLossBot), 'X'))

comJLSum = np.average(comJamLengthBot) + np.average(comJamLengthMid) + np.average(comJamLengthTop)
semJLSum = np.average(semJamLengthMid) + np.average(semJamLengthTop)
print ("\nSoma dos JameLengths (todas as faixas)\ncomAcostamento : {:.2f}\nsemAcostamento : {:.2f}".format(comJLSum, semJLSum))
print ("\nJamLength por faixa:")
print ("\nX\tComAcostamento\tSemAcostamento")
print ("esquerda\t{:.2f}+-{:.2f}\t\t{:.2f}+-{:.2f}".format(np.average(comJamLengthTop), np.std(comJamLengthTop), np.average(semJamLengthTop), np.std(semJamLengthTop)))
print ("meio\t\t{:.2f}+-{:.2f}\t{:.2f}+-{:.2f}".format(np.average(comJamLengthMid), np.std(comJamLengthMid), np.average(semJamLengthMid), np.std(semJamLengthMid)))
print ("acostamento\t{:.2f}+-{:.2f}\t{}\n\n".format(np.average(comJamLengthBot), np.std(comJamLengthBot), 'X'))
print (semJamLengthMid)
comCo2Sum = np.average(comCo2)
semCo2Sum = np.average(semCo2)
print ("Emissao de Co2 comAcostamento: {:.2f}+-{:.4f} kg/s\tsemAcostamento : {:.2f}+-{:.4f} kg/s".format(comCo2Sum, np.std(comCo2), semCo2Sum, np.std(semCo2)))
fuelSemSum = np.average(fuelSem)
fuelComSum = np.average(fuelCom)
print ("Consumo de combustivel semAcostamento: {:.2f}+-{:.4f} L/s\tcomAcostamento : {:.2f}+-{:.4f} L/s".format(fuelSemSum, np.std(fuelSem), fuelComSum, np.std(fuelCom)))
