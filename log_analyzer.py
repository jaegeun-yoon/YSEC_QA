from appium import webdriver
import subprocess
import re
import os
import time
from tqdm import tqdm

mode = 'DEV'

# device status check
status = subprocess.check_output(['adb', 'devices'])
status = status.decode('utf-8').split(sep='\n', maxsplit=1)

if status[1] :
    print("status : ", status[1])
else :
    # adb start-server
    try :
        status = subprocess.check_output(['adb', 'start-server'])
        status = status.decode('utf-8').split(sep='\n', maxsplit=1)
    except :
        print("adb error : ", status)

# log 탐지 - DEV
status = subprocess.check_output(['adb', 'shell', 'logcat', '-d', '|', 'grep', 'YSEC'])
status = status.decode('utf-8').split(sep='\n', maxsplit=1)

if mode == 'DEV':
    pattern = '<DEV>\s(.*)\s(.*)'
elif mode == 'PROD':
    pattern = '<PROD>\s(.*)\s(.*)'

RootingPackage_Counter = 0
RemoteController_Counter = 0
ParallelCloner_Counter = 0

if status[1] :

    result = re.findall(pattern, status[1])

    print("result : ", result)

    data = dict()

    if result :
        logs = result[0][0].split(sep=' ')
        logs = list(filter(None, logs)) # remove none value in list

        print("log : ", logs)

        for log in logs :
            if log == ']' :
                break

            log = log.split(sep=':')

            if log[0] == "PackageName" :
                print("RootingPackage: ", log[1])

            elif log[0] == "hashCode" :
                print("hashCode : ", log[1])

            elif log[0] == "RootingPackage" :
                RootingPackage_Counter += 1
                print("RootingPackage : ", log[1])

            elif log[0] == "RemoteController" :
                RemoteController_Counter += 1
                print("RemoteController : ", log[1])

            elif log[0] == "ParallelCloner" :
                ParallelCloner_Counter += 1
                print("ParallelCloner : ", log[1])
    else:
        print("Result not found..")
else:
    print("App isn't loaded..")


print("RootingPackage : ", RootingPackage_Counter, "개 발견됨")
print("RemoteController : ", RemoteController_Counter, "개 발견됨")
print("ParallelCloner : ", ParallelCloner_Counter, "개 발견됨")