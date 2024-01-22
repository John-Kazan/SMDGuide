# Guide for Steered Molecular dynamics (SMD) simulation on ASU Sol cluster

## Initial steps with PDB

Follow the PyMOL guide here: [PyMOLGuide]

## Using VPN to connect to ASU network:

Follow the VPN guide here: [VPNGuide]

## After logging in:

`pwd` shows me home directory `/home/ikazan`

change directory to scratch space

```
cd /scratch/ikazan
```

create a new directory here by using

```
mkdir -pv testdir1
```

change directory to the new one

```
cd testdir1/
```

```
ls
```

the directory is empty

`pwd` shows me the current working directory

copy the SMD directory on github to the `/scratch/ikazan/testdir1` directory on sol. Run the command on the terminal connected to your local computer.

```
scp -r SMD ikazan@login.sol.rc.asu.edu:/scratch/ikazan/testdir1/
```

## prepare SMD

Swtich terminal window to the one connected to sol and run

```
cd SMD
```

```
cd prepare
```

From the production MD simulation copy the parameter file `WT_cript_S102Y.parm` and the last pdb file `last_prod.pdb` in to this directory.

run

```
sbatch pull_prepare.sh [62] [123 125 127] 3 0.0001 25
```

(`sbatch pull_prepare.sh <FIX> <SMD> <k> <Vel> <dis> `)

we will copy the prepared files to `required_files` directory

```
cp -v WT_cript_S102Y.parm ../required_files/
cp -v last_prod.pdb ../required_files/
cp -v WT_cript_S102Y_rest.pdb ../required_files/
cp -v WT_cript_S102Y_SMD.ref ../required_files/
```

then

```
cd ..
```

## run SMD

run 50 pulls

```
circle_run.sh 1 50
```

[PyMOLGuide]: https://github.com/John-Kazan/PyMOLGuide
[VPNGuide]: https://github.com/John-Kazan/VPNGuide
