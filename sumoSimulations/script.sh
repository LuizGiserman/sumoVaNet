#!/bin/bash

readonly numDirectories=4

declare -a directories=("comAcostamento" "semAcostamento") # "semAcostamento") #"comSaidas" "comSaidasEntradas" )


echo ./genFiles.py
./genFiles.py

for directory in "${directories[@]}";
do
  for value in {6020..10001..20}
  do

    echo sumo -c ./$directory/base.sumocfg -e$value --additional-files ./$directory/$value/additional$value.xml
    PROC= sumo -c ./$directory/base.sumocfg -e$value --additional-files ./$directory/$value/additional$value.xml
    echo $PROC
  done

done
