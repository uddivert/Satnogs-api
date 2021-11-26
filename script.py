#!/usr/bin/env python
import sys
import requests
import argHandler
import keyHandler 
from distutils.util import strtobool


"""
main method. Handles all the commandline arguments and
and runs their respective methods 
"""
def main() -> int:
    argHandler.argParser();
    return 0;

if __name__ == '__main__':
    sys.exit(main())