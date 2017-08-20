from colors import bcolors

def warn(msg):
    print(bcolors.WARNING + "[WARNING] " + msg + bcolors.ENDC)

def fail(msg):
    print(bcolors.FAIL + "[ERROR] " + msg + bcolors.ENDC)

def info(msg):
    print(bcolors.OKBLUE + "[INFO] " + msg + bcolors.ENDC)

