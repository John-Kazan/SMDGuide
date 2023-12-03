#!/bin/bash

#SBATCH -N 1                                                                    
#SBATCH -n 2                                                                    
#SBATCH -p physicsgpu1,physicsgpu2                                                          
#SBATCH -q physicsgpu1                                                          
#SBATCH --gres=gpu:1                                                            
#SBATCH -t 1-00:00:00                                                               
#SBATCH -o slurm.%N.%j.out                                                      
#SBATCH -e slurm.%N.%j.err  

module load namd/2.13b1-cuda
namd2 pull.conf > pull.log 
