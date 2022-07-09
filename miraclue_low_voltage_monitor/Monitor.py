import time
from typing import List
import miraclue_low_voltage_monitor.config as config
import miraclue_low_voltage_monitor.util as util
from miraclue_low_voltage_monitor.IT6322A_handler import IT6322A_handler

class Monitor:
    def __init__(self, current_thresholds: List[float], sleep_time: int) -> None:
        self._current_thresholds = current_thresholds
        self._sleep_time = sleep_time
        self._handler = IT6322A_handler(
            config.IT6322A_socket_server['IP'],
            config.IT6322A_socket_server['port']
        )

    def check_current(self, currents) -> None:
        util.tprint('start checking current')
        is_exceed = False
        for (th_current, current) in zip(self._current_thresholds, currents):
            if current > th_current:
                is_exceed = True
        if is_exceed:
            util.tprint(f'exceed software current limit!')
            util.tprint(f'current: {currents}, th_current: {self._current_thresholds}')
            self._sleep()
        else:
            util.tprint(f'currents are normal')
   
    def _sleep(self) -> None:
        self._handler.set_state(0)
        time.sleep(self._sleep_time)
        self._handler.set_state(1)