#
# DebugPrint
# Handy console output utilities for AVT ADAS DataBridge
#
# @NamoDev, September 2019
#

import sys
import time
import datetime

class DebugPrint():

    def __init__(self):
        pass

    def debugPrint(message, severity = "info"):

        if(severity == "info"):
            DebugPrint.prBlack("[" + str(datetime.datetime.now()) + "][INFO] " + message)
        elif(severity == "warning"):
            DebugPrint.prYellow("[" + str(datetime.datetime.now()) + "][WARN] " + message)
        elif(severity == "error"):
            DebugPrint.prRed("[" + str(datetime.datetime.now()) + "][ERR] " + message)
        elif(severity == "success"):
            DebugPrint.prGreen("[" + str(datetime.datetime.now()) + "][OK] " + message)
        elif(severity == "init"):
            DebugPrint.prCyan("[" + str(datetime.datetime.now()) + "][INIT] " + message)
        else:
            DebugPrint.prBlack("[" + str(datetime.datetime.now()) + "][DEBUG] " + message)

    # Generic ANSI terminal color helpers
    def prRed(prstring): print("\033[91m {}\033[00m" .format(prstring))
    def prGreen(prstring): print("\033[92m {}\033[00m" .format(prstring))
    def prYellow(prstring): print("\033[93m {}\033[00m" .format(prstring))
    def prLightPurple(prstring): print("\033[94m {}\033[00m" .format(prstring))
    def prPurple(prstring): print("\033[95m {}\033[00m" .format(prstring))
    def prCyan(prstring): print("\033[96m {}\033[00m" .format(prstring))
    def prLightGray(prstring): print("\033[97m {}\033[00m" .format(prstring))
    def prBlack(prstring): print("\033[98m {}\033[00m" .format(prstring))
