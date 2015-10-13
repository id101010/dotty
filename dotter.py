#!/usr/bin/python2

DOTFILELIST = 'dotfiledb'

filelist = open(DOTFILELIST, 'rw')
data = []

class DBEntry(object):
    ''' Object to store the db content '''
    TIMESTAMP = ''
    LINKNAME = ''
    SRC = ''
    DST = ''

class DotfileDBTools(object):
    ''' Tools used to populate the database '''

    def parseList(self, filename):
        # Parse filelist and generate an internal list.
        for i, line in enumerate(filelist):
            if not line.startswith('#'):
                fl.append(line)

    def appendObject()

class Dotter(object):
    ''' Control logic '''
