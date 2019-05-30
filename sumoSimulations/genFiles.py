#! /usr/bin/python3
import os
import shutil
import subprocess
import tempfile

index = ''
directories = ['comAcostamento/']#, 'semAcostamento/'] #'comSaidas/', 'comSaidasEntradas/', ]
endValues = [int(index) for index in range(20, 6001	, 20)]

for directory in directories:
	for value in endValues:
		# Create a folder named str(value) in each simulation's dir
		# Create an additional file, considering the str(value) specifications
		# run sumo with config file, end time and additional file

		#creating value dir
		if not os.path.exists(directory + str(value)):
			os.mkdir (directory + str(value))

		#creating additional file
		f = open ('additional'+str(value)+'.xml', "w+")
		f.write('<additional>\n\t<edgeData id="myEdges" file="edgesOutput_' + str(value) + '.xml"/>\n\t<laneData id="myLanes" file="lanesOutput_' + str(value) + '.xml"/>\n</additional>')

		#moving additional file
		shutil.move('additional' + str(value) + '.xml', directory + str(value) + '/' + 'additional' + str(value) + '.xml')

		#running sumo
		#os.system("ls ./semAcostamento")
		#print('sumo ' + '-c ./' + directory + 'base.sumocfg ' + '-e' + str(value) + ' --additional-files ./'+ directory + str(value) + '/' 'additional'+str(value)+'.xml')

		#os.system ('sumo ' + '-c ./' + directory + 'base.sumocfg ' + '-e' + str(value) + ' --additional-files ./'+ directory + str(value) + '/' 'additional'+str(value)+'.xml')


# sumo -c base.sumocfg -e5000 --additional-file additional5000.xml





#<additional>
#	<edgeData id="myEdges" file="edgesOutput_5000"/>
#	<laneData id="myLanes" file="lanesOutput_5000"/>
#</additional>
