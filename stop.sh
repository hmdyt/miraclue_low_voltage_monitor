#!/usr/bin/bash
docker-compose exec -T monitor poetry run python miraclue_low_voltage_monitor/set_voltage.py 0 0 0
docker-compose down