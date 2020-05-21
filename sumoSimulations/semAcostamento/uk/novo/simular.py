import random
import subprocess
import os

simulation_time = 22500

for index in range(5):

        os.remove('additional.xml')
        additional = open ('additional.xml', 'w+')
        additional.write('<additional>\n')
        additional.write('<laneAreaDetector id="top" lane="2_1" freq="'+ str(simulation_time) +'" file="SAlaneDetTop'+ str(index) +'.xml"/>\n')
        additional.write('<laneAreaDetector id="mid" lane="2_0" freq="'+ str(simulation_time) +'" file="SAlaneDetMid'+ str(index) +'.xml"/>\n')
        additional.write('\t<laneData id="mid" type="emissions" file="CAemissions'+ str(index) +'" excludeEmpty="true"/>\n')
        additional.write('</additional>\n')
        additional.close()

        seed = random.randint(10000, 99999)
        print (subprocess.call(['./sumo_script.sh',  str(seed)]))
