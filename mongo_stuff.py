from pymongo import MongoClient
import subprocess
from PrintException import PrintException as prEx


def db_worker(collection):
    try:
        con = MongoClient()
        con.server_info()
        db = con[collection]
    except:
        subprocess.call(['sudo', 'service', 'mongod', 'restart'])
        db = MongoClient()[collection]
    return db


class MongoReporter:
    def __init__(self):
        self.products_db = db_worker('products')
        self.avg_prices_list = []

    def average_price(self):
        try:

            for avg in self.products_db.aggregate([
                {'$group': {'_id': '$category', 'avg_price': {'$avg': '$price'}}}
            ]):
                self.avg_prices_list.append(avg)
        except:
            print(prEx())
            return {'status': 500,
                    'result': prEx()}
        
        return {'status': 200,
                'result': self.avg_prices_list}
