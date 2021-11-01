import platform
import re
import os


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('Professor! here is programming assignment 7.')
    osENV = str(os.environ)
    platformUNAME = str(platform.uname())#os.uname does not work on windows :(

    userNAME = re.findall(r"'USERNAME': '[a-zA-Z0-9]*'", osENV)
    systemName = re.findall(r"system='[^']*'", platformUNAME)
    nodeName = re.findall(r"COMPUTERNAME'[^']*'[^']*'", osENV)
    print(systemName)
    print(nodeName)
    print(userNAME)
    print(osENV)


