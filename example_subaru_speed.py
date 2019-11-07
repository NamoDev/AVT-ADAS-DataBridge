#
# Example code for grabbing wheel speed data from a Subaru GP car
#

from common.corebus.corebus import CoreBus
from common.utils.debugprint import DebugPrint as dp
from common.can.interface import CANInterface as cif

# Initialize app and CoreBus:
dp.debugPrint("Wheel speed logger", "init")
appCoreBus = CoreBus().connection

# Set CAN interface socket and DBC filename here:`
canInterface = cif("can0", "subaru_global.dbc")
sock = canInterface.sock

# Primary loop
while(True):

    # Keep on listening for CAN packets:
    packet = sock.recv(72)
    decoded = canInterface.decode(packet = packet, filter_id_hex = "0x13a")
    if(decoded != False):

        # Individual wheel speeds
        appCoreBus.set("vehicle.core.sensor.wheelspeed.front.right", float(decoded["FR"]))
        appCoreBus.set("vehicle.core.sensor.wheelspeed.front.left", float(decoded["FL"]))
        appCoreBus.set("vehicle.core.sensor.wheelspeed.rear.right", float(decoded["RR"]))
        appCoreBus.set("vehicle.core.sensor.wheelspeed.rear.left", float(decoded["RL"]))
        appCoreBus.set("vehicle.core.sensor.wheelspeed.updated", canInterface.getCurrentTimestamp())
