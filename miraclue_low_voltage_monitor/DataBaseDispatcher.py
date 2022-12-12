import pymysql
from loguru import logger
import miraclue_low_voltage_monitor.util as util
import miraclue_low_voltage_monitor.config as config


class DataBaseDispatcher:
    def __init__(self, dbinfo: dict) -> None:
        if config.database_enabled:
            self._ip = dbinfo['IP']
            self._port = dbinfo['port']
            self._user = dbinfo['user']
            self._password = dbinfo['password']
            self._dbname = dbinfo['dbname']
            self._table = dbinfo['table']
            self._establish_connection()
        else:
            logger.warning("DB is now disabled")

    def _establish_connection(self) -> None:
        self._db_connection = pymysql.connect(
            host=self._ip,
            port=self._port,
            user=self._user,
            passwd=self._password,
        )
        self._cursor = self._db_connection.cursor()
        self._cursor.execute(f'USE {self._dbname}')

    def insert(self, voltages, currents) -> None:
        if config.database_enabled:
            sql_query = f"insert into {self._table}(ch1,ch2,ch3,ch4,ch5,ch6) values(%s, %s, %s, %s, %s, %s)"
            query_tuple = []
            for i in range(3):
                query_tuple.append(str(voltages[i]))
                query_tuple.append(str(currents[i]))
            query_tuple = tuple(query_tuple)
            self._cursor.execute(sql_query, query_tuple)
            self._db_connection.commit()
            logger.success('save to DB')
        else:
            logger.warning("DB is now disabled")
