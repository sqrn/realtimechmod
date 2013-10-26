#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TO RUN THIS PROGRAM YOU NEED ROOT PERMISSIONS!
"""

from realtimechmod import RealTimeChmod


directories = (
               '/home/mariusz/workspace/python/realtimechmod/testdir',
               '/home/mariusz/workspace/python/realtimechmod/testdir2',
              )

#newowner = ('esdom', 'ic')

# 1 - cron mode (program is executed in specified time (/etc/crontab)) (default)
# 2 - real time mode (demon)

runningmode = 1


def main():
    rtchm = RealTimeChmod(1)
    rtchm.run(directories)
    rtchm.sleepseconds = 10
    #rtchm.filesInDirectories(directories)



if __name__ == "__main__":
    main()

