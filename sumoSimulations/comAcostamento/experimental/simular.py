import subprocess
import os
from shutil import copyfile
import random

probabilities = [(0.9, 0.0), (0.88, 0.166), (0.86, 0.285), (0.84, 0.375), (0.82, 0.444), (0.8, 0.5), (0.7, 0.667)]
numero_rodadas = 10
#, (0.6, 0.75), (0.5, 0.8), (0.4, 0.833), (0.3, 0.857), (0.2, 0.875), (0.1, 0.888)]

for z in range (1, numero_rodadas):

    dirAtual = 'simulacoes3/rodada' + str(z) + '/'
    os.mkdir(dirAtual)

    #index + 1 !!!
    #Gera simulações do
    for index, (mr, mi) in enumerate(probabilities):
        #additional
        os.remove('additional.xml')
        additional = open ('additional.xml', 'w+')
        additional.write('<additional>\n')
        additional.write('<laneAreaDetector id="top" lane="2_2" freq="50000" file="' + dirAtual + 'laneDetTop'+ str(index) +'.xml"/>\n')
        additional.write('<laneAreaDetector id="mid" lane="2_1" freq="50000" file="' + dirAtual + 'laneDetMid'+ str(index) +'.xml"/>\n')
        additional.write('<laneAreaDetector id="bot" lane="2_0" freq="50000" file="' + dirAtual + 'laneDetBot'+ str(index) +'.xml"/>\n')
        additional.write('\t<laneData id="mid" type="emissions" file="' + dirAtual + 'emissions'+ str(index) +'" excludeEmpty="true"/>\n')
        additional.write('</additional>\n')
        additional.close()

        #base.rou.xml
        os.remove('base.rou.xml')
        f = open('base.rou.xml', 'w+')
        f.write('<routes>\n')
        f.write('\t<vType id="BadDriver" carFollowModel="IDM" accel="3" decel="3" color="1,0,0" vClass="custom1" length="4.0" minGap="2.0" stepping="1"/>\n')
        f.write('\t<vType id="GoodDriver" carFollowModel="IDM" accel="3" decel="3" color="0,0,1" vClass="custom2" length="4.0" minGap="2.0" stepping="1"/>\n')
        if (mi != 0.0):
            f.write('\t<flow id="BadSwarm" color="1,0,0" begin="0"  probability="'+ str(mi) + '" departLane="random" type="BadDriver">\n')
            f.write('\t\t<route edges="1 2 3 4"/>\n')
            f.write('\t</flow>\n')
        f.write('\t<flow id="GoodSwarm" color="0,0,1" begin="0" probability="'+ str(mr) + '" departLane="random" type="GoodDriver">\n')
        f.write('\t\t<route edges="1 2 3 4"/>\n')
        f.write('\t</flow>\n')
        f.write('</routes>\n')
        f.close()

        seed = random.randint(10000, 99999)
        print (subprocess.call(['./sumo_script.sh',  str(seed)]))
