#!/bin/bash

#SBATCH -n 14


#SBATCH -t 0-4:00
#SBATCH -o slurm.%N.%j.out
#SBATCH -e slurm.%N.%j.err



module load namd/2.13-mpi
mpiexec namd2 pull.conf > pull.log 
