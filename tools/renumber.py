#!/usr/bin/python3
# Renumber a BASIC PROGRAM.
# Manage GOTO AND GOSUB Calls too

import sys,re
from pathlib import Path

LINE_FINDER=re.compile("([0-9]+)", re.IGNORECASE)
GOTO_FINDER=re.compile("GOTO ([0-9]+)", re.IGNORECASE)

def collect_numbers(fname, increment=100):
    old2new={}    
    new_line_number=100
    with open(fname, "r") as f:
        for current_line in f:    
            possibile_number=LINE_FINDER.findall(current_line)
            #print(current_line,possibile_number)
            if(len(possibile_number)>=1):
                current_number=int(possibile_number[0])
                old2new[current_number]=new_line_number
                new_line_number=new_line_number+increment
    return old2new

def renumber_file(fname,old2new, postfix=".new"):
    dest_filename=fname+postfix
    with open(dest_filename, "w") as dest:
        with open(fname,"r") as source:
            for current_line in source:
                possibile_number=LINE_FINDER.findall(current_line)
                if(len(possibile_number)>=1):
                    new_number=old2new[int(possibile_number[0])]
                    ## renumbered_line=re.sub("([0-9]+) ",str(new_number)+" ",current_line,count=1)           
                    renumbered_line=LINE_FINDER.sub(str(new_number),current_line,count=1)                    
                    #print(current_line," ->", renumbered_line)
                    dest.write(renumbered_line)
                else:
                    dest.write(current_line)
    return dest_filename

def fix_goto(fname,old2new):
    temp_filename=fname+".tmp"
    with open(temp_filename, "w") as dest:
        with open(fname,"r") as source:
            for current_line in source:
                possible_goto=GOTO_FINDER.findall(current_line)
                if(len(possible_goto)>=1):
                    dest_line=current_line                    
                    for candidate in possible_goto:
                        new_goto_number=old2new[int(candidate)]
                        dest_line=GOTO_FINDER.sub("GOTO "+str(new_goto_number),dest_line,count=1)
                        print(candidate, "->",new_goto_number, dest_line)
                else:
                    dest_line=current_line
                dest.write(dest_line)    
    return (Path(temp_filename)).replace(fname)
                

def renumber(flist):
    for fname in flist:
        print("Renumbering",fname)
        old2new=collect_numbers(fname)
        print(old2new)
        dest_filename=renumber_file(fname,old2new)
        fix_goto(dest_filename,old2new)
        #fix_gosub(fname,old2new)

if __name__ == "__main__":
    renumber(sys.argv[1:])