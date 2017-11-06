#Script to generate embed code for ActionScript 3 assets
#goes through files in folder and subfolders and creates embed code for each one
#Author: James Konik
#Created: November 2017


import os
import sys

def print_embed( name ):

    #ignore files that start with .
    if name[0] == '.':
        return

    subpath = os.path.relpath(dirpath,mypath)
    subpath = subpath.replace('\\', '/')

    #Adjust this as needed
    print( "[Embed(source='../../../assets/graphics/" + subpath + "/" + name + "')]" )

    #Modify file names to reflect class name constraints

    #remove suffix from name
    name = os.path.splitext( name )[0]
    
    #replace numerics at start of string
    if name[0].isdigit():
        name = "I" + name
    
    #remove dashes
    name = name.replace('-','_')
    print( "public static const " + name.upper() + ":Class;" )



if len(sys.argv) > 1:
    mypath = sys.argv[1]
    
else:
    print( "Usage: 'python embed_generator.py c:/path/to/folder' " )
    exit()


for dirpath, dirnames, filenames in os.walk(mypath):
        for filename in [f for f in filenames ]:
            print_embed( filename )
            







