
#!/usr/bin/python

import thread
import time


class test(object):
	def __init__(self):
		self.num_var = 0
	def count_up(self):
		for x in xrange(1,50):
			time.sleep(1)
			self.num_var = self.num_var +1
			#print self.num_var

testobj = test()
testobj2 = test()
#testobj.count_up()

try:
	thread.start_new_thread( testobj.count_up, () )
	thread.start_new_thread( testobj2.count_up, () )
except:
	print "Erps ror: unable to start thread"

while 1:
	time.sleep(1)
	print testobj.num_var
	print testobj2.num_var


"""import time
from jsonrpclib import Server
from abio import TempSensor, AnalogOut, AnalogLambda, FireSensor
from innovate_lambda import SerialLambda
from flask import Flask
from flask_restful import Resource, Api


DEVICE_NAME = "LC-2"
DEVICE_PORT = "/dev/ttyUSB0"
BAUD = 19200
SYNC_HEADER_ATTEMPT = 10

FAN_RELAY_PIN = 8
FAN_ANALOG_PIN = 1
LAMBDA_RELAY_PIN = 7
LAMBDA_ANALOG_PIN = 1
FIRE_ANALOG_PIN = 2

s = Server("http://127.0.0.1/rpc")


tank = TempSensor(s,"286B075005000099")
boiler = TempSensor(s, "28E6E8500500008C")
fall_back = TempSensor(s, "2888045105000028")
print tank.get_temp()
print boiler.get_temp()
print fall_back.get_temp()


def get_all_temp():
	return {"Tank": tank.get_temp(), "Boiler": boiler.get_temp(), "Fall back": fall_back.get_temp()}



app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return get_all_temp()

api.add_resource(HelloWorld, '/')

app.run(host='0.0.0.0', debug=True)

"""
"""
#Lambda
lambdasond0 = AnalogLambda(s, LAMBDA_RELAY_PIN, LAMBDA_ANALOG_PIN)
lambdasond0.activate_contactor()
for x in xrange(1,50):
	print lambdasond0.get_voltage()
	time.sleep(0.5)
lambdasond0.deactivate_contactor()
"""
"""

lambdasond1 = SerialLambda(s, LAMBDA_RELAY_PIN, DEVICE_NAME, DEVICE_PORT, BAUD, SYNC_HEADER_ATTEMPT)
#lambdasond1.activate_contactor()

print lambdasond1.GetAllValue()
lambdasond1.deactivate_contactor()
"""
"""
#FAN
fan = AnalogOut(s, FAN_RELAY_PIN, FAN_ANALOG_PIN)

fan.activate_contactor()
time.sleep(2)
for x in xrange(1,15):
	fan.increase_voltage(0.5)
	print fan.voltage
	time.sleep(1)

for x in xrange(1,15):
	fan.decrease_voltage(0.5)
	print fan.voltage
	time.sleep(1)

fan.set_voltage(0)
fan.deactivate_contactor()

#Fire
fire = FireSensor(s, FIRE_ANALOG_PIN)
print fire.get_temp()

#TEMP 
tank = TempSensor(s,"286B075005000099")
boiler = TempSensor(s, "28E6E8500500008C")
fall_back = TempSensor(s, "2888045105000028")
print tank.get_temp()
print boiler.get_temp()
print fall_back.get_temp()
"""