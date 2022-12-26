from appium import webdriver
import subprocess
import os
import time
from tqdm import tqdm

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

base_path = '/Users/jaegeun.yoon/dev/PalleralCloner_apk'

pc_matching = {
    # "package.name" : "file.apk"
    "com.space.water.clone.multiple.clone.app.accounts.arm32":"water_clone_arm32.apk",
    "com.parallel.space.pro.arm32":"parallel_space_pro_arm32.apk",
    "com.parallel.space.lite.arm32":"parallel_space_lite_arm32.apk",
    "com.kabadokia.bit64.dual_multi_space_64bit_support":"dual_multi_space_64bit_support.apk",
    "com.app.hider.master.dual.app.helper64":"hider_dual_helper64.apk",
    "com.app.hider.master.dual.app.helper32":"hider_dual_helper32.apk", # INSTALL_FAILED_NO_MATCHING_ABIS
    "com.khapalstudio.parallel.clonespace.accounts.app":"Parallel Accounts App.apk",
    "com.matey.parallel.space.cloner":"Multi Parallel Space.apk",
    "com.oneplus.backuprestore":"휴대전화 복제.apk",
    "io.multiple.clone":"Clone App.apk",
    "cloner.infocus.whatclone.whatsweb":"WhatsClone.apk",
    "com.kuotareguler.wacloneapp":"WA Clone App.apk",
    "com.pspace.vandroid":"Virtual Android.apk",
    "com.cloneapp.parallelspace.dualspace.arm32":"Clone App 32Bit Support.apk", # INSTALL_FAILED_NO_MATCHING_ABIS
    "com.pan.parallelspace":"Parallel Space.apk",
    "com.pt.multiple.parallel.dual.space":"Parallel Accounts  Dual Space.apk",
    "com.ninetyplus.dualapp":"Dual Space.apk",
    "com.excelliance.multiaccounts.b32":"Multiple Accounts Assist.apk",
    "com.directworks.dualappspro":"Dual Apps.apk",
    "com.cloner.android":"AppCloner.apk",
    "com.mtech.mydual":"Dual.apk",
    "do.multiple.cloner":"DO Multiple Space.apk",
    "com.app.hider.master.dual.app.lite":"Dual App Lite.apk",
    "com.app.hider.master.dual.app":"Dual App.apk",
    "com.dualspace.multispace.android":"MultiSpace.apk",
    "com.dualspace.cloneapp.parallelspace.privacy":"DualClone.apk",
    "com.dualspace.cloneapp.parallelspace.lite":"DualCloneLite.apk",
    "com.dualapp.dualspace.cloneapp":"DualApp.apk",
    "com.excean.parallelspace.b32":"Parallel App Assist.apk",
    "com.trendmicro.tmas":"Dr Clone.apk", # INSTALL_FAILED_NO_MATCHING_ABIS
    "com.parallel.space.lite.arm32":"Parallel Space Lite 32Bit Support.apk",
    "com.parallel.space.pro.arm32":"Parallel Space Pro 32Bit Support.apk",
    "com.parallel.space.pro":"Parallel Space Pro.apk", # INSTALL_FAILED_NO_MATCHING_ABIS
    "com.parallel.space.lite":"Parallel Space Lite.apk", # INSTALL_FAILED_NO_MATCHING_ABIS
    "com.lbe.parallel.intl.arm32":"Parallel Space 32Bit Support.apk",
    "com.excean.parallelspace":"Parallel App.apk",
    "com.ludashi.dualspace":"DualSpace.apk",
    "com.ludashi.superboost":"DualSpace Lite.apk",
    "com.ludashi.dualspaceprox":"DualSpace Pro.apk",
    "com.space.water.clone.multiple.clone.app.accounts.arm32":"Water Clone - 32bit Support.apk", # INSTALL_FAILED_NO_MATCHING_ABIS
    "com.space.water.clone.multiple.clone.app.accounts":"Water Clone.apk",
    "multi.parallel.dualspace.cloner":"Multi Parallel.apk",
    "com.excelliance.multiaccount":"2Accounts.apk",
    "com.polestar.super.clone":"Super Clone.apk",
    "com.excelliance.multiaccounts":"Multiple Accounts.apk",
    "com.cloneapp.parallelspace.dualspace":"Clone App.apk",
    "com.applisto.appcloner.premium":"App Cloner Premium  Add-ons.apk",
}

pkg_counter = 0
install_success_counter = 0

# App installation
# install option -e : used for active emulator
# install option -d : used for connected USB

for pkg_name, apk in tqdm(pc_matching.items()) :
    full_name = os.path.join(base_path, apk)
    #print(full_name)
    pkg_counter += 1

    try :

        status = subprocess.check_output(['adb', 'install', full_name])
        status = status.decode('utf-8').split(sep='\n', maxsplit=1)

        #print("install : ", status)

        # 중복 설치 시 에러 메세지 없음, 결과값 : 'Success\n'
        if status[1].strip() == "Success":
            install_success_counter += 1
            #print("install successed")
            
    except :
        print("install error : ", full_name)

print("Install Success : ", install_success_counter, "/", pkg_counter)


# adb kill-server

# try :
    
#     status = subprocess.check_output(['adb', 'kill-server'])
#     status = status.decode('utf-8').split(sep='\n', maxsplit=1)
    
#     print("kill server : ", status)

#     if status[1].strip() == "Success":
#         print("exit")

# except :
#     print("kill server error : ", status)