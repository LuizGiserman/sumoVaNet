from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

length = 997.0

simulationTimes = [int(index) for index in range(200, 84501, 200)]

filesComAcostamento = ["../comAcostamento/lc2013/50000/laneDetTop.xml"]

soupsComAcostamento = []

for file in filesComAcostamento:
    fp = open (file, "r")
    soup = BeautifulSoup (fp, "lxml")
    soupsComAcostamento.append(soup)


dictComAcostamento = {'Faixa de Cima' : []}

for soup in soupsComAcostamento:
    for interval in soup.find_all ('interval'):
        meanSpeed = interval.get('meanspeed')
        meanTravelTime = length/int(meanSpeed)
        dictComAcostamento['Faixa de Cima'].append(meanTravelTime)

print (dictComAcostamento)
