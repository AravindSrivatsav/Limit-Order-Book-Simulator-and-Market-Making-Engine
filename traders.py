import random
from order import *
# Use OOPS (Object Oriented Programming)
class Trader:
    possible_states = ["BUY","SELL"]
    price_offset = 6
    min_quantity = 1
    max_quantity = 10
    next_trader_id = 1

    def __init__(self,mid_price = 100):
        self.trader_id = self.next_trader_id
        Trader.next_trader_id += 1
        self.mid_price = mid_price
        
    def generate_limit_order(self):
        side = random.choice(self.possible_states)
        price = self.mid_price + random.randint(-self.price_offset,self.price_offset)
        quantity = random.randint(self.min_quantity,self.max_quantity)
        return Limit_Order(side,price,quantity,owner_id = self.trader_id)
    
    def generate_market_order(self):
        side = random.choice(self.possible_states)
        quantity = random.randint(self.min_quantity,self.max_quantity)
        return Market_Order(side,quantity,owner_id = self.trader_id)


class Noise_Trader(Trader):
    pass
    
class Aggressive_Buyer(Trader):
    possible_states = ["BUY"]
    
class Aggressive_Seller(Trader):
    possible_states = ["SELL"]
    
class Large_Trader(Trader):
    min_quantity = 50
    max_quantity = 60
    