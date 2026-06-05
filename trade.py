class Trade:
    next_trade_id = 1
    total_volume = 0
    def __init__(self,price,quantity,buyer_id,seller_id,buy_order_id,sell_order_id):
        self.price = price
        self.quantity = quantity
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.buy_order_id = buy_order_id
        self.sell_order_id = sell_order_id
        self.trade_id = Trade.next_trade_id
        Trade.next_trade_id += 1
        Trade.total_volume += quantity
        