from mongo_stuff import db_worker


class CheckPrice:
    def __init__(self):
        self.products_db = db_worker('products')

    def check_price(self):
        pass
