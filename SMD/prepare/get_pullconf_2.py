#!/usr/bin/env python                                                           
"""                                                                             
Make configuration file in NAMD                                                 
================================                                                
                                                                                
Description                                                                     
------------                                                                    
Make configuration file in NAMD by extract the position of Mass Center and box    size, in the same time change the protein name.
                                                                                
Example                                                                         
--------                                                                        
python get_conf.py                                                              
                                                                                
                                                                                
"""                                                                             
                                                                                
import sys                                                                      
import os


def extract(dirfile):
    """get the direction from Force_direction"""
    data=[]
    file=open(dirfile,'r')
    data_read=file.readlines()
    for line in data_read:
        data.append(line)

    Dir=data[-1]
    return Dir
    

def makeconfigfile(k, Vel, dis):
    """make .conf file for pull"""
    outfile_name="pull_rest2.conf"
    outfile=open(outfile_name,'w')
    script="\nSMDk " + k + "\nSMDVel " + Vel + "\nSMDDir " + Dir + "\nSMDOutputFreq 1" + "\n#EXECUTION SCRIPT"+"\nrun " +str(int(float(dis)/float(Vel))) + " ;# 2ps"
    outfile.write(script)
    outfile.close()

if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("Less Input File")
        sys.exit(1)
    

    Dir=extract("Force_direction")
    k = sys.argv[1]
    Vel = sys.argv[2]    
    dis = sys.argv[3]
    
    makeconfigfile(k, Vel, dis)
















         
