IT6322A_socket_server = {
    'IP': '10.37.0.146',
    'port': 1234
}

base_interval = 1  # [sec]
monitor_interbal = 3  # monitor_interbal * base_interval [sec]
DB_interval = 10  # DB_interval * base_interval [sec]

current_thresholds = [100, 4, 4]
sleep_time = 3

database_enabled = False
database_info = {
    'IP': '10.37.0.214',
    'port': 3306,
    'user': 'rubis',
    'password': 'password',
    'dbname': 'IT6332A',
    'table': 'IT6332A_1'
}

set_voltages = [0, 2.5, 2.5]  # [V]

channel_list = ["FIR", "SECO", "THI"]
encoding_method = 'utf-8'
decoding_method = 'utf-8'
buffer_size = 1024

log_file = './log'
log_file_max = '1 GB'
logfile_loglevel = 'DEBUG'
stdout_loglevel = 'INFO'
