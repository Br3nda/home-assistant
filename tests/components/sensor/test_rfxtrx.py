"""
tests.components.sensor.test_rfxtrx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests Rfxtrx sensor.
"""

import unittest


from homeassistant.components.sensor import rfxtrx
from homeassistant.components import rfxtrx as rfxtrx_core
from homeassistant.const import TEMP_CELCIUS

from tests.common import get_test_home_assistant

class TestSensorRfxtrx(unittest.TestCase):
    """ Test the Rfxtrx sensor. """

    def setup_method(self, method):
        """ setup hass """
        self.hass = get_test_home_assistant(0)

    def teardown_method(self, method):
        """ Stop down stuff we started. """
        self.hass.stop()

    def test_default_config(self):
        """ Test with 0 sensors """
        config = {'devices': {}}
        devices = []

        def add_dev_callback(devs):
            """ callback to add device """
            for dev in devs:
                devices.append(dev)

        rfxtrx.setup_platform(self.hass, config, add_dev_callback)
        self.assertEqual(0, len(devices))

    def test_one_sensor(self):
        """ Test with 1 sensor """
        config = {'devices':
                  {'sensor_0502': {
                      'name': 'Test',
                      'packetid': '0a52080705020095220269',
                      'data_type': 'Temperature'}}}
        devices = []

        def add_dev_callback(devs):
            """ callback to add device """
            for dev in devs:
                devices.append(dev)

        rfxtrx.setup_platform(self.hass, config, add_dev_callback)

        self.assertEqual(1, len(devices))
        entity = devices[0]
        self.assertEqual('Test', entity.name)
        self.assertEqual(TEMP_CELCIUS, entity.unit_of_measurement)
        self.assertEqual(14.9, entity.state)
        self.assertEqual({'Humidity status': 'normal', 'Temperature': 14.9,
                          'Rssi numeric': 6, 'Humidity': 34,
                          'Battery numeric': 9,
                          'Humidity status numeric': 2},
                         entity.device_state_attributes)

    def test_one_sensor2(self):
        """ Test with 1 sensor """
        config = {'devices':
                  {'sensor_0502': {
                      'name': 'Test',
                      'packetid': '0a52080705020095220269',
                      'data_type': 'Temperature'}}}
        devices = []

        def add_dev_callback(devs):
            """ callback to add device """
            for dev in devs:
                devices.append(dev)

        rfxtrx.setup_platform(self.hass, config, add_dev_callback)

        self.assertEqual(1, len(devices))
        entity = devices[0]
        self.assertEqual('Test', entity.name)
        self.assertEqual(TEMP_CELCIUS, entity.unit_of_measurement)
        self.assertEqual(14.9, entity.state)
        self.assertEqual({'Humidity status': 'normal', 'Temperature': 14.9,
                          'Rssi numeric': 6, 'Humidity': 34,
                          'Battery numeric': 9,
                          'Humidity status numeric': 2},
                         entity.device_state_attributes)

#    def test_several_sensors(self):
#        """ Test with 3 sensors """
#        config = {'devices':
#                  {'sensor_0502': {
#                      'name': 'Test',
#                      'packetid': '0a52080705020095220269',
#                      'data_type': 'Temperature'},
#                   'sensor_0601': {
#                       'name': 'Bath_Humidity',
#                       'packetid': '0a520802060100ff0e0269',
#                       'data_type': 'Humidity'},
#                   'sensor_0601 2': {
#                       'name': 'Bath',
#                       'packetid': '0a520802060100ff0e0269'}}}
#        devices = []
#
#        def add_dev_callback(devs):
#            """ callback to add device """
#            for dev in devs:
#                devices.append(dev)
#
#        rfxtrx.setup_platform(self.hass, config, add_dev_callback)
#
#        self.assertEqual(3, len(devices))
#        device_num = 0
#        for entity in devices:
#            if entity.name == 'Bath_Humidity':
#                device_num = device_num + 1
#                self.assertEqual('%', entity.unit_of_measurement)
#                self.assertEqual(14, entity.state)
#                self.assertEqual({'Battery numeric': 9, 'Temperature': 25.5,
#                                  'Humidity': 14, 'Humidity status': 'normal',
#                                  'Humidity status numeric': 2,
#                                  'Rssi numeric': 6},
#                                 entity.device_state_attributes)
#                self.assertEqual('Bath_Humidity', entity.__str__())
#            elif entity.name == 'Bath':
#                device_num = device_num + 1
#                self.assertEqual(TEMP_CELCIUS, entity.unit_of_measurement)
#                self.assertEqual(25.5, entity.state)
#                self.assertEqual({'Battery numeric': 9, 'Temperature': 25.5,
#                                  'Humidity': 14, 'Humidity status': 'normal',
#                                  'Humidity status numeric': 2,
#                                  'Rssi numeric': 6},
#                                 entity.device_state_attributes)
#                self.assertEqual('Bath', entity.__str__())
#            elif entity.name == 'Test':
#                device_num = device_num + 1
#                self.assertEqual(TEMP_CELCIUS, entity.unit_of_measurement)
#                self.assertEqual(14.9, entity.state)
#                self.assertEqual({'Humidity status': 'normal',
#                                  'Temperature': 14.9,
#                                  'Rssi numeric': 6, 'Humidity': 34,
#                                  'Battery numeric': 9,
#                                  'Humidity status numeric': 2},
#                                 entity.device_state_attributes)
#                self.assertEqual('Test', entity.__str__())
#
#        self.assertEqual(3, device_num)
#
#    def test_discover_sensor(self):
#        """ Test with discover of sensor """
#        config = {'devices': {}}
#        devices = []
#
#        def add_dev_callback(devs):
#            """ callback to add device """
#            for dev in devs:
#                devices.append(dev)
#
#        rfxtrx.setup_platform(self.hass, config, add_dev_callback)
#        self.assertEqual(0, len(devices))
#        event = rfxtrx_core.get_rfx_object('0a520801070100b81b0279')        
#        event.data = bytearray(b'\nR\x08\x01\x07\x01\x00\xb8\x1b\x02y')
#
#        self.assertEqual(0, len(rfxtrx_core.RFX_DEVICES))        
#        rfxtrx_core.RECEIVED_EVT_SUBSCRIBERS[0](event)
#        self.assertEqual(1, len(rfxtrx_core.RFX_DEVICES))
#
#        rfxtrx_core.RECEIVED_EVT_SUBSCRIBERS[0](event)
#        self.assertEqual(1, len(rfxtrx_core.RFX_DEVICES))
#
#    def test_discover_sensor_no_auto_add(self):
#        """ Test with discover of sensor when auto add is False """
#        config = {'automatic_add': False, 'devices': {}}
#        devices = []
#
#        print("\n\n\n\n\n\n")
#        def add_dev_callback(devs):
#            """ callback to add device """
#            for dev in devs:
#                devices.append(dev)
#
#        rfxtrx.setup_platform(self.hass, config, add_dev_callback)
#        self.assertEqual(0, len(devices))
#        event = rfxtrx_core.get_rfx_object('0a520801070100b81b0279')        
#        event.data = bytearray(b'\nR\x08\x01\x07\x01\x00\xb8\x1b\x02y')
#
#        self.assertEqual(0, len(rfxtrx_core.RFX_DEVICES))        
#        rfxtrx_core.RECEIVED_EVT_SUBSCRIBERS[0](event)
#        self.assertEqual(0, len(rfxtrx_core.RFX_DEVICES))
#
#        rfxtrx_core.RECEIVED_EVT_SUBSCRIBERS[0](event)
#        self.assertEqual(0, len(rfxtrx_core.RFX_DEVICES))
