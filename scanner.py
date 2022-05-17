#!/usr/bin/env python3
"""
Temperature Measurement NCP-host Example Application.
"""

# Copyright 2021 Silicon Laboratories Inc. www.silabs.com
#
# SPDX-License-Identifier: Zlib
#
# The licensor of this software is Silicon Laboratories Inc.
#
# This software is provided 'as-is', without any express or implied
# warranty. In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

import argparse
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from common.conversion import Ieee11073Float
from common.util import BluetoothApp, PeriodicTimer

# Constants
# Unit definitions for temperature measurement
TEMPERATURE_UNIT_CELSIUS = b"\x00"
TEMPERATURE_UNIT_FAHRENHEIT = b"\x01"
# Temperature measurement characteristic indication period in seconds
INDICATION_PERIOD = 1.0
# Characteristic values
GATTDB_DEVICE_NAME = b"Thermometer Example"
GATTDB_MANUFACTURER_NAME_STRING = b"Silicon Labs"
GATTDB_TEMPERATURE_TYPE = b"\x02" # Body

class App(BluetoothApp):
    """ Application derived from generic BluetoothApp. """
    def event_handler(self, evt):
        """ Override default event handler of the parent class. """
        # This event indicates the device has started and the radio is ready.
        # Do not call any stack command before receiving this boot event!
        if evt == "bt_evt_system_boot":
            #self.timer = PeriodicTimer(period=INDICATION_PERIOD, target=self.send_indication)

            self.lib.bt.scanner.start(
                self.lib.bt.gap.PHY_PHY_1M,
                self.lib.bt.scanner.DISCOVER_MODE_DISCOVER_GENERIC)


        elif evt == "bt_evt_scanner_scan_report":

                 print("BLE device found\n")
                 #print(evt.data)
                 print(" rssi:", evt.rssi, "\n" )
                 print(" packet_type:" ,  evt.packet_type, "\n" )
                 print(" address:" ,  evt.address,"\n" )
                 print(" address_type: " ,  evt.address_type, "\n" )
                 print(" bonding: " ,  evt.bonding, "\n" )
                 print(" data: " ,  evt.data, "\n" )
                 #print("Advertisement Count: %d\n", BleADVCounter++ )


        # This event indicates that a new connection was opened.
        elif evt == "bt_evt_connection_opened":
            print("Connection opened")

        # This event indicates that a connection was closed.
        elif evt == "bt_evt_connection_closed":
            self.timer.stop()
            print("Connection closed")
            self.adv_start()


# Script entry point.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    # Instantiate the application.
    app = App(parser=parser)
    # Running the application blocks execution until it terminates.
    app.run()
