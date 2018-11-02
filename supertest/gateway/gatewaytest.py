import requests
import unittest
import pprint
import json

#prefix = 'http://127.0.0.1:8080'
#prefix = 'http://127.0.0.1:5000'
#prefix = 'http://194.58.120.31:80'
#prefix = 'http://142.93.108.222:5000'
prefix = 'http://192.168.39.236:30952'
auth_prefix = 'http://192.168.39.236:30953'

class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = requests.Session()
        res = self.app.post(auth_prefix +'/sign_in', """{
	        "e_mail": "ml@gmail.com",
	        "password": "123456"
        }""")
        self.token = res.text
        #print("login is \n")
        #print(res.url)
        #print(res.text)

    def test_post_obj(self):
        data= {
            "name": "MyTestObjectName",
            "address": "MyTestObjectAddress"
        }
        params = {
            "token": self.token, 
        }
        resp = self.app.post(prefix + '/v2/object', json=data, params=params)
        print('Register Object\n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        print("```")
        pp.pprint(res)
        print("```")

    def controler_create(self):
        data= {
          "mac": "D5-F6-60-DC-D3-EE",
          "controller_type": 1
        }
        params = {
            "token": self.token, 
        }
        resp = self.app.post(prefix + '/v2/controller', json=data, params=params)
        res = json.loads(resp.text)
        print('Register Controller\n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        print("```")
        pp.pprint(res)
        print("```")
        return res["msg"]["id"]

    def controller_activate(self, id):
        data= {
           "name": "Новый контроллер",
           "meta": "Мета нового контроллера",
            "object_id": 1
        }
        params = {
            "token": self.token, 
        }
        resp = self.app.post(prefix + '/v2/controller/{}/activate'.format(id), json=data, params=params)
        res = json.loads(resp.text)
        print('Activate Controller\n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        print("```")
        pp.pprint(res)
        print("```")

    def test_create_controller(self):
        _id = self.controler_create()
        self.controller_activate(_id)

    def test_create_sensor(self):
        data = {
          "date" : "2018-11-1",
          "sensor_type": 1,
          "name": "Имясенсора",
          "company": "Имякомпании",
          "controller_id": 1
        }
        params = {
            "token": self.token, 
        }
        resp = self.app.post(prefix + '/v2/sensor', json=data, params=params)
        res = json.loads(resp.text)
        print('Create Sensor\n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        print("```")
        pp.pprint(res)
        print("```")
#
    #def test_post_controller(self):
    #    data={
    #        "id": 2,
    #        "object_id": 1,
    #        "name": "somename",
    #        "meta": "somemeta"
    #    }
    #    resp = self.app.post(prefix + '/controller/register', json=data)
    #    print('Register Controller\n')
    #    pp = pprint.PrettyPrinter()
    #    res = json.loads(resp.text)
    #    pp.pprint(res)
    #
    #def test_post_sensor(self):
    #    data={
    #        "controller_id" : 1,
    #        "id" : 2,
    #        "name": "sensorname",
    #        "company": "company"
    #    }
    #    resp = self.app.post(prefix + '/sensor/register', json=data)
    #    print('Register Sensor\n')
    #    pp = pprint.PrettyPrinter()
    #    res = json.loads(resp.text)
    #    pp.pprint(res)
#
    def test_user_info(self):
        params = {
            "token": self.token, 
        }
        resp = self.app.get(prefix+'/user/user_info', params=params)
        print('User Info:\n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        print("```")
        pp.pprint(res)
        print("```")
#
    def test_get_user_controllers(self):
        params = {
            "token": self.token, 
        }
        resp = self.app.get(prefix+'/controller/get_user_controllers', params=params)
        print('User Controllers: \n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        print("```")
        pp.pprint(res)
        print("```")
    
    def test_get_conroller_sensors(self):
        params = {
            "token": self.token, 
        }
        resp = self.app.get(prefix+'/controller/1/get_sensors', params=params)
        print('Controller Sensors: \n')
        print(resp.url)
        print("```")
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        pp.pprint(res)
        print("```")

    def test_get_controller_stats(self):
        params = {
            "token": self.token, 
        }
        resp = self.app.get(prefix+'/controller/1/get_controller_stats', params=params)
        print('Controller Stats \n')
        print(resp.url)
        print("```")
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        pp.pprint(res)
        print("```")


    def test_get_sensor_stats(self):
        params = {
            "token": self.token, 
        }
        resp = self.app.get(prefix+'/sensor/1/view_stats', params=params)
        print('Sensor Stats\n')
        print(resp.url)
        print("```")
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        pp.pprint(res)
        print("```")
    
    def test_get_sensor_data(self):
        params = {
            "token": self.token,
            "limit": 5
        }
        resp = self.app.get(prefix+'/sensor/1/get_data', params=params)
        print('Sensor Data\n')
        print(resp.url)
        print("```")
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        pp.pprint(res)
        print("```")
    
    def test_get_user_object(self):
        params = {
            "token": self.token, 
        }
        resp = self.app.get(prefix + '/object/get_user_objects', params=params)
        print('Get User Objects\n')
        print(resp.url)
        print("```")
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        pp.pprint(res)
        print("```")

    def test_get_obj_controllers(self):
        params = {
            "token": self.token, 
        }
        resp = self.app.get(prefix + '/object/1/get_object_controllers', params=params)
        print('Get Object Controllers\n')
        print(resp.url)
        print("```")
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        pp.pprint(res)
        print("```")

# /v2/user/relations
    def test_get_user_relations(self):
        params = {
            "token": self.token, 
        }
        resp = self.app.get(prefix+'/v2/user/relations', params=params)
        print('V2 User Relations: \n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        print("```")
        pp.pprint(res) 
        print("```")

    def test_get_object_relations(self):
        params = {
            "token": self.token, 
        }
        resp = self.app.get(prefix+'/v2/object/1/relations', params=params)
        print('V2 object Relations: \n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        print("```")
        pp.pprint(res) 
        print("```")

    def test_get_controller_relations(self):
        params = {
            "token": self.token, 
        }
        resp = self.app.get(prefix+'/v2/controller/1/relations', params=params)
        print('V2 controller Relations: \n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        print("```")
        pp.pprint(res) 
        print("```")

    def test_get_obj_stats(self):
        params = {
            "token": self.token, 
        }
        resp = self.app.get(prefix + '/object/1/get_object_stats', params=params)
        print('Get Object Stats\n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        print("```")
        pp.pprint(res)
        print("```")

    def test_get_obj_stats(self):
        params = {
            "token": self.token,
            "from": "2018-10-01T17:40:45",
            "to": "2018-10-05T17:40:45"
        }
        resp = self.app.get(prefix + '/v2/sensor/1/get_data_period', params=params)
        print('Get Sensor Data by period\n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        print("```")
        pp.pprint(res)
        print("```")

if __name__ == '__main__':
    unittest.main()