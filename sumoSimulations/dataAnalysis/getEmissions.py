from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fileComAcostamento = "../comAcostamento/lc2013/84500/emissionOutput.xml"
fileSemAcostamento = "../semAcostamento/lc2013/84500/emissionOutput.xml"


co2List = []
fuelList = []

fp = open (fileComAcostamento, "r")
soupComAcostamento = BeautifulSoup (fp, "lxml-xml")
# fp = open (fileSemAcostamento, "r")
# soupSemAcostamento = BeautifulSoup (fp, "lxml")

for timestep in soupComAcostamento.find_all ('timestep'):
    auxCO2 = 0
    auxFUel = 0
    for vehicle in timestep.find_all ('vehicles'):
        auxCO2 = vehicle.get ('co2')
        auxFuel = vehicle.get ('fuel')
    co2List.append(auxCO2)
    fuelList.append(auxFuel)

print (co2List)
