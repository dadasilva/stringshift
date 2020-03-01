#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    ssmaster.py
    David DaSilva
    
    PROJECT
    - From an input string and an offset number,
      create the output string in which each character of
      the input string is shifted by the offset.
    - ignore special characters
    - keep case with lower and upper
    - alphabet and digits must loop from z -> a and 0 -> 9
    
    EXECUTION
    - python3 ssmaster.py [test.txt] [offset #]
    
    DIRECTORY
    /ssmaster.py
    /0#.txt
    /dll.py
    /Output
        /output_#.txt
 
    TESTING
    - This driver will self test by shifting the given string,
      writing to an external output file and then resetting it.
    
"""

import os
import sys
import string
import codecs
from subprocess import call
from dll import Node, DLL

ofAlpha = 0
ofDigit = 1

def initList(list, flag):
    if flag == 0:
        for i in range(26):
            list.append(string.ascii_lowercase[i])
    if flag == 1:
        for i in range(10):
            list.append(string.digits[i])
    return

def stringShiftDriver(str, offset):
    strTarget = ""
    if len(str) == 0 or offset == 0: return str
    for i in range(len(str)):
        try:
            if(ord(str[i]) > 255): continue
            if str[i].isalpha(): # ALPHA
                if str[i].isupper(): #UP
                    strTarget += DLL.find(alphaList.head,
                                          str[i].lower(),
                                          offset,
                                          ofAlpha
                                          ).upper()
                elif str[i].islower(): #LOW
                    strTarget += DLL.find(alphaList.head,
                                          str[i],
                                          offset,
                                          ofAlpha
                                          )
            elif str[i].isnumeric(): # NUM
                strTarget += DLL.find(digitList.head,
                                      str[i],
                                      offset,
                                      ofDigit
                                      )
            else: # ALL OTHERS
                strTarget += str[i]
                continue
        except:
            print("usage: utf-8")
            continue
    return strTarget


if __name__ == '__main__':


    File = sys.argv[1]
    offset = sys.argv[2]
    reset = int(offset)*-1
    targetString = list()
    unShiftTargetString = list()

    shiftFilename = r"Output/shiftOutput_ss_offset={}.txt".format(offset)
    unshiftFilename = r"Output/unShiftOutput_ss_offset={}.txt".format(offset)

    #probStr="!@#$%^&*()"
    #offset = 1

    #INITIALIZE DLL:
    #   Alphabet [a...z]
    #   Digits   [0...9]
    alphaList = DLL()
    initList(alphaList, ofAlpha)
    digitList = DLL()
    initList(digitList, ofDigit)

    #SET THE HEADS AND THE TAILS TO POINT TO ONE ANOTHER
    alphaList.head.prev = DLL.last(alphaList.head)
    DLL.last(alphaList.head).next = alphaList.head
    digitList.head.prev = DLL.last(digitList.head)
    DLL.last(digitList.head).next = digitList.head

    with open(File,'r') as i:
           probStr = i.readlines()
           os.system("echo " + "{} ".format(probStr[-1]))
           os.system("echo" + " Shifting...")
           targetString.append(stringShiftDriver(probStr[-1], int(offset)))
           #print("\n{} \nbecomes \n{}".format(probStr, stringShiftDriver(probStr[-1], int(offset))))

    with open(shiftFilename,'w') as o:
        for line in targetString:
            o.write("{}".format(line))

    os.system("cat " + "{} ".format(shiftFilename))

    with open(shiftFilename,'r') as i:
              probStr = i.readlines()
              unShiftTargetString.append(stringShiftDriver(probStr[-1], reset))
              #print("\n{} \nbecomes \n{}".format(probStr, stringShiftDriver(probStr[-1], int(offset))))

    with open(unshiftFilename,'w') as o:
        for line in unShiftTargetString:
            o.write("{}".format(line))


    #SHOW DIFFERENCE ON CONSOLE
    os.system("echo" + " unShifting...")
    os.system("cat " + "{} ".format(unshiftFilename))

    exit(0)
