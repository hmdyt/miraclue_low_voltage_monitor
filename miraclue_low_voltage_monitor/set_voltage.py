import argparse
import time

import miraclue_low_voltage_monitor.config as config
from miraclue_low_voltage_monitor.IT6322A_handler import IT6322A_handler

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("v_ch1", type=float)
    parser.add_argument("v_ch2", type=float)
    parser.add_argument("v_ch3", type=float)
    args = parser.parse_args()
    
    handler = IT6322A_handler(
        config.IT6322A_socket_server['IP'],
        config.IT6322A_socket_server['port']
    )
    handler.set_voltage(0, args.v_ch1)
    handler.set_voltage(1, args.v_ch2)
    handler.set_voltage(2, args.v_ch3)
    time.sleep(1)
    voltages = [handler.get_voltage(i) for i in range(3)]
    print(f"current voltages are {voltages}")

if __name__ == '__main__':
    main()
