import time
import requets
import json
import board 
import adafruit_dht

url = 'https://yoeergerojrgfphyxavb.supabase.co/rest/v1/receive_dados'

dhtDevice = adafruit_dht.DHT22(board.D18)

while True: 
	try: 
        temperature_c = dhtDevice.temperature 
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity 
        obj_sensor = {
	        'temperatura': temperature_c,
	        'umidade' : humidity
        }
        headers = {
	        "apikey": "<seu token aqui>" ,
	        "Autorization": "<Bearer seu token aqui>" 
        }
        send_data = requests.post(url,json = obj_sensor , headers = headers )
        print(send_data) 
    except RuntimeError as error:
         print(error.args[0]) 
         time.sleep(2.0) 
    continue except Exception as error: 
         dhtDevice.exit() 
         raise error 
    time.sleep(2.0)
