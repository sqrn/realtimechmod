#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Mariusz Skóra
"""

import os
from stat import S_IRWXO
from time import sleep

DEBUG = True
DEBUGLEVEL = 5

"""
DEBUG MAIN
0 - Emergency (emerg)
1 - Alerts (alert)
2 - Critical (crit)
3 - Errors (err)
4 - Warnings (warn)
5 - Notification (notice)
6 - Information (info)
7 - Debug (debug)
"""

levelList = {
    0 : 'Emergency',
    1 : 'Alerts',
    2 : 'Critical',
    3 : 'Errors',
    4 : 'Warnings',
    5 : 'Notification',
    6 : 'Information',
    7 : 'Debug'
}

class RealTimeChmod:
    sleepseconds = 10

    def __init__(self, runningmode):
        if runningmode == 1:
            self._debug(5, "Running in cron mode...")
        if runningmode == 2:
            self._debug(5, "Running in real time mode...")

        self.runningmode = runningmode


    def run(self, directories):
        if self.runningmode == 1:
            self.filesInDirectories(directories)
        if self.runningmode == 2:
            while(True):
                self.filesInDirectories(directories)
                sleep(self.sleepseconds)


    def filesInDirectories(self, directories):
        """ Public method to changes of needed values
         of files in given directiories
        """
        for dirnamepath in directories:    
            directoryList = os.listdir(dirnamepath)
            debugText = "Jestem w katalogu: {0}".format(dirnamepath)
            self._debug(7, debugText)
            for filename in directoryList:
                debugText = "Found file name: {0}".format(filename)
                self._debug(7, debugText)
                # change mod of file
                filepath = "{0}/{1}".format(dirnamepath, filename)
                print filepath
                self._changeMod(filepath)

    def _changeMod(self, filepath, mode=0777):
        """ Method changes permissions of given filepath"""
        os.chmod(filepath, mode)
        # @TODO
        # trzeba sprawdzic czy uprawnienia sie zmienily

    def _changeOwner(self, filepath, newowner, newgroup):
        """ Method changes owner and group of file, like chmod owner:group"""
        # owner - UID of new owner
        # group - GID of new group
        uid = self._getUserUIDAndGID(newowner, newgroup)[0]
        gid = self._getUserUIDAndGID(newowner, newgroup)[1]

        os.chown(filepath, uid, gid)

        #@TODO has it been changed?

    def _checkFilePermissions(self, filepath, mode=0777):
        pass

    def _getUserUIDAndGID(self, username):
        import pwd
        uid = pwd.getpwnam(username)[2]
        gid = pwd.getpwnam(username)[3]

        return (uid,gid,)

    def _debug(self, levelindex, inputtext):
        if DEBUG is True:
            if levelindex <= DEBUGLEVEL:
                debugText = "{0}: {1}".format(levelList[levelindex], inputtext)
                print debugText
            





