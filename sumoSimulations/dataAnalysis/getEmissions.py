from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fileComAcostamento = "../comAcostamento/lc2013/84500/emissionOutput.xml"
fileSemAcostamento = "../semAcostamento/lc2013/84500/emissionOutput.xml"


co2List = []
fuelList = []
pmList = []
noxList = []
allSteps = []
index = 0
fp = open (fileComAcostamento, "r")
soupComAcostamento = BeautifulSoup (fp, "lxml")

index = -1

auxCO2 = 0
auxFuel = 0
auxPM = 0
auxNOx = 0


for timestep in soupComAcostamento.find_all ('timestep'):
  for vehicle in timestep.find_all ('vehicle'):
    auxCO2 += vehicle.get ('co2')
    auxFuel += vehicle.get ('fuel')
    auxPM += vehicle.get('pmx')
    auxNOx += vehicle.get('nox')      
  
  co2List.append(auxCO2)
  fuelList.append(auxFuel)
  pmList.append(auxPM)
  noxList.append(auxNOx)
  index += 1
  allSteps.append(index)

test = open ("error.txt", "w")
fp.close()

stirng = "co2List len = {}\nfuelList len = {}\n pmList len = {}\n noxList len = {}\n allSteps len = {}\n".format(len(co2List), len(fuelList), len(pmList), len(noxList), len(allSteps))
test.write(stirng)
test.write(allStpes)
test.write(co2List)
test.close()
print(co2List)

dataFrame = pd.DataFrame ({'CO2':co2List}, index=allSteps)
dataFrame = dataFrame.astype (float)
ax = dataFrame.plot (title="Emissao de CO2 com Acostamento")
ax.set_xlabel ("Tempo de simulacao (s)")
ax.set_ylabel ("CO2 (mg)")
plt.save("co2Com.png")

print(fuelList)

dataFrame = pd.DataFrame ({'Fuel':fuelList}, index=allSteps)
dataFrame = dataFrame.astype (float)
ax = dataFrame.plot (title="Uso de Combustivel na Sim. com Acostamento")
ax.set_xlabel ("Tempo de simulacao (s)")
ax.set_ylabel ("Combustivel (ml)")
plt.save("fuelCom.png")

print(pmxList)

dataFrame = pd.DataFrame ({'pmx':pmList}, index=allSteps)
dataFrame = dataFrame.astype (float)
ax = dataFrame.plot (title="Emissao de PMx com Acostamento")
ax.set_xlabel ("Tempo de simulacao (s)")
ax.set_ylabel ("PMx (mg)")
plt.show()

print(noxList)

dataFrame = pd.DataFrame ({'nox':noxList}, index=allSteps)
dataFrame = dataFrame.astype (float)
ax = dataFrame.plot (title="Emissao de NOx com Acostamento")
ax.set_xlabel ("Tempo de simulacao (s)")
ax.set_ylabel ("NOx (mg)")
plt.save("noxCom.png")

