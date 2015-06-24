import time
from jsonrpclib import Server
from abio import TempSensor, AnalogOut, AnalogLambda, FireSensor
from innovate_lambda import SerialLambda

class Ab(object):
	def __init__(self, openWbCfg):
		self.openWbCfg = openWbCfg
		self.alivecount = 0
		self.s = Server(self.openWbCfg.EVOK_URL)
		self.tank = TempSensor(self.s, self.openWbCfg.TANK_TEMP_SENSOR_ID)
		self.boiler = TempSensor(self.s, self.openWbCfg.BOILER_TEMP_SENSOR_ID)
		self.fall_back = TempSensor(self.s, "286B075005000099")
		self.fire = FireSensor(self.s, self.openWbCfg.FIRE_TEMP_SENSOR_ANALOG_PIN)
		self.fan = AnalogOut(self.s, self.openWbCfg.FAN_CONTACTOR_PIN, self.openWbCfg.FAN_ANALOG_PIN)

	def start(self):
		for x in xrange(1,10):
			time.sleep(1)
			print "sleep"
	def count_up(self):
		for x in xrange(1,1000):
			time.sleep(1)
			self.alivecount = self.alivecount +1

	def get_all_data(self):
		return {"Fan rpm": self.fan.get_rpm(), "Tank": self.tank.get_temp(), "Boiler": self.boiler.get_temp(), "Fall back": self.fall_back.get_temp(), "Fire": self.fire.get_temp()}

