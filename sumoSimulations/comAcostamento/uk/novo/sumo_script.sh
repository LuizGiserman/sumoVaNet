#!/bin/bash

echo sumo -c base.sumocfg -e 22500 --additional-files additional.xml --seed $1
PROC= sumo -c base.sumocfg -e 22500 --additional-files additional.xml --seed $1
echo $PROC
