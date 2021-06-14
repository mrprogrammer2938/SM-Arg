#!/usr/bin/python3
# This code write by Mr.nope
import os
import time
import sys
import platform
system = platform.uname()[0]
smarg_version = "\nSMArg 1.3.0\n"
def arg():
    try:
        if sys.argv[1] == '--install':
          os.system("sudo apt install " + sys.argv[2])
        elif sys.argv[1] == '--help':
            print("""
This code write by Mr.nope

--install installing pkg
--help smarg Argument help
--version smarg version
--uninstall uninstalling pkg
""")
            sys.exit()
        elif sys.argv[1] == '--version':
            print(smarg_version)
            sys.exit()
        elif sys.argv[1] == '--uninstall':
            os.system("sudo apt remove " + sys.argv[2])
            sys.exit()
        else:
            print("\nPlease, Check Argument!\n")
            sys.exit()
    except IndexError:
        print("\nPlease, usage: --help\n")
        sys.exit()
if __name__ == '__main__':
    try:
        if system == 'Linux':
            arg()
        elif system == 'Mac':
            arg()
        elif system == 'Windows':
            print("\nPlease, Run This Code on Linux OR MacOS\n")
            sys.exit()
        else:
            print("\nPlease, Run This Code on Linux OR MacOS\n")
            sys.exit()
    except:
        sys.exit()
