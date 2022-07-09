from miraclue_low_voltage_monitor.IT6322A_handler import IT6322A_handler
from miraclue_low_voltage_monitor.Monitor import Monitor
import miraclue_low_voltage_monitor.util as util
import miraclue_low_voltage_monitor.config as config
import time

handler = IT6322A_handler(
	config.IT6322A_socket_server['IP'],
	config.IT6322A_socket_server['port']
)
monitor = Monitor(
	config.current_thresholds,
	config.sleep_time
)

counter = 0
a_cycle = config.base_interval * config.monitor_interbal * config.DB_interval

while True:
	voltages = [handler.get_voltage(i) for i in range(3)]
	currents = [handler.get_current(i) for i in range(3)]
	util.tprint(f'voltages: {voltages}')
	util.tprint(f'currents: {currents}')

	if counter % config.monitor_interbal == 0:
		monitor.check_current(currents)

	counter += 1
	if counter % a_cycle == 0:
		counter = 0
	time.sleep(config.base_interval)