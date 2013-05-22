import time,os
from upload_test.CommonLibrary.Android.AdbBase import adb

def adb_get_current_activity():
    '''return current activity object, it have property package name and activity name'''
    class Activity(object):
        def __init__(self):
            self.package_name = None
            self.activity_name = None
    activity = Activity()
    output = execute_adb_command("shell dumpsys activity")
    print output
    lines = output.splitlines()
    for line in lines:
        line = line.strip()
        if line.startswith("mFocusedActivity"):
            items = line.split("{")[1].split(" ")[2].split("/")
            package_name = items[0]
            activity_name = items[1].split(".")[-1]
            if activity_name.endswith("}"):
                activity_name = activity_name[:-1]
            activity.package_name = package_name
            activity.activity_name = activity_name
    return activity

def adb_install_apk(apk_path,apk_name):
    apk_path_name=apk_path + os.sep + apk_name
    output=execute_adb_command("install %s" % apk_path_name)
    if output.find("Success")==-1:
        raise RuntimeError("install apk %s fail" % apk_name)
    else:
        print "install apk %s success" % apk_path_name
    
def adb_unistall_apk(package_name):
    output=execute_adb_command('uninstall %s' % (package_name))
    if output.find("Success")==-1:
        raise RuntimeError("unistall apk with package name %s fail" %package_name)
    else:
        print "uninstall apk with package name %s success" % package_name

def adb_launch_app(package_name, launch_activity_name):
    output=execute_adb_command("shell am start -n %s/%s"%(package_name, launch_activity_name))
    print output
    if output.find("Error")!=-1:
        raise RuntimeError("launch app fail")

def adb_enable_wifi():
    execute_adb_command("shell svc wifi enable")

def adb_disable_wifi():
    execute_adb_command("shell svc wifi disable")
    
def adb_check_network_connected():
    output = execute_adb_command("shell ping -c 3 www.126.com")
    if output.find("ping: unknown host www.126.com") != -1:
        return False
    else:
        return True
    
def adb_restart_device():
    execute_adb_command("reboot")
    
def adb_check_device_started():
    output=execute_adb_command("shell getprop init.svc.bootanim")
    if output.find("stopped")!=-1:
        return True
    else:
        return False
        
def adb_kill_process(*process_names):
    def remove_space_in_list(items):
        new_list=[]
        for item in items:
            if item!="":
                new_list.append(item)
        return new_list
    
    def waiting():
        time.sleep(1)
        
    def kill_process(*process_names):
        output=execute_adb_command("shell ps")
        lines = output.split("\r\n")
        for line in lines:
            items=remove_space_in_list(line.split(" "))
            if len(items)!=9:continue
            for process_name in process_names:
                if items[8].startswith(process_name):
                    pid=items[1]
                    print "adb shell kill %s"%pid
                    execute_adb_command("shell kill %s" % pid)
        waiting()
        
    kill_process(*process_names)
    kill_process(*process_names)
    
def adb_force_stop_app(package_name):
    execute_adb_command("shell am force-stop %s" % package_name)
    
def adb_unlock_screen(key_event_code=82):
    '''code 82 is only working for emulator, not for all the devices'''
    execute_adb_command("shell input keyevent %d" % key_event_code)

def execute_adb_command(command):
    p = adb.cmd(command)
    output=p.communicate()[0].decode("utf-8")
    if os.environ.has_key("ADBCMD_OUTPUT"):
        print output
    return output
    
if __name__=="__main__":
#     adb_kill_process("com.example.pushservice_compatible1.view","com.netease.pomelo.messageservice_V1")
#     adb_unistall_apk("com.example.pushservice_compatible1.view")
    activity = adb_get_current_activity()
    print activity.package_name
    print activity.activity_name
#     adb_launch_app("com.netease.androidsdk", ".MainActivity")
        
    # adb_kill_process("com.netease.androidsdk")
    

