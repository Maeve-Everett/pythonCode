import sys
## This section will add the time libraries
import PIL
import datetime
import time
import calendar
import icalendar
import datetime
import os
from slackclient import SlackClient

##This line will add the inkyphat library
import inkyphat

## This line will add the bme680 breakout board library
import bme680
print("""This code will make your coffee pot an iot pot! Check at LINK TO BE ADDED SOON
for the laser cutting files""")

dateString = "%-I:%M %p"
sensor = bme680.BME680()
tempGoal = 40
currentTemp = sensor.data.temperature
prevTemp = sensor.data.temperature

# This Section will grab data from the temperature sensor and print it in terminal on the raspberry pi
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

font = PIL.ImageFont.truetype(inkyphat.fonts.FredokaOne, 22)

w, h = font.getsize("FRESH POTS")
x = (inkyphat.WIDTH / 2) - (w / 2)
y = (inkyphat.HEIGHT / 2) - (h / 2)

w, h = font.getsize("STALE POT,\n AVOID BRO")
x2 = ((inkyphat.WIDTH / 2) - (w / 2)) + 65
y2 = ((inkyphat.HEIGHT / 2) - (h / 2)) - 17

slack_client = SlackClient(os.environ.get('SLACK_TOKEN'))

def send_message(channel_id, message):
	slack_client.api_call(
		"chat.postMessage",
		channel=channel_id,
		text=message,
		username='Coffee Bot')

print("current temp:")

while True:
    if sensor.get_sensor_data(): 
        output = "{0} C".format(sensor.data.temperature)
        print(output)
    currentTemp = sensor.data.temperature
    if currentTemp > tempGoal and prevTemp < tempGoal:
        inkyphat.set_border(inkyphat.BLACK)
	inkyphat.clear()
        inkyphat.text((x, y), "FRESH POTS", inkyphat.RED, font)
        inkyphat.show()
	send_message('Channel Id Here', 'Coffee is ready')
    elif currentTemp < tempGoal and prevTemp > tempGoal:
        inkyphat.set_border(inkyphat.BLACK)
        inkyphat.clear()
        inkyphat._draw.multiline_text((x2, y2), "STALE POT,\n AVOID BRO", inkyphat.RED, font)
        inkyphat.show()
	send_message('Channel Id Here', 'Coffee is now cold')

    prevTemp = currentTemp
    time.sleep(5)
    
