"""
Get value from device for a UUID
----------------

"""

from Device_data import *


mac_addr = mac_bike # mac_RPI
UUID = UUID_Bike_5 
UUID = UUID_Bike_Read

import asyncio
from bleak import BleakClient

async def run(mac_addr):
    client = BleakClient(mac_addr)
    try:
        await client.connect()
        data = await client.read_gatt_char(UUID)
        print("Value: {0}".format("".join(map(chr, data))),"Raw:",data)
    except Exception as e:
        print(e)
    finally:
        await client.disconnect()


loop = asyncio.get_event_loop()
loop.run_until_complete(run(mac_addr))

