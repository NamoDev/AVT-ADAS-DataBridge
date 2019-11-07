#
# CANInterface
# Handy functions for interfacing with a car's CAN Interface
#
# @NamoDev, September 2019
#

import os
import sys
import time
import socket
import struct
import cantools
import datetime
import binascii
from common.utils.debugprint import DebugPrint as dp

class CANInterface():

    #
    # __init__()
    # Initializes the interface
    #
    def __init__(self, can_interface = "can0", dbc_file = "generic.dbc"):
        dp.debugPrint("Initializing CAN interface on " + can_interface, "info")
        self.interface = can_interface

        # Try to connect to CAN
        sock = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
        while True:
            try:
                sock.bind((self.interface,))
                break
            except OSError:
                dp.debugPrint("Unable to establish CAN connection on " + can_interface + ". Terminating!", "error")
                exit(1)

        dp.debugPrint("Established CAN connection on " + can_interface, "success")
        self.sock = sock

        # Load DBC
        dp.debugPrint("Loading DBC: " + dbc_file, "info")
        actualPath = os.path.dirname(os.path.abspath(__file__))
        db = cantools.database.load_file(str(actualPath) + "/dbc/" + dbc_file)
        self.db = db
        dp.debugPrint("DBC loaded", "success")

    #
    # decode()
    # Filters and decodes CAN data
    #
    def decode(self, packet, filter_id_hex):

        # Do we have a valid CAN (not CAN-FD) packet to process?
        if(len(packet) == 16):
            canID, packetLength, rawData = struct.unpack("<IB3x8s", packet)
            canDataStr = str(binascii.hexlify(rawData), "utf-8")

            # Is this what we're looking for?
            if(canID == int(filter_id_hex, 16)):

                # Yes. Decode and return:
                decoded = self.db.decode_message(canID, rawData)
                return decoded
            else:
                # Not what we're looking for
                return False
        else:
            # Not what we're looking for either
            return False

    #
    # getCurrentTimestamp()
    # Return current timestamp in human-readable format.
    # Useful for a variety of purposes.
    #
    def getCurrentTimestamp(self):
        return str(datetime.datetime.now())
