
import xml.etree.ElementTree as ET
import os, time, hashlib

CONFIG_FILE = 'config.xml'


class ECU(object):

	def __init__(self):
		self.HW_NAME = tryParse("info", "hw_name")
		self.IP = tryParse("info", "ip")

		self.BOILER_TEMP_SENSOR_ENABLED = tryParse("boiler_temp_sensor", "enabled")
		self.BOILER_TEMP_SENSOR_TYPE = tryParse("boiler_temp_sensor", "type")
		self.BOILER_TEMP_SENSOR_BASE_DIR = tryParse("boiler_temp_sensor", "base_dir")
		self.BOILER_TEMP_SENSOR_FILE_NAME = tryParse("boiler_temp_sensor", "file_name")
		self.BOILER_TEMP_SENSOR_ID = tryParse("boiler_temp_sensor", "id")
		self.BOILER_TEMP_SENSOR_GPIO = tryParse("boiler_temp_sensor", "gpio")

		self.TANK_TEMP_SENSOR_ENABLED = tryParse("tank_temp_sensor", "enabled")
		self.TANK_TEMP_SENSOR_TYPE = tryParse("tank_temp_sensor", "type")
		self.TANK_TEMP_SENSOR_BASE_DIR = tryParse("tank_temp_sensor", "base_dir")
		self.TANK_TEMP_SENSOR_FILE_NAME = tryParse("tank_temp_sensor", "file_name")
		self.TANK_TEMP_SENSOR_ID = tryParse("tank_temp_sensor", "id")
		self.TANK_TEMP_SENSOR_GPIO = tryParse("tank_temp_sensor", "gpio")

		self.FIRE_TEMP_SENSOR_ENABLED = tryParse("fire_temp_sensor", "enabled")
		self.FIRE_TEMP_SENSOR_TYPE = tryParse("fire_temp_sensor", "type")
		self.FIRE_TEMP_SENSOR_BASE_DIR = tryParse("fire_temp_sensor", "base_dir")
		self.FIRE_TEMP_SENSOR_FILE_NAME = tryParse("fire_temp_sensor", "file_name")
		self.FIRE_TEMP_SENSOR_ID = tryParse("fire_temp_sensor", "id")
		self.FIRE_TEMP_SENSOR_GPIO = tryParse("fire_temp_sensor", "gpio")

		self.BUTTON_AUTO_MAN = tryParse("control_button", "auto_man_gpio")
		self.BUTTON_MAN_SCREW = tryParse("control_button", "man_screw_gpio")
		self.BUTTON_MAN_FAN = tryParse("control_button", "man_fan_gpio")
		
		self.BLOCK_TIME = tryParse("timers", "block_time")
		self.BLOCK_TIME_IDLE = tryParse("timers", "bock_time_idle")
		self.RUN_TIME_FAN_IDLE = tryParse("timers", "run_time_fan_idle")
		self.RUN_TIME_SCREW = tryParse("timers", "run_time_screw")
		self.RUN_TIME_SCREW_IDLE = tryParse("timers", "run_time_screw_idle")
		
		self.MAX_POWER_MIN_TEMP = tryParse("limits", "min_temp_value")
		self.IDLE_MIN_TEMP = tryParse("limits", "idle_min_temp_value")

		self.FAN_ENABLED = tryParse("fan", "enabled")
		self.FAN_TYPE = tryParse("fan", "type")
		self.FAN_GPIO = tryParse("fan", "gpio")

		self.SCREW_ENABLED = tryParse("screw", "enabled")
		self.SCREW_TYPE = tryParse("screw", "type")
		self.SCREW_GPIO = tryParse("screw", "gpio")

		self.DATABASE_ENABLED = tryParse("database", "enabled")
		self.DATABASE_TYPE = tryParse("database", "type")
		self.DATABASE_NAME = tryParse("database", "db_name")

		self.LOG_BASE_DIR = tryParse("log", "base_dir")
		self.LOG_FILE_NAME = tryParse("log", "file_name")

def tryParse(child, chilchild):
	tree = ET.parse(CONFIG_FILE)
	root = tree.getroot()
	try:
		for tag in root.findall(child):
			x = tag.find(chilchild).text
			if x.lower() in ['yes', 'true', '1', 'y', 'ja']:
				return True
			if x.lower() in ['no', 'false', '0', 'n', 'nej']:
				return False
		#print child + " " + chilchild + " = " + x		
		return x
	except:
		#print "failed to parse " + chilchild + " in " + child
		pass

def wLog(content):
    if os.path.isfile(myECU.LOG_BASE_DIR + myECU.LOG_FILE_NAME) == False:
        print content
        file = open(myECU.LOG_BASE_DIR + myECU.LOG_FILE_NAME, "w")
        #file.write(time.ctime(time.time()) + " - F.TEMP: [" + str(f) + "] - B.TEMP: [" + str(b) + "]---->  " + content + "\n")
        file.write(content)
        file.close()
    else:
        print content
        file = open(myECU.LOG_BASE_DIR + myECU.LOG_FILE_NAME, "a")
        #file.write(time.ctime(time.time()) + " - F.TEMP: [" + str(f) + "] - B.TEMP: [" + str(b) + "]---->  " + content + "\n")
        file.write(content)
        file.close()

def checkHash():
	hasher = hashlib.md5()
	afile = open(CONFIG_FILE, 'rb')
	buf = afile.read()
	hasher.update(buf)
	afile.close()
	return hasher.hexdigest()




while 1:
	myECU = ECU()
	wLog("ny runda")
	C_HASH = checkHash()
	while C_HASH == checkHash():
		print myECU.HW_NAME
		print myECU.IP
		print myECU.BOILER_TEMP_SENSOR_ENABLED
		print myECU.BOILER_TEMP_SENSOR_TYPE
		print myECU.BOILER_TEMP_SENSOR_BASE_DIR
		print myECU.BOILER_TEMP_SENSOR_FILE_NAME
		print myECU.BOILER_TEMP_SENSOR_ID
		time.sleep(1)
		os.system("clear")
		time.sleep(0.2)

"""
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

top = Element('top')

comment = Comment('Generated for PyMOTW')
top.append(comment)

child = SubElement(top, 'child')
child.text = 'This child contains text.'

child_with_tail = SubElement(top, 'child_with_tail')
child_with_tail.text = 'This child has regular text.'
child_with_tail.tail = 'And "tail" text.'

child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
child_with_entity_ref.text = 'This & that'

print tostring(top)

"""