from pymongo import MongoClient

def main():
    client = MongoClient('mongodb://localhost:27017/')
    coll = client['sensors_data']['1']
    coll.insert({
        'value': 1,
        'timestamp': 2,
        'hash': 'adasxzscadqw',
    })


if __name__ == '__main__':
    main()