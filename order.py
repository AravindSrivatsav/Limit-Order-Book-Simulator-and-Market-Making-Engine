class Order():
    
    def __init__(self,side,quantity,order_id = None, owner_id = None):
        self.order_id = order_id
        self.side = side
        self.quantity = quantity
        self.owner_id = owner_id
    
    def __lt__(self, other):
        if self.side == "BUY":
            if self.price != other.price:
                return self.price > other.price
            return self.order_id < other.order_id
        if self.side == "SELL":
            if self.price != other.price:
                return self.price < other.price
            return self.order_id < other.order_id

class Limit_Order(Order):
    def __init__(self,side,price,quantity,order_id = None,owner_id  = None):
        super().__init__(side,quantity,order_id,owner_id)
        self.price = price
        self.active = True  

class Market_Order(Order):
    pass




    
        




