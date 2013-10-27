#!/usr/bin/env python
# -*- coding: utf-8 -*-

from realtimechmod import RealTimeChmod


"""
Put here the directories full path
"""
directories = (
               '/home/mariusz/workspace/python/realtimechmod/testdir',
               '/home/mariusz/workspace/python/realtimechmod/testdir2',
              )

#this below option is not enabled yet
#newowner = ('esdom', 'ic')


# 1 - cron mode (program is executed in specified time (/etc/crontab)) (default)
# 2 - real time mode (demon)

#set 1 or 2
runningmode = 2


def main():
    rtchm = RealTimeChmod(runningmode)
    rtchm.run(directories)
    rtchm.sleepseconds = 10
    #rtchm.filesInDirectories(directories)



if __name__ == "__main__":
    main()


