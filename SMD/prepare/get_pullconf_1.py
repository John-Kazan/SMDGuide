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


def extract(boxfile):
    """get all the parameters from box.txt"""
    data=[]
    file=open(boxfile,'r')
    data_read=file.readlines()
    for line in data_read:
        line=line.strip()
        line=line.split()
        data.append(line)

    box={"c_x":data[1][0],"c_y":data[1][1],"c_z":data[1][2],"x":data[3][0],"y":data[3][1],"z":data[3][2]}
    
    return box



def makeconfigfile(name,data,temp):
    """makes .conf file for NAMD"""
    c_x=data['c_x']
    c_y=data['c_y']
    c_z=data['c_z']
    x=data['x']
    y=data['y']
    z=data['z']
    outfile_name="pull.conf"
    outfile=open(outfile_name,'w')
    script="#MY SETTING\n"+"set name          "+name+"\nset stage         pull"+"\nset temperature    "+ str(temp) +"\nset boxsize_x     "+x+"\nset boxsize_y     "+y+"\nset boxsize_z     "+z+"\nset center_x     "+c_x+"\nset center_y     "+c_y+"\nset center_z     "+c_z+"\n"   
    outfile.write(script)
    outfile.close()


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Less Input File")
        sys.exit(1)
        
    name = sys.argv[1]
    boxfile = sys.argv[2]
    data = extract(boxfile)
    
    temp=300 #might need adjustment
    makeconfigfile(name, data, temp)
    
























