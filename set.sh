#!/usr/bin/bash

docker-compose exec -T monitor poetry run python miraclue_low_voltage_monitor/set_voltage.py --state 1 $1 $2 $3
