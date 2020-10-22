"""
Communication with Domyos Bike
----------------
"""

from Device_data import *
mac_addr = mac_bike


import asyncio
from bleak import BleakClient


def notification_handler(sender, data):
    print("{0}: {1}".format(sender, data))
    
    
async def run(mac_addr):
    client = BleakClient(mac_addr, timeout=60.0)
    try:
        x = await client.connect()
        print("Connected: {0}".format(x))
        
        data = await client.read_gatt_char(UUID_Bike_Model)
        print("Value: {0}".format("".join(map(chr, data))),"Raw:",data)
        
        #data = await client.read_gatt_char(UUID_Bike_Read)
        #print("Value: {0}".format("".join(map(chr, data))),"Raw:",data)
        
        
        cmd1 = [240, 172, 156]                                         # "0xf0ac9c" 
        write_value1 = bytearray(cmd1)            
        cmd2 = [240,203,2,0,8,255,1,0,109,1,1,0,0,0,1,0,50,0,1,0]      # "0xf0cb020008ff01006d0101000000010032000100"
        #cmd2 = [240,203,2,0,8,255,12,11,109,10,9,8,7,6,5,4,60,3,2,1]
        write_value2 = bytearray(cmd2)
        cmd3 = [1,0,1,0,0,0,106]                                       # "0x0100010000006a" 
        write_value3 = bytearray(cmd3)                
        cmd4 = [240, 201, 185]                                         # "0xf0c9b9" 
        write_value4 = bytearray(cmd4)
        cmd5 = [240, 163, 147]                                         # "0xf0a393" 
        write_value5 = bytearray(cmd5)
        cmd6 = [240, 164, 148]                                         # "0xf0a494" 
        write_value6 = bytearray(cmd6)

        try:
            await client.start_notify(UUID_Bike_Read, notification_handler)
            for x in range(10):                                        
                
                if(x == 1):
                    await client.write_gatt_char(UUID_Bike_Write, write_value2)
                    print("Writing cmd2")        
                    await client.write_gatt_char(UUID_Bike_Write, write_value3)
                    print("Writing cmd3")        
                
                if(x == 4):
                    await client.write_gatt_char(UUID_Bike_Write, write_value4)
                    print("Writing cmd4")

                if(x == 6):
                    await client.write_gatt_char(UUID_Bike_Write, write_value5)
                    print("Writing cmd5")

                if(x == 8):
                    await client.write_gatt_char(UUID_Bike_Write, write_value6)
                    print("Writing cmd6")

                if(x != 1 and x != 4 and x != 6 and x != 8):
                    await client.write_gatt_char(UUID_Bike_Write, write_value1)
                    print("Writing ___cmd1")

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


