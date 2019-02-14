from core.base import BaseReceiverTest
import time

class TestCase(BaseReceiverTest):
    def test_ping(self):
        result = self.receiver.get('/ping')
        print(result)
        assert result.json() == { 
            "ok": True
        }
    
    def test_send_data(self):
        data= {
            "controller_mac": "CF-64-93-81-CA-EC",
            "sensor_id": 1,
            "value": 565711,
            "hash": "aaaaaaaaaaa",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
        }
        result = self.receiver.post(
            '/sensor.addRecord',
            json=data
        )
        assert result.json() == { 
            "ok": True
        }

    def test_send_bad_data(self):
        data= {
            "controller_mac": "CF-64-93-81-CA-EC",
            "sensor_id": "a",
            "value": 565711,
            "hash": "aaaaaaaaaaa",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
        }
        result = self.receiver.post(
            '/sensor.addRecord',
            json=data
        )
        print(result)
        assert result.json() == { 
            "ok": False,
            "errors": {
                "sensor_id": [
                  "Not a valid integer."
                ]
            }
        }
        assert result.code == 400
