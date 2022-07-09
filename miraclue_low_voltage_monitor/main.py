from miraclue_low_voltage_monitor.IT6322A_handler import IT6322A_handler
from miraclue_low_voltage_monitor.DataBaseDispatcher import DataBaseDispatcher
from miraclue_low_voltage_monitor.Monitor import Monitor
import miraclue_low_voltage_monitor.util as util
import miraclue_low_voltage_monitor.config as config
import time
import signal
import sys

def init():
	handler = IT6322A_handler(
		config.IT6322A_socket_server['IP'],
		config.IT6322A_socket_server['port']
	)
	monitor = Monitor(
		config.current_thresholds,
		config.sleep_time
	)
	dispatcher = DataBaseDispatcher(config.database_info)
	return handler, monitor, dispatcher

def init_voltages(handler):
	for i in range(3):
		handler.set_voltage(i, config.set_voltages[i])
	handler.set_state(1)

def start(handler, monitor, dispatcher):
	counter = 0
	a_cycle = config.base_interval * config.monitor_interbal * config.DB_interval
	while True:
		voltages = [handler.get_voltage(i) for i in range(3)]
		currents = [handler.get_current(i) for i in range(3)]
		util.tprint(f'voltages: {voltages}')
		util.tprint(f'currents: {currents}')

		if counter % config.monitor_interbal == 0:
			monitor.check_current(currents)
		if counter % config.DB_interval == 0:
			dispatcher.insert(voltages, currents)

		counter += 1
		if counter % a_cycle == 0:
			counter = 0
		time.sleep(config.base_interval)

def main():
	handler, monitor, dispatcher = init()
	init_voltages(handler)
	start(handler, monitor, dispatcher)

if __name__ == '__main__':
	main()
