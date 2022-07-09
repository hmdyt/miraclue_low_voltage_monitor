IT6322A_socket_server = {
    'IP': '10.37.0.146',
    'port': 1234
}
channel_list = ["FIR","SECO","THI"]

base_interval = 1 # [sec]
monitor_interbal = 3 # monitor_interbal * base_interval [sec]
DB_interval = 1 # DB_interval * base_interval [sec]

current_thresholds = [3, 3, 3]
sleep_time = 3

encoding_method = 'utf-8'
decoding_method = 'utf-8'
buffer_size = 1024