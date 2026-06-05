import random
from order import Order
class Random_Trader:

    def __init__(self,trader_id:int):
        self.trader_id = trader_id
    
    def generate_order(self):
        side = random.choice(["BUY","SELL"])
        price = random.randint(98,102)
        quantity = random.randint(1,10)
        return Order(side,price,quantity)
    

