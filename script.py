import sys
import getopt
import requests

def getKey():
    with open('key.txt', 'r') as file:
        data = file.read().rstrip()
        return data
