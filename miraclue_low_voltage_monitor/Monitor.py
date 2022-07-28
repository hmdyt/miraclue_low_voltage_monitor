import time
from typing import List
from loguru import logger
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
        logger.info('start checking current')
        is_exceed_chs = [
            current > th_current for (th_current, current) in zip(self._current_thresholds, currents)
        ]
        for i, is_exceed in enumerate(is_exceed_chs):
            ch = i + 1
            if is_exceed:
                logger.warning(f'exceed software current limit! (ch{ch})')
                self._sleep(i)
            else:
                logger.success(f'ch {ch} current is normal')
   
    def _sleep(self, i) -> None:
        # i means channel - 1 (0-indexed)
        logger.warning(f'sleep ch{i + 1} {self._sleep_time} sec')
        self._handler.set_voltage(i, 0)
        time.sleep(self._sleep_time)
        self._handler.set_voltage(i, config.set_voltages[i])