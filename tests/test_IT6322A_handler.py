from miraclue_low_voltage_monitor.IT6322A_handler import IT6322A_handler
import miraclue_low_voltage_monitor.config as config
import time

def _init_handler():
    handler = IT6322A_handler(
        config.IT6322A_socket_server['IP'],
        config.IT6322A_socket_server['port']
        )
    return handler

def test_method_query():
    handler = _init_handler()
    res1 = handler._send_query('q*IDN?')
    res2 = handler._send_query('q*IDN?')
    assert res1 == 'ITECH Ltd., IT6332A, 802071092767310443, 1.11-1.08\n'
    assert res2 == 'ITECH Ltd., IT6332A, 802071092767310443, 1.11-1.08\n'

def test_set_channel():
    handler = _init_handler()
    for i in range(3):
        handler._set_channel(i)
        assert handler._send_query('qINST?').strip() == f'CH{i+1}'

def test_get_voltage():
    handler = _init_handler()
    res1 = handler.get_voltage(0)
    res2 = handler.get_voltage(1)
    res3 = handler.get_voltage(2)
    assert type(res1) == float
    assert type(res2) == float
    assert type(res3) == float

def test_get_current():
    handler = _init_handler()
    res1 = handler.get_current(0)
    res2 = handler.get_current(1)
    res3 = handler.get_current(2)
    assert type(res1) == float
    assert type(res2) == float
    assert type(res3) == float

def test_get_voltage():
    handler = _init_handler()
    res = handler.get_state()
    assert (res == 0) or (res == 1)

def test_set_voltage():
    handler = _init_handler()
    handler.set_state(0)
    assert handler.get_state() == 0

def test_method_set_voltage():
    handler = _init_handler()
    for i in range(3):
        handler.set_voltage(i, 0.1)
    handler.set_state(1)
    time.sleep(1)
    for i in range(3):
        assert 1e-3 < handler.get_voltage(i) < 0.3
    handler.set_state(0)
    assert 0 == handler.get_state()