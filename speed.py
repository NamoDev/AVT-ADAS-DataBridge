#
# Speed logger - PriusCAN
# AVT ADAS & Autonomy Team, Fall 2019
#

from common.corebus.corebus import CoreBus
from common.utils.debugprint import DebugPrint as dp
from common.can.interface import CANInterface as cif

# Initialize app and CoreBus:
dp.debugPrint("Wheel speed logger", "init")
appCoreBus = CoreBus().connection

# Set CAN interface socket and DBC filename here:`
canInterface = cif("can0", "toyota_prius.dbc")
sock = canInterface.sock

# Primary loop
while(True):

    # Keep on listening for CAN packets:
    packet = sock.recv(72)

    # Try to decode wheel speed
    wheelSpeedDecoded = canInterface.decode(packet = packet, filter_id_hex = "0x0aa")
    if(wheelSpeedDecoded != False):
        # Individual wheel speeds
        appCoreBus.set("vehicle.core.sensor.wheelspeed.front.right", float(wheelSpeedDecoded["WHEEL_SPEED_FR"]))
        appCoreBus.set("vehicle.core.sensor.wheelspeed.front.left", float(wheelSpeedDecoded["WHEEL_SPEED_FL"]))
        appCoreBus.set("vehicle.core.sensor.wheelspeed.rear.right", float(wheelSpeedDecoded["WHEEL_SPEED_RR"]))
        appCoreBus.set("vehicle.core.sensor.wheelspeed.rear.left", float(wheelSpeedDecoded["WHEEL_SPEED_RL"]))
        appCoreBus.set("vehicle.core.sensor.wheelspeed.updated", canInterface.getCurrentTimestamp())

    # Try to decode composite speed
    speedDecoded = canInterface.decode(packet = packet, filter_id_hex = "0x0b4")
    if(speedDecoded != False):
        # Individual wheel speeds
        appCoreBus.set("vehicle.core.sensor.speed", float(speedDecoded["SPEED"]))
        appCoreBus.set("vehicle.core.sensor.speed.updated", speedDecoded.getCurrentTimestamp())
