from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

porcentagensAcostamento = [0.0, 7.946642555905795, 12.487718062327357, 15.31861081981371, 17.421362334021385, 19.08622322823506, 24.010626771383624]

somas_co2 = []
final_co2 = []

somas_co = []
final_co = []

somas_hc = []
final_hc = []

somas_nox = []
final_nox = []

somas_pmx = []
final_pmx = []

somas_fuel = []
final_fuel = []

for z in range (0, 10):
    dirAtual = 'simulacoes2/rodada' + str(z) + '/'
    somas_co2.append([])
    somas_co.append([])
    somas_hc.append([])
    somas_nox.append([])
    somas_pmx.append([])
    somas_fuel.append([])

    for index in range (0, 7):

        file_name = dirAtual + 'emissions' + str(index)
        file = open(file_name, 'r')
        soup = BeautifulSoup(file, 'lxml')
        somas_co2[z].append(0)
        somas_co[z].append(0)
        somas_hc[z].append(0)
        somas_nox[z].append(0)
        somas_pmx[z].append(0)
        somas_fuel[z].append(0)
        for lane in soup.find_all('lane'):
            somas_co2[z][index] += float(lane.get('co2_perveh'))/(10**6)
            somas_co[z][index] += float(lane.get('co_perveh'))/(10**6)
            somas_hc[z][index] += float(lane.get('hc_perveh'))/(10**6)
            somas_nox[z][index] += float(lane.get('nox_perveh'))/(10**6)
            somas_pmx[z][index] += float(lane.get('pmx_perveh'))/(10**6)
            somas_fuel[z][index] += float(lane.get('fuel_perveh'))/(10**3)

final_co2 = np.average(somas_co2, axis=0)
std_co2 = np.std(somas_co2, axis = 0)
final_co = np.average(somas_co, axis=0)
final_hc = np.average(somas_hc, axis=0)
final_nox = np.average(somas_nox, axis = 0)
final_pmx = np.average(somas_pmx, axis = 0)
final_fuel = np.average(somas_fuel, axis=0)
std_fuel = np.std(somas_fuel, axis=0)


dict = {'CO2': final_co2, 'CO': final_co, 'HC': final_hc, 'NOx': final_nox, "PMx": final_pmx}
dict = {'CO2': final_co2}
print (dict)
dataFrame = pd.DataFrame (dict, index=porcentagensAcostamento)
dataFrame = dataFrame.astype (float)
ax = dataFrame.plot(title="Emissão de CO2 por veículo", marker='o', legend='false', yerr=std_co2)
ax.set_xlabel("Carros que entraram no acostamento (%)")
ax.set_ylabel("CO2 emitido (kg/s) ")
plt.savefig('graficos/co2.eps', format='eps', dpi=1200)

dictFuel = {'fuel': final_fuel}
dataFrame = pd.DataFrame (final_fuel, index=porcentagensAcostamento)
dataFrame = dataFrame.astype (float)
ax = dataFrame.plot(title="Consumo de combustível", marker='o', yerr=std_fuel)
ax.set_xlabel("Carros que entraram no acostamento (%)")
ax.set_ylabel("Consumo (L/s)")
plt.savefig('graficos/combustivel.eps', format='eps', dpi=1200)
