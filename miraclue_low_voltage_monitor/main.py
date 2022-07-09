from miraclue_low_voltage_monitor.LowVoltageHandler import LowVoltageHandler
from miraclue_low_voltage_monitor.Monitor import Monitor
import threading

SERIAL_NUMBER = '802071092767310443'
LVH_HOST = 'localhost'
LVH_PORT = 12345

low_vol_handler = LowVoltageHandler(LVH_HOST, LVH_PORT, SERIAL_NUMBER)
monitor = Monitor(LVH_HOST, LVH_PORT, 1)

def exec_low_vol_handler():
	low_vol_handler.start()

def exec_monitor():
	monitor.start()

low_vol_handler_thread = threading.Thread(target=exec_low_vol_handler)
monitor_thread = threading.Thread(target=exec_monitor)

low_vol_handler_thread.start()
monitor_thread.start()