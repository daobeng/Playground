import os

def read_from_file(filename):
    if not os.path.exists(filename):
        raise Exception('Bad File')
    in_file = open(filename, 'r')
    line = in_file.readline()
    return line
