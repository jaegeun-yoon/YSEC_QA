import os
import subprocess
from tqdm import tqdm

base_path = '/Users/jaegeun.yoon/dev/Rooting_apk'

rooting_matching = {
    # "package.name" : "file.apk"
    #"com.ramdroid.appquarantine":"App Quarantine ROOT FREEZE_v1.29_apkfab.com.apk",
    "com.ramdroid.appquarantine":"App_Quarantine-1.29.apk",
    "com.formyhm.hideroot":"Hide Rooting Lite_v1.7_apkfab.com.apk",
    #"com.amphoras.hidemyroot":"Hide my Root_v4.0_apkfab.com.apk",
    "com.amphoras.hidemyroot":"Hide_My_Root-4.0.apk",
    "com.kingoapp.apk":"KingoRoot.apk",
    #"ru.sxbuIDfx.pFSOyagrF":"Lucky Patcher v10.1.0.apk",
    #"ru.sxbuIDfx.pFSOyagrF":"Lucky_Patcher v10.0.9.apk",
    #"ru.sxbuIDfx.pFSOyagrF":"Lucky Patcher v10.1.1.apk",
    "ru.sxbuIDfx.pFSOyagrF":"Lucky+Patcher v10.1.2.apk",
    "com.topjohnwu.magisk":"Magisk Manager_63a89d9f_apkcombo.com.apk",
    "com.smedialink.oneclickroot":"One Click Root_1.2_apkcombo.com.apk",
    "com.zhiqupk.root.global":"Root Master_3.0.0_apkcombo.com.apk", # INSTALL_FAILED_NO_MATCHING_ABIS
    "com.devadvance.rootcloakplus":"RootCloak Plus (Cydia)_1.2_apkcombo.com.apk", # INSTALL_FAILED_NO_MATCHING_ABIS
    "eu.chainfire.supersu.pro":"SuperSU Pro_2.82_apkcombo.com.apk",
    "eu.chainfire.supersu.pro":"eu.chainfire.supersu.pro-2.82-free-www.apkshub.com.apk",
    "eu.chainfire.supersu":"supersu-2-82.apk",
    "com.jrummy.apps.build.prop.editor":"buildprop-editor-2-4-0-rc-gp-free-23408.apk", # INSTALL_FAILED_NO_MATCHING_ABIS
    "stericson.busybox":"busybox-64.apk",
    "com.jrummy.root.browserfree":"com-jrummy-root-browserfree-44113-57720989-264f85e81173c36f7118ef503db475b8.apk", #
    "com.koushikdutta.superuser":"com-koushikdutta-superuser-1027-4406748-c5687e27180dfd781425fc172948bb44.apk",
    "com.alephzain.framaroot":"com.alephzain.framaroot-1.9.3-free-www.apkshub.com.apk", # INSTALL_FAILED_NO_MATCHING_ABIS
    "com.devadvance.rootcloak2":"com.devadvance.rootcloak2_v18_c43b61.apk",
    "com.kingouser.com":"com.kingouser.com_v2.2.7.apk", # INSTALL_FAILED_NO_MATCHING_ABIS
    "com.kingroot.kinguser":"com.kingroot.kinguser_v5.4.0-204_Android-2.3.apk",
    "com.koushikdutta.rommanager":"com.koushikdutta.rommanager_v5.5.3.7-5537_Android-2.2.apk",
    "com.noshufou.android.su":"com.noshufou.android.su-3.3-free-www.apkshub.com.apk",
    "com.saurik.substrate":"com.saurik.substrate-0.9.4011-free-www.apkshub.com.apk", # INSTALL_FAILED_NO_MATCHING_ABIS
    "com.yellowes.su":"com.yellowes.su_2016-04-11.apk",
    "de.robv.android.xposed.installer":"de.robv.android.xposed.installer_v33_36570c.apk",
    "com.oasisfeng.greenify":"greenify-4-7-8.apk",
    "me.phh.superuser":"phh's SuperUser_1.0.3.3_apkcombo.com.apk", # INSTALL_FAILED_NO_MATCHING_ABIS
}

pkg_counter = 0
uninstall_success_counter = 0

for pkg_name, apk in tqdm(rooting_matching.items()) :
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