"""
--------------
Scan all BLE Devices
--------------
"""


from Device_data import *


import nest_asyncio
nest_asyncio.apply()

import asyncio
from bleak import discover


async def run():
    devices = await discover()
    for d in devices:
        print(d)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
