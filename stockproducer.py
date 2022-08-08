from faker.providers import BaseProvider
import random
from yahoo_fin import stock_info as si
from datetime import datetime

StockNames = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'ADA-USD', 'DOGE-USD']

class StockProvider(BaseProvider):

    def stock_name(self):
        return random.choice(StockNames)

    def stock_value(self, stockname):
        nextval=si.get_live_price(stockname)  
        return nextval

    
    def produce_msg(self):
        stockname =self.stock_name()

        # get current datetime
        today = datetime.now()

        # Get current ISO 8601 datetime in string format
        iso_date = today.isoformat()
        message = {
            'stock_name': stockname,
            'stock_value': self.stock_value(stockname),
            'timestamp': iso_date
        }
        key = {'stock_name': stockname}
        return message, key