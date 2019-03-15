import nest
from nest import utils as nest_utils
from os import environ
import boto3
import os
from base64 import b64decode
import time

useFutureWeather = True # Use estimated temp 2 hours in the future. Useful in climates with large temperature swings
minhumidity = int(os.environ['min'])
maxhumidity = int(os.environ['max'])
multiplier = int(os.environ['multiplier']) # 20-40

#Handle AWS lambda encrypted resources
epassword = os.environ['password']
password = boto3.client('kms').decrypt(CiphertextBlob=b64decode(epassword))['Plaintext']
eusername = os.environ['username']
username = boto3.client('kms').decrypt(CiphertextBlob=b64decode(eusername))['Plaintext']


def caluculateHumidity(temperature):
    humidity = .5 * temperature + multiplier # Formula assumes fahrenheit
    # Check min/max
    if humidity > maxhumidity:
        humidity = maxhumidity
    elif humidity < minhumidity:
        humidity = minhumidity
    print 'Humidity will be set to: %s\n' % humidity
    return humidity

def lambda_handler(event, context):
    napi = nest.Nest(username, password)
    structure = napi.structures[0]

    if useFutureWeather:
        outsideTemprature = nest_utils.c_to_f(structure.weather.hourly[2].temperature)
    else:
        outsideTemprature = nest_utils.c_to_f(structure.weather.current.temperature)

    print 'Temperature used: %s' % outsideTemprature

    humidity = caluculateHumidity(outsideTemprature)

    for device in napi.devices:
        device.target_humidity = humidity
        
    return
