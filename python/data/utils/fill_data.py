from pymongo import MongoClient
from data_model.sensor_data import SensorDataModel
import random
from datetime import datetime
from datetime import timedelta
import argparse
import string

def insert_data(client, maxdata, data_delta, data_random, num, sensor_id, mac, sensor_type):
    time_delta = timedelta(days=-1)
    data_model = SensorDataModel(client)
    curr_data = maxdata
    ts = datetime.now()
    for i in range(0, num):
        curr_delta = data_delta + random.uniform(-data_random, data_random)
        curr_data -= curr_delta
        ts += time_delta
        data_template = dict(
            controller_mac=mac,
            sensor_id=sensor_id,
            value=curr_data,
            hash="HASH",
            timestamp=ts.strftime('%Y-%m-%dT%H:%M:%S'),
        )
        data_model.insert_data(data_template, sensor_type=sensor_type)

def insert_raw_data(client, sensor_id, mac, num, datasize=10):
    time_delta = timedelta(days=-1)
    data_model = SensorDataModel(client)
    ts = datetime.now()
    for i in range(0, num):
        curr_data = ''.join(random.choices(string.ascii_uppercase + string.digits, k=datasize))
        ts += time_delta
        data_template = dict(
            controller_mac=mac,
            sensor_id=sensor_id,
            value=curr_data,
            hash="HASH",
            timestamp=ts.strftime('%Y-%m-%dT%H:%M:%S'),
        )
        data_model.insert_data(data_template, sensor_type=0)

def drop_data(client):
    client.drop_database(SensorDataModel._DATABASE_NAME)

def main():
    parser = argparse.ArgumentParser(description='Сгенерировать данные')
    parser.add_argument('--connection', '-c', type=str, default="localhost:27017", help='часть для connection string')
    parser.add_argument('--number', '-n', type=int, default=1, help='Количество комплектов сенсоров')
    args = parser.parse_args()
    time_delta = timedelta(days=-1)
    maxdata = 99999
    data_delta = 400/30
    data_random = 50/30
    num = 730
    client = MongoClient('mongodb://{}/'.format(args.connection))
    drop_data(client)
    num_in_pack = 730
    for ind in range(0, args.number):
        base = ind * 5
        insert_data(
            client=client,
            maxdata=11111,
            data_delta=400/30,
            data_random=50/30,
            num=num_in_pack,
            sensor_id=base+1,
            mac="6b:45:cd:97:41:48",
            sensor_type=1,
        )

        insert_data(
            client=client,
            maxdata=3000,
            data_delta=8.9/30,
            data_random=0.7/30,
            num=num_in_pack,
            sensor_id=base+2,
            mac="6b:45:cd:97:42:48",
            sensor_type=2,
        )

        insert_data(
            client=client,
            maxdata=3000,
            data_delta=8.9/30,
            data_random=0.7/30,
            num=num_in_pack,
            sensor_id=base+3,
            mac="6b:45:cd:97:43:48",
            sensor_type=3,
        )
        
        insert_data(
            client=client,
            maxdata=3000,
            data_delta=120/30,
            data_random=20/30,
            num=num_in_pack,
            sensor_id=base+4,
            mac="6b:45:cd:97:44:48",
            sensor_type=4,
        )

        insert_raw_data(
            client=client,
            sensor_id=base+5,
            mac="6b:45:cd:97:45:48",
            num=num_in_pack
        )
    

if __name__ == '__main__':
    main()