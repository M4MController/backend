import unittest
from gateway import app


# api.add_resource(UserInfo, '/user/user_info', resource_class_kwargs=args)
# api.add_resource(GetUserControllers, '/controller/get_user_controllers', resource_class_kwargs=args)
# api.add_resource(GetControllerSensors, '/controller/<int:controller_id>/get_sensors', resource_class_kwargs=args)
# api.add_resource(GetControllerStats, '/controller/<int:controller_id>/get_controller_stats', resource_class_kwargs=args)
# api.add_resource(GetSensorData, '/sensor/<int:sensor_id>/view_stats', resource_class_kwargs=args)
# api.add_resource(GetSensorStats, '/sensor/<int:sensor_id>/get_data', resource_class_kwargs=args)

class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_user_info(self):
        resp = self.app.get('/user/user_info')
        print('User Info:\n')
        print(resp.data)

    def test_get_user_controllers(self):
        resp = self.app.get('/controller/get_user_controllers')
        print('User Controllers: \n')
        print(resp.data)
    
    def test_get_conroller_sensors(self):
        resp = self.app.get('/controller/1/get_sensors')
        print('Controller Sensors: \n')
        print(resp.data)

    def test_get_controller_stats(self):
        resp = self.app.get('/controller/1/get_controller_stats')
        print('Controller Stats \n')
        print(resp.data)

    def test_get_sensor_stats(self):
        resp = self.app.get('sensor/1/view_stats')
        print('Sensor Stats\n')
        print(resp.data)
    
    def test_get_sensor_data(self):
        resp = self.app.get('/sensor/1/get_data')
        print('Sensor Data\n')
        print(resp.data)
    
    

if __name__ == '__main__':
    unittest.main()