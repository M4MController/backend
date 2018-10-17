from pymongo import MongoClient
from data_model.sensor_data import SensorDataModel
import random
from datetime import datetime
from datetime import timedelta


def main():
    time_delta = timedelta(days=-1)
    maxdata = 99999
    data_delta = 400/30
    data_random = 50/30
    num = 730
    #client = MongoClient('mongodb://192.168.39.236:30261/')
    #client = MongoClient('mongodb://localhost:30261/')
    data_model = SensorDataModel(client)
    curr_data = maxdata
    ts = datetime.now()
    for i in range(0, num):
        curr_delta = data_delta + random.randint(-data_random, data_random)
        curr_data -= curr_delta
        ts += time_delta
        data_template = dict(
            controller_mac="6b:45:cd:97:48:48",
            sensor_id=1,
            value=curr_data,
            hash="HASH",
            timestamp=ts.strftime('%Y-%m-%dT%H:%M:%S'),
        )
        data_model.insert_data(data_template)


if __name__ == '__main__':
    main()