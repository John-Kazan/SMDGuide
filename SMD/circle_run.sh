#!/bin/bash

i=$1
n=$2
while [ $i -le $n ]
do
mkdir pull_$i
cp ./required_files/* pull_$i
cd pull_$i
sleep 1
sbatch pull_namd_CPU.sh
cd ..
i=$[$i+1]
done
