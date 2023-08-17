import os,platform
os.system('git pull')
# exit(' Wait Tool On updating ')
usmii=platform.architecture()[0]
if usmii=="32bit":__import__("usmi32")
elif usmii=="64bit":__import__("usmi64")
