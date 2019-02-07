import requests
import unittest
import time
import requests

#prefix = 'http://192.168.39.236:31987'
prefix = 'http://142.93.108.222:5004'


class TestCase(unittest.TestCase):
    #/sensor.addRecord
    # controller_mac: string
    # sensor_id: int
    # value: int
    # timestamp: string
    def test_post_data(self):
        #%Y-%m-%dT%H:%M:%S
        self.app = requests.Session()
        data= """{{
            "controller_mac": "CF-64-93-81-CA-EC",
            "sensor_id": 1,
            "value": 565711,
            "hash": "aaaaaaaaaaa",
            "timestamp": \"{}\"
        }}""".format(time.strftime("%Y-%m-%dT%H:%M:%S"))
        print(time.strftime("%Y-%m-%dT%H:%M:%S"))
        resp = self.app.post(prefix + '/sensor.addRecord', json=data)
        print('/sensor.addRecord\n')
        print(resp.text)



if __name__ == '__main__':
    unittest.main()