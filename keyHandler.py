""" 
this opens up the 'key.txt' file
and reads the authorization key written in it
"""
def getKey():
    with open('key.txt', 'r') as file:
        data = file.read().rstrip()
        return data