import requests
import unittest
import pprint
import json

#prefix = 'http://127.0.0.1:8080'
#prefix = 'http://127.0.0.1:5000'
#prefix = 'http://194.58.120.31:80'
#prefix = 'http://142.93.108.222:5000'
prefix = 'http://192.168.39.236:30952'

class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = requests.Session()
        res = self.app.post(prefix +'/user/sign_in', """{
	        "e_mail": "ml@gmail.com",
	        "password": "123456"
        }""")
        #print("login is \n")
        #print(res.url)
        #print(res.text)

    #def test_post_obj(self):
    #    data= {
    #        "adres": "adres",
    #        "name": "name"
    #    }
    #    resp = self.app.post(prefix + '/object/register', json=data)
    #    print('Register Object\n')
    #    pp = pprint.PrettyPrinter()
    #    res = json.loads(resp.text)
    #    pp.pprint(res)
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
        resp = self.app.get(prefix+'/user/user_info')
        print('User Info:\n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        print("```")
        pp.pprint(res)
        print("```")
#
    def test_get_user_controllers(self):
        resp = self.app.get(prefix+'/controller/get_user_controllers')
        print('User Controllers: \n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        print("```")
        pp.pprint(res)
        print("```")
    
    def test_get_conroller_sensors(self):
        resp = self.app.get(prefix+'/controller/1/get_sensors')
        print('Controller Sensors: \n')
        print(resp.url)
        print("```")
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        pp.pprint(res)
        print("```")

    def test_get_controller_stats(self):
        resp = self.app.get(prefix+'/controller/1/get_controller_stats')
        print('Controller Stats \n')
        print(resp.url)
        print("```")
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        pp.pprint(res)
        print("```")


    def test_get_sensor_stats(self):
        resp = self.app.get(prefix+'/sensor/1/view_stats')
        print('Sensor Stats\n')
        print(resp.url)
        print("```")
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        pp.pprint(res)
        print("```")
    
    def test_get_sensor_data(self):
        payload = {
            "limit": 5
        }
        resp = self.app.get(prefix+'/sensor/1/get_data', params=payload)
        print('Sensor Data\n')
        print(resp.url)
        print("```")
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        pp.pprint(res)
        print("```")
    
    def test_get_user_object(self):
        resp = self.app.get(prefix + '/object/get_user_objects')
        print('Get User Objects\n')
        print(resp.url)
        print("```")
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        pp.pprint(res)
        print("```")

    def test_get_obj_controllers(self):
        resp = self.app.get(prefix + '/object/2/get_object_controllers')
        print('Get Object Controllers\n')
        print(resp.url)
        print("```")
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        pp.pprint(res)
        print("```")

# /v2/user/relations
    def test_get_user_relations(self):
        resp = self.app.get(prefix+'/v2/user/relations')
        print('V2 User Relations: \n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        print("```")
        pp.pprint(res) 
        print("```")

    def test_get_object_relations(self):
        resp = self.app.get(prefix+'/v2/object/2/relations')
        print('V2 object Relations: \n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        print("```")
        pp.pprint(res) 
        print("```")

    def test_get_controller_relations(self):
        resp = self.app.get(prefix+'/v2/controller/1/relations')
        print('V2 controller Relations: \n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        print("```")
        pp.pprint(res) 
        print("```")

    def test_get_obj_stats(self):
        resp = self.app.get(prefix + '/object/1/get_object_stats')
        print('Get Object Stats\n')
        print(resp.url)
        pp = pprint.PrettyPrinter()
        res = json.loads(resp.text)
        print("```")
        pp.pprint(res)
        print("```")

if __name__ == '__main__':
    unittest.main()