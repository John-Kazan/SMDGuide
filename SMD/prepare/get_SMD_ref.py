#!/usr/bin/env python
help="""
get_SMD_ref.py
==============

Description
------------
Generates a SMD restrain file which defines the fixed atom
and the moving atom. It fixes and moves only CA atoms.

Also output the force dirction unit vector in SMD_direction file.


Input required: fixed_atom, SMD_atom, pdb_file
Example
----------
python get_SMD_ref.py <pdb_file> <fixed_residue> <SMD_residue>

Generates: SMD_ref_file, force_direction

"""


import numpy as np
import sys
import re


def CM_cal(CA,C,N):
    num_CA=len(CA)
    num_C=len(C)
    num_N=len(N)
    M = 12*(len(CA)+len(C)) + 14*len(N)
    coor = np.zeros(3)
    for i in CA:
        coor[0]+=12*i[0]
        coor[1]+=12*i[1]
        coor[2]+=12*i[2]       
    for i in C:
        coor[0]+=12*i[0]
        coor[1]+=12*i[1]
        coor[2]+=12*i[2]       
    for i in N:
        coor[0]+=14*i[0]
        coor[1]+=14*i[1]
        coor[2]+=14*i[2]

    return coor/M



def get_SMF_ref(pdb_file, fixed, SMD):
    f = open(pdb_file,'r')
    pdb = f.readlines()
    out=[]
    
    CA_SMD=[]
    N_SMD=[]
    C_SMD=[]

    CA_FIX=[]                                                              
    N_FIX=[]                                                               
    C_FIX=[]
    
    for line in pdb:
        if line[:4] == "ATOM":
            atom = line[0:6]
            atomserialnumber = int(line[6:11])
            atomname = line[12:16]
            atomname=atomname.strip()
            alternatelocationindicator = line[16:17]
            residuename = line[17:20]
            chainidentifier = line[21:22]
            chainidentifier = chainidentifier.strip()
            resnumber = line[22:26]
            resnumber=int(resnumber.strip())
            codeforinsertionofresidues = line[26:27]
            orthogonalcoordinatesforx = float(line[30:38])
            orthogonalcoordinatesfory = float(line[38:46])
            orthogonalcoordinatesforz = float(line[46:54])
            occupancy = float(line[54:60])
            bfactor = float(line[60:66])
            elementsymbol = line[76:78]
            chargeontheatom = line[78:80]

            if atomname == 'CA':
                if resnumber in fixed:
                    bfactor=1
                    occupancy=0
                    A=[orthogonalcoordinatesforx,orthogonalcoordinatesfory,orthogonalcoordinatesforz]
                    CA_FIX.append(A)
                elif resnumber in SMD:
                    occupancy=1
                    bfactor=0
                    B=[orthogonalcoordinatesforx,orthogonalcoordinatesfory,orthogonalcoordinatesforz]
                    CA_SMD.append(B)
                else:
                    bfactor = 0
                    occupancy=0
            elif atomname == 'C':          
                if resnumber in fixed:                                          
                    bfactor=1                                                   
                    occupancy=0                                                 
                    A=[orthogonalcoordinatesforx,orthogonalcoordinatesfory,orthogonalcoordinatesforz]
                    C_FIX.append(A)                                             
                elif resnumber in SMD:                                          
                    occupancy=1                                                 
                    bfactor=0                                                   
                    B=[orthogonalcoordinatesforx,orthogonalcoordinatesfory,orthogonalcoordinatesforz]
                    C_SMD.append(B)                                             
                else:                                                           
                    bfactor = 0                                                 
                    occupancy=0

            elif atomname == 'N':          
                if resnumber in fixed:                                          
                    bfactor=1                                                   
                    occupancy=0                                                 
                    A=[orthogonalcoordinatesforx,orthogonalcoordinatesfory,orthogonalcoordinatesforz]
                    N_FIX.append(A)                                             
                elif resnumber in SMD:                                          
                    occupancy=1                                                 
                    bfactor=0                                                   
                    B=[orthogonalcoordinatesforx,orthogonalcoordinatesfory,orthogonalcoordinatesforz]
                    N_SMD.append(B)                                             
                else:                                                           
                    bfactor = 0                                                 
                    occupancy=0



            else:
                bfactor = 0
                occupancy=0

            oneliner = "%-6s%5d %4s%1s%3s %1s%4s%1s   %8.3f%8.3f%8.3f%6.2f%6.2f          %2s%2s\n" % \
                (atom,
                atomserialnumber,
                atomname,
                alternatelocationindicator,
                residuename,
                chainidentifier,
                int(resnumber),
                codeforinsertionofresidues,
                orthogonalcoordinatesforx,
                orthogonalcoordinatesfory,
                orthogonalcoordinatesforz,
                occupancy,
                bfactor,
                elementsymbol,
                chargeontheatom)
            out.append(oneliner)

        else:
            out.append(line)
   
    title=re.split("/|\.",pdb_file)[-2] 
    g = open("%s_SMD.ref"%title,"w")
    g.writelines(out)
    g.close()
    
    FIX_CM=CM_cal(CA_FIX,C_FIX,N_FIX)
    SMD_CM=CM_cal(CA_SMD,C_SMD,N_SMD)
    vec=SMD_CM-FIX_CM
    np.linalg.norm(vec)
    force_dir=vec/np.linalg.norm(vec)
    f = open("Force_direction",'w')
    out="Force Dirction between %s and %s CA,C,N atoms:\n%f %f %f"%(fixed,SMD,force_dir[0],force_dir[1],force_dir[2])
    f.write(out)
    f.close()
    return


if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("Incomplete input")
        #print help
        sys.exit(1)
    else:
        pdb_file=sys.argv[1]
        fixed=eval(sys.argv[2])
        SMD=eval(sys.argv[3])
        get_SMF_ref(pdb_file, fixed, SMD)
