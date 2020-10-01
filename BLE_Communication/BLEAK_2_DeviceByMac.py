"""
--------------
Scan BLE Device with specific MAC Address - mac_addr
--------------
"""

from Device_data import *

mac_addr = mac_bike 

import asyncio
import platform

import nest_asyncio
nest_asyncio.apply()

from bleak import BleakScanner


async def run():
    device = await BleakScanner.find_device_by_address(mac_addr)
    print("Device Available:",device)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
