from flask import Flask
from flask_restful import Resource, Api
from ab import Ab
from openWbCfg import openWbCfg
import thread

CFG_FILE = "openWB.cfg"





openWbCfg = openWbCfg(CFG_FILE)

Ab = Ab(openWbCfg)


class HelloWorld(Resource):
	def get(self):
		return Ab.get_all_data()
		#return {"alivecount": Ab.alivecount}

try:
	thread.start_new_thread( Ab.count_up, () )
except:
	print "Erps ror: unable to start thread"

app = Flask(__name__)
api = Api(app)
api.add_resource(HelloWorld, '/')
app.run(host='0.0.0.0', debug=True)







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