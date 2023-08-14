import os,platform
os.system('git pull')
# exit(' Wait Tool On updating ')
USMI=platform.architecture()[0]
if usmi=="32bit":
    __import__("usmi32")
elif usmi=="64bit":
     __import__("usmi64")
