from order_book import Order_Book
from order import *
class Market_Maker:

    def __init__(self):
        self.owner_id = "MM"
        self.cash = 0
        self.inventory = 0
        self.last_processed_trade_id = 0
        self.PnL = 0
        self.active_orders = []

    def generate_limit_orders(self,book:Order_Book):
        # Two orders BUY 1 @ Mid_price-1 and SELL 1 @ Mid_price+1
        mid_price = book.compute_mid_price()
        new_buy_order = Limit_Order( "BUY" , mid_price-1 , 2 , owner_id = self.owner_id )
        new_sell_order = Limit_Order( "SELL" , mid_price+1 , 2 , owner_id = self.owner_id )
        self.active_orders.append(new_buy_order)
        self.active_orders.append(new_sell_order)

        return [new_buy_order,new_sell_order]
    
    def generate_market_orders(self):
        
        new_buy_order = Market_Order( "BUY" , 2 , owner_id = self.owner_id )
        new_sell_order = Market_Order( "SELL" , 2 , owner_id = self.owner_id )

        return [new_buy_order,new_sell_order]

    def cancel_prev_orders(self):
        for order in self.active_orders:
            order.active = False 

        self.active_orders.clear()
    
    def process_trades(self,book):
        if not book.trades:
            print("No new trades to be processed")
            return
        for trade in book.trades[self.last_processed_trade_id:]:
            # Check if MM is buyer or seller for any trade
            if trade.buyer_id == "MM":
                self.cash -= (trade.price)*(trade.quantity)
                self.inventory += trade.quantity
            if trade.seller_id == "MM":
                self.cash += (trade.price)*(trade.quantity)
                self.inventory -= trade.quantity
        self.last_processed_trade_id = trade.trade_id

    def compute_PnL(self,book):
        mid_price = book.compute_mid_price()
        self.PnL = self.cash + self.inventory*mid_price
    
    def print_stats(self):
        print(f"cash = {self.cash}\ninventory = {self.inventory}\nPnL = {self.PnL}")

        

