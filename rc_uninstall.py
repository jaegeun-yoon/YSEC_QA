import os
import subprocess
from tqdm import tqdm

base_path = '/Users/jaegeun.yoon/dev/RemoteControler_apk'

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
uninstall_success_counter = 0

for pkg_name, apk in tqdm(rc_matching.items()) :
    full_name = os.path.join(base_path, apk)
    #print(full_name)
    pkg_counter += 1
    # App uninstallation
    # adb uninstall [-k : keep the data and cache directories] package

    try :
        
        status = subprocess.check_output(['adb', 'uninstall', pkg_name])
        status = status.decode('utf-8').split(sep='\n', maxsplit=1)
        
        #print("uninstall : ", status)

        if status[0].strip() == "Success":
            uninstall_success_counter += 1
            #print("Uninstall success")

    except :
        print("uninstall error : ", full_name)

print("Uninstall Success : ", uninstall_success_counter, "/", pkg_counter)