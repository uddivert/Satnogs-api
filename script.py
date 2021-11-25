#!/usr/bin/env python
import sys
import getopt
import requests
import argparse

"""
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

#printArgs()
"""
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-s", "--satellite", help="Retrieve a full or filtered list" +
                   "of satellites in SatNOGS DB",
                    action="store_true")
group.add_argument("-m", "--mode", help="Radio Frequency modulation modes" +
                   "(RF Modes) currently tracked in the SatNOGS DB database",
                    action="store_true")
group.add_argument("-t", "--telemetry", help="View into the Telemetry " +
                   "objects in the SatNOGS DB database. Currently, " +
                   "this table is inclusive of all data collected from "
                   "satellite downlink observations",
                   action="store_true")
group.add_argument("-l", "--tle", help="Read-only view into the most" +
                   "recent two-line elements (TLE) in the SatNOGS DB database",
                   action="store_true")
group.add_argument("-r", "--transmitter", help="View into the Transmitter" +
                   "entities in the SatNOGS DB database. Transmitters are " +
                   "inclusive of Transceivers and Transponders",
                   action="store_true")
parser.add_argument("-fs", '--format_string', type=str, help='foo help')

args = parser.parse_args()

if args.format_string:
    print(args.format_string)
if args.mode:
    print("mode turned on")
elif args.satellite:
    print("satllite is turned on")
elif args.telemetry:
    print("telemetry is turned on")
elif args.tle:
    print("tle is turned on")

