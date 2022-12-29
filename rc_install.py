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

base_path = '/Users/' + os.getenv('USER') + '/dev/RemoteControler_apk'

rc_matching = {
    # "package.name" : "file.apk"
    "com.rsupport.mobile.agent":"RVAgent.apk", 
    "com.microsoft.appmanager":"Windows와 연결.apk",
    "com.sand.airdroid":"AirDroid.apk",
    "com.sand.aircast":"AirDroid Cast.apk", 
    "com.devolutions.remotedesktopmanager":"Remote Desktop Manager.apk",
    "com.zoho.assist":"Zoho Assist.apk",
    "com.sand.airmirror":"AirMirror.apk",
    "com.idrive.remotedesktop.android":"Remote Desktop Viewer.apk",
    "com.midassoft.ezhelp":"ezHelp.apk",
    "com.anydesk.anydeskandroid":"AnyDesk.apk",
    "com.remoteutilities.mviewer":"Remote Utilities.apk",
    "com.midassoft.ezmobilesamsung":"ezMobile.apk",
    "com.awesun.control":"AweSun.apk",
    "com.rsupport.remotecall.rtc.host":"RemoteCall.apk",
    "com.midassoft.ezremote":"ezRemote.apk",
    "com.sand.airdroidbizc":"Business.apk",
    "com.prosoftnet.rpcnew":"RemotePC.apk",
    "kr.co.helpu.host":"helpu_host.apk",
    "kr.co.helpu.manager":"HelpU.apk",
    "rsupport.AndroidViewer":"RemoteView.apk",
    "net.koino.anysupportMobile":"koino_anysupportmobile.apk",
    "com.teamviewer.host.market":"Host.apk",
    "com.splashtop.remote.business":"Splashtop Business.apk",
    "runsoft.com.runsupport":"runRemote원격.apk",
    "com.islonline.isllight.mobile.android":"ISL Light.apk",
    "com.splashtop.remote.pad.v2":"Splashtop Personal.apk",
    "nfo.oneassist":"화면 공유.apk",
    "com.monect.portable":"PC Remote.apk",
    "com.sand.airsos":"Support.apk",
    "www.forwardiot.com":"아프로.apk",
    "com.jiransoft.psremote":"PS 리모트 뷰어.apk",
    "com.teamviewer.teamviewer.market.mobile":"TeamViewer.apk",
    "com.rsupport.rs.activity.rsupport":"모바일 지원.apk",
    "com.microsoft.rdc.android":"RD Client.apk",
    "com.realvnc.viewer.android":"VNC Viewer.apk",
    "com.ahranta.android.arc.asp":"모바일헬퍼.apk",
}

pkg_counter = 0
install_success_counter = 0

# App installation
# install option -e : used for active emulator
# install option -d : used for connected USB

for pkg_name, apk in tqdm(rc_matching.items()) :
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