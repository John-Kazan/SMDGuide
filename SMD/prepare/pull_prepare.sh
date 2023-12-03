#!/bin/bash                                                                     
                                                                                
#SBATCH -n 1                                                                   


#SBATCH -t 0-1:00                                                               
#SBATCH -o slurm.%N.%j.out                                                      
#SBATCH -e slurm.%N.%j.err

usage="""
Prepare for the pull
=====================

Description
-----------

1. Get SMD.ref which looks like pdb file but specify the pulling and fixing CA atom. In the mean time getting Force direction which will be using in .conf file.

2. Get _rest.pdb file for constructing the harmonic constraints.

3. Calculating the box size and center of mass position of _prod.pdb file.

4. Based on the boxsize and CM, Force direction, pulling speed and distance,  construct the .conf file.

5. make file structures and copy those files to folder required_files then start circle run.


Usage
-----
sbatch pull_prepare.sh <fixed_residue> <SMD_residue>


Generates: _SMD.ref, force_direction, _rest.pdb
"""

FIX=$1
SMD=$2
k=$3
Vel=$4
dis=$5


pdbfile=$(ls *prod.pdb)
name=${pdbfile%%_prod*}

python get_SMD_ref.py $pdbfile $FIX $SMD
python get_rest_pdb.py $pdbfile


module load vmd/1.9.3                                                           
xvfb-run -s '-screen 0 1400x900x24 +iglx' vmd  

vmd $pdbfile \
-e namd_box.vmd

sleep 10

python get_pullconf_1.py $name box.txt

sleep 10

python get_pullconf_2.py  $k $Vel $dis

sleep 10

cat pull_rest1.conf >> pull.conf
cat pull_rest2.conf >> pull.conf

cp  *TIP3P* pull.conf    ../required_files

cd ../
sh circle_run.sh 1 5




