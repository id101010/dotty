#!/usr/bin/python2
#-*- coding: utf-8 -*-

from optparse import OptionParser

class DBEntry(object):
    ''' Object to store the db content '''
    LINKNAME = ''
    SRC = ''
    DST = ''

    # Get/Set functions
    def setName(self, name):
        self.LINKNAME = name
    def getName(self):
        return self.LINKNAME
    def setSRC(self, src):
        self.SRC = src
    def getSRC(self):
        return self.SRC
    def setDST(self, dst):
        self.DST = dst
    def getDST(self):
        return self.DST

    # fill the data object
    def fill(self, src, dst, name):
        self.setName(name)
        self.setSRC(src)
        self.setDST(dst)

class DotfileDBTools(object):
    ''' Tools used to populate the database '''

    i = 0;

    # Parses the dotfiledb and generates a DBEntry object
    def getDotfiles(self, filename):
        dotfiles = []
        with open(filename, "r") as dblist:
            lines = [line.strip() for line in dblist if line.strip()]
        for line in lines:
            if not line.startswith('#'):
                src, dst, name = line.split(":")
                dotfiles.append(DBEntry())
                dotfiles[-1].fill(src,dst,name)
                print dotfiles[-1].getName
                print dotfiles[-1].getSRC
                print dotfiles[-1].getDST

    # Appends a dotfile to the dotfiledb
    def linkObject(self, DBEntry):
        #TODO
        print "not implemented"

    # Appends a dotfile to the dotfiledb
    def listObject(self, DBEntry):
        #TODO
        print "not implemented"

if __name__ == "__main__":
    '''Control logic, if not loaded as a module'''
    # Variables
    dbfilename = './dotfiledb'
    
    # Option parsing
    parser = OptionParser()
    

    parser.add_option(  "-d", 
                        "--dbfile",
                        action="store", 
                        type="string", 
                        dest="dbfilename",
                        help="Path for the DB file.")

    parser.add_option(  "-a", 
                        "--adddotfile", 
                        action="store_true", 
                        dest="add",
                        help="Adds a dotfile to the DB.")

    parser.add_option(  "-t", 
                        "--testdb", 
                        action="store_true",
                        dest="test",
                        help="List entrys in the DB.")
    
    parser.add_option(  "-l",
                        "--link",
                        action="store_true",
                        dest="link",
                        help="Create links according to the DB.")

    (options, args) = parser.parse_args()

    if options.add is True:
        print "add not implemented"

    if options.test is True:
        tools = DotfileDBTools()
        tools.getDotfiles(options.dbfilename)


    if options.link is True:
        print "link not implemented"



    test = DBEntry()
    test.setName("test")
    test.setSRC("adfjasdlfk")
    test.setDST("asdasd")

    dblist = []
    dblist.append(test)

    print test.getName
