import socket

import miraclue_low_voltage_monitor.config as config
import miraclue_low_voltage_monitor.util as util

class IT6322A_handler:
    def __init__(self, ip: str, port: int) -> None:
        self._ip = ip
        self._port = port
    
    def _establish_connection(self) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self._ip, self._port))
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    def _send_query(self, query: str) -> str:
        self._establish_connection()
        self._socket.send(query.encode(config.encoding_method))
        response = self._socket.recv(config.buffer_size).decode(config.decoding_method)
        self._socket.close()
        util.tprint(f'send ---> {query}')
        util.tprint(f'recv <--- {response.strip()}')
        return response
    
    def _set_channel(self, channel: int) -> str:
        channel_string = config.channel_list[channel]
        status_code = self._send_query(f'wINST {channel_string}')
        return status_code

    def get_voltage(self, channel: int) -> float:
        self._set_channel(channel)
        voltage = self._send_query('qMEAS?')
        voltage = util.parse_to_float(voltage)
        return voltage

    def get_current(self, channel: int) -> float:
        self._set_channel(channel)
        current = self._send_query('qMEAS:CURR?')
        current = util.parse_to_float(current)
        return current
    
    def set_voltage(self, channel: int, voltage: float) -> str:
        if not -0.1 < voltage < 4:
            util.tprint_error(f'inputted {voltage}V is invalid voltage')
            return "-1"
        self._set_channel(channel)
        voltage = util.parse_to_str(voltage)
        status_code = self._send_query(f'wVOLT {voltage}')
        util.tprint(f'set CH{channel + 1} {voltage}V')
        return status_code

    def get_state(self) -> bool:
        state = self._send_query('qOUTP?')
        state = util.parse_to_int(state)
        return state

    def set_state(self, state: bool) -> str:
        if (state != 0) and (state != 1):
            util.tprint_error(f'inputted command is invalid')
            return "-1"
        status_code = self._send_query(f'wOUTP {state}')
        return status_code