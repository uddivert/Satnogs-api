#!/usr/bin/env python
import sys
import requests
import argparse
from distutils.util import strtobool

""" 
this opens up the 'key.txt' file
and reads the authorization key written in it
"""
def getKey():
    with open('key.txt', 'r') as file:
        data = file.read().rstrip()
        return data

"""
main method. Handles all the commandline arguments and
and runs their respective methods 
"""
def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True) #requires a mutually exclusive parameter to run
    """ satellite, telemetry, mode, tle and transmitter are all mutually exclusive 
        they cannot be inputted together
    """
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
    parser.add_argument("-fs", '--format_string', type=str, choices=["json","json-ld"],
                        help="format string")
    parser.add_argument("-io", "--in_orbit_boolean",type=str, default="False",
                        help="Filter by satellites currently in orbit (True) or those that have decayed (False)")
    parser.add_argument("-nci", '--norad_cat_id_string', type=str, 
                        help="Select a satellite by its NORAD-assigned identifier")
    parser.add_argument("-si", '--sat_id_string', type=str, help="Satellite ID")
    parser.add_argument("-ss", '--satellite_status', type=str, 
                        help="Filter by satellite status: alive dead future re-entered")
    


    args = parser.parse_args()

    #command line flags
    if args.format_string:
        print(args.format_string)
    if args.norad_cat_id_string:
        print(args.norad_cat_id_string)
    if args.in_orbit_boolean:
        print(strtobool(args.in_orbit_boolean))
    if args.mode:
        print("mode turned on")
    elif args.satellite:
        print("satellite is turned on")
    elif args.telemetry:
        print("telemetry is turned on")
    elif args.tle:
        print("tle is turned on")
    return 0;

if __name__ == '__main__':
    sys.exit(main())