#!/usr/bin/env python
import sys
import getopt
import requests

def getKey():
    with open('key.txt', 'r') as file:
        data = file.read().rstrip()
        return data

def printArgs():
    print('ARGV      :', sys.argv[1:])
    print('OPTIONS   :', options)
    print('MODE      :', mode)
    print('SATELLITE :', satellite)
    print('REMAINING :', remainder)

#### MAIN METHOD ####
version = '1.0'
satellite = ''
satFlag = False
modeFlag = False

options, remainder = getopt.getopt(sys.argv[1:], 's:m:', ['satellite=', 
                                                         'mode',
                                                         ])
for opt, arg in options:
    if opt in ('-s', '--satellite'):
        satellite = arg
        satFlag = True

    elif opt in ('-m', '--mode'):
        mode = arg
        modeFlag = True

printArgs()
## what tf does this shit mean if __name__ == "__main__":
