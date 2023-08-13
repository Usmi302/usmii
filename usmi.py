import os,platform

os.system('git pull')

ass=platform.architecture()[0]

if ass=="32bit":

__import__("usmi32"). approval()

elif ass=="64bit":

__import__("usmi64"). approval()
