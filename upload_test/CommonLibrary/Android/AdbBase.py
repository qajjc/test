import os
import re
import subprocess

__all__ = ["adb"]

class Adb():
    def __init__(self, serial=None):
        self.__adb_cmd = None
        self.default_serial = serial if serial else os.environ.get("ANDROID_SERIAL", None)
        
    def adb(self):
        if self.__adb_cmd is None:
            if "ANDROID_HOME" in os.environ:
                filename = "adb.exe" if os.name == 'nt' else "adb"
                adb_cmd = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", filename)
                if not os.path.exists(adb_cmd):
                    raise EnvironmentError(
                        "Adb not found in $ANDROID_HOME path: %s." % os.environ["ANDROID_HOME"])
            else:
                import distutils
                if "spawn" not in dir(distutils):
                    import distutils.spawn
                adb_cmd = distutils.spawn.find_executable("adb")
                if adb_cmd:
                    adb_cmd = os.path.realpath(adb_cmd)
                else:
                    raise EnvironmentError("$ANDROID_HOME environment not set.")
            self.__adb_cmd = adb_cmd
        return self.__adb_cmd
    
    def cmd(self, args):
        '''adb command, add -s serial by default. return the subprocess.Popen object.'''
        cmd_line = ["-s", self.device_serial()] + args.split(" ")
        return self.raw_cmd(*cmd_line)

    def raw_cmd(self, *args):
        '''adb command. return the subprocess.Popen object.'''
        cmd_line = [self.adb()] + list(args)
        if os.name != "nt":
            cmd_line = [" ".join(cmd_line)]
        return subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def device_serial(self):
        devices = self.devices()
        if not devices:
            raise EnvironmentError("Device not attached.")

        if self.default_serial:
            if self.default_serial not in devices:
                raise EnvironmentError("Device %s not connected!" % self.default_serial)
        elif len(devices) == 1:
            self.default_serial = list(devices.keys())[0]
        else:
            raise EnvironmentError("Multiple devices attached but default android serial not set.")
        return self.default_serial

    def devices(self):
        '''get a dict of attached devices. key is the device serial, value is device name.'''
        out = self.raw_cmd("devices").communicate()[0].decode("utf-8")
        match = "List of devices attached"
        index = out.find(match)
        if index < 0:
            raise EnvironmentError("adb is not working.")
        return dict([s.split() for s in out[index + len(match):].strip().splitlines() if s.strip()])

    def forward(self, local_port, device_port):
        '''adb port forward. return 0 if success, else non-zero.'''
        return self.cmd("forward tcp:%d tcp:%d" % (local_port, device_port)).wait()

    def forward_list(self):
        '''adb forward --list'''
        version = self.version()
        if int(version[1]) <= 1 and int(version[2]) <= 0 and int(version[3]) < 31:
            raise EnvironmentError("Low adb version.")
        lines = self.raw_cmd("forward", "--list").communicate()[0].decode("utf-8").strip().splitlines()
        return [line.strip().split() for line in lines]

    def version(self):
        '''adb version'''
        match = re.search(r"(\d+)\.(\d+)\.(\d+)", self.raw_cmd("version").communicate()[0].decode("utf-8"))
        return [match.group(i) for i in range(4)]
    
adb=Adb()