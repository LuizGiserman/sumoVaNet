#!/bin/bash

echo sumo -c base.sumocfg -e22500 --additional-files additional.xml --seed $1
PROC= sumo -c base.sumocfg -e22500 --additional-files additional.xml --seed $1
echo $PROC
