class TempSensor(object):
	def __init__(self,s, adress):
		self.s = s
		self.adress = adress
	def get_temp(self):
		return self.s.sensor_get_value(self.adress)


class AnalogOut(object):
	def __init__(self,s, relay_pin, analog_pin, voltage=0):
		self.s = s
		self.relay_pin = relay_pin
		self.analog_pin = analog_pin
		self.voltage = voltage

	def activate_contactor(self):
		self.s.relay_set(self.relay_pin, 1)
	def deactivate_contactor(self):
		self.s.relay_set(self.relay_pin, 0)
	def set_voltage(self, voltage):
		self.voltage = voltage
		self.s.ao_set_value(self.analog_pin, self.voltage)
	def increase_voltage(self, increase_value):
		self.voltage = self.voltage + increase_value
		self.s.ao_set_value(self.analog_pin, self.voltage)
	def decrease_voltage(self, decrease_value):
		self.voltage = self.voltage - decrease_value
		self.s.ao_set_value(self.analog_pin, self.voltage)
	def get_rpm(self):
			return self.voltage * 244

class AnalogLambda(object):
	def __init__(self,s, relay_pin, analog_pin):
		self.s = s
		self.relay_pin = relay_pin
		self.analog_pin = analog_pin

	def activate_contactor(self):
		self.s.relay_set(self.relay_pin, 1)
	def deactivate_contactor(self):
		self.s.relay_set(self.relay_pin, 0)
	def get_voltage(self):
		l = self.s.ai_get(self.analog_pin)
		return round(l[0], 2)
	def get_lambda():
		pass

class FireSensor(object):
	def __init__(self, s, analog_pin):
		self.s = s
		self.analog_pin = analog_pin
	def get_temp(self):
		t = self.s.ai_get(self.analog_pin)
		return round(t[0]/5*1000, 1)