"""
Communication with Domyos Bike
----------------
"""

from Device_data import *


mac_addr = mac_bike # mac_RPI
UUID = UUID_Bike_5 #UUID_Rpi_1
#UUID = UUID_Bike_Service
UUID = UUID_Bike_Read
#UUID = UUID_Bike_Write


import asyncio
from bleak import BleakClient


def notification_handler(sender, data):
    print("{0}: {1}".format(sender, data))
    
    
async def run(mac_addr):
    client = BleakClient(mac_addr, timeout=60.0)
    try:
        x = await client.connect()
        print("Connected: {0}".format(x))
        
        data = await client.read_gatt_char(UUID_Bike_5)
        print("Value: {0}".format("".join(map(chr, data))),"Raw:",data)
        
        data = await client.read_gatt_char(UUID_Bike_Read)
        print("Value: {0}".format("".join(map(chr, data))),"Raw:",data)
        
        # "0xf0ac9c" 
        cmd1 = [240, 172, 156]        
        write_value1 = bytearray(cmd1)            
        cmd2 = "f0ac9c"
        write_value2 = bytearray(cmd2, 'utf-8')
        
        write_value = write_value1        
        print("Writing Value:", write_value)
        
       
        try:
            await client.start_notify(UUID_Bike_Read, notification_handler)
            for x in range(5):
                #print(x)
                await client.write_gatt_char(UUID_Bike_Write, write_value)        
                await asyncio.sleep(2.0)
        except Exception as e:
            print(e)
        finally:
            await client.stop_notify(UUID_Bike_Read)
                
        
    except Exception as e:
        print(e)
    
    finally:        
        await client.disconnect()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(mac_addr))


