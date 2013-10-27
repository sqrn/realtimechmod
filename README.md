Introduce
==========
This is simple program which changes file' permissions in real time or in cron mode. It can be useful if you have automaticaly generated files and your user application does not have permission to read/write/execute them. You can change permissions also automaticaly.
You do not need setfacl, umask, and others staff.


How to use
==========
- In *main.py* file there are directory section. Put your directories full path.
- Default running mode of program is 2, what it means - real time. Your program is running in loop, at it changes file' permissions if it is needed. You can use option - 1, if you would like to use CRONtab.


What is needed?
==========
Be sure you are running Unix like system ;) This program use Python 2.7.3, and it was written on Debian.

