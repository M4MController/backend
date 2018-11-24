import requests
import json
from datetime import datetime

prefix = 'http://142.93.108.222:5000'
auth_prefix = 'http://142.93.108.222:4999'

def get_token():
    session = requests.Session()
    res = session.post(auth_prefix +'/sign_in', """{
        "e_mail": "demo@mail.ru",
        "password": "0000"
    }""")
    return session, res.text

def create_sensor(controller_id, company_name, sensor_name, sensor_type, date):
    session, token = get_token()
    data = {
      "date" : date.strftime('%Y-%m-%d'),
      "sensor_type": sensor_type,
      "name": sensor_name,
      "company": company_name,
      "controller_id": controller_id
    }
    params = {
        "token": token, 
    }
    resp = session.post(prefix + '/v2/sensor', json=data, params=params)
    res = json.loads(resp.text)

def main():
    #for i in range(1, 130):
    #    create_sensor(i, "Мосэнергосбыт", "Электричество", 1, datetime.now())
    #    create_sensor(i, "Мосводоканал", "Холодная вода", 2, datetime.now())
    #    create_sensor(i, "Мосводоканал", "Горячая вода", 3, datetime.now())
    #    create_sensor(i, "Мосгаз", "Газ", 4, datetime.now())
    
    #Влом добавлять ещё один файлик. Это для разного рода чисток
    session, tok = get_token()
    print(tok)
    for i in range(2, 3):
        #if i == 16:
        #    continue
        res = session.delete("http://142.93.108.222:5000/v2/controller/{}/activate?token={}".format(i,tok))
        #res = session.delete("http://142.93.108.222:5000/v2/object/{}?token={}".format(i,tok))

if __name__ == "__main__":
    main()