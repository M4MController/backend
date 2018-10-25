from pymongo import MongoClient
from data_model.sensor_data import SensorDataModel
import random
from datetime import datetime
from datetime import timedelta

def insert_data(client, maxdata, data_delta, data_random, num, sensor_id, mac):
    time_delta = timedelta(days=-1)
    #client = MongoClient('mongodb://192.168.39.236:30261/')
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
        data_model.insert_data(data_template)

def main():
    time_delta = timedelta(days=-1)
    maxdata = 99999
    data_delta = 400/30
    data_random = 50/30
    num = 730
    #client = MongoClient('mongodb://192.168.39.236:30261/')
    client = MongoClient('mongodb://localhost:27017/')
    insert_data(
        client=client,
        maxdata = 11111,
        data_delta = 400/30,
        data_random = 50/30,
        num = 730,
        sensor_id=1,
        mac="6b:45:cd:97:41:48",
    )

    insert_data(
        client=client,
        maxdata = 3000,
        data_delta = 8.9/30,
        data_random = 0.7/30,
        num = 730,
        sensor_id=2,
        mac="6b:45:cd:97:42:48",
    )

    insert_data(
        client=client,
        maxdata = 3000,
        data_delta = 8.9/30,
        data_random = 0.7/30,
        num = 730,
        sensor_id=3,
        mac="6b:45:cd:97:43:48",
    )

    insert_data(
        client=client,
        maxdata = 3000,
        data_delta = 120/30,
        data_random = 20/30,
        num = 730,
        sensor_id=4,
        mac="6b:45:cd:97:44:48",
    )

if __name__ == '__main__':
    main()