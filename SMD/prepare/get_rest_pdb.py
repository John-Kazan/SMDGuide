#!/usr/bin/env python

help="""
get_rest_pdb.py
================

Generates a pdb file which define a constraints on the CA atome of the residue only on the protein.

Usage
------
python <pdbfile>

"""

import numpy as np
import sys
import re

def get_rest_pdb(pdb_file):
    f = open(pdb_file,'r')
    pdb = f.readlines()
    out=[]
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

            if (resnumber <= 118) and (atomname == 'CA'):
                bfactor=7
            else:
                bfactor=0
            oneliner = "%-6s%5d  %-3s%1s%3s %1s%4s%1s   %8.3f%8.3f%8.3f%6.2f%6.2f          %2s%2s\n" % \
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
    g = open("%s_rest.pdb"%title,"w")                                            
    g.writelines(out)                                                           
    g.close()


if __name__ == "__main__":
    
    if len(sys.argv) < 1:
        print("Incomplete input")
        #print help
        sys.exit(1)
    else:
        pdb_file=sys.argv[1]
        get_rest_pdb(pdb_file)







