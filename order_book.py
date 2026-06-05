import heapq
from order import *
from trade import Trade
class Order_Book:

    def __init__(self):
        self.buy_orders = [] # Highest Bid first, earlier time first
        self.sell_orders = [] # Lowest Ask first, earlier time first
        self.trades = [] # Stores the trades hitsory
        self.next_order_id = 1

    def add_order(self,order:Order):
        if order.quantity == 0:
            return 
        if order.order_id == None:
            order.order_id = self.next_order_id
            self.next_order_id += 1
        if type(order) == Limit_Order:
            if order.side == "BUY":
                self.match_buy_order(order)
            else:
                self.match_sell_order(order)
            return 
        elif type(order) == Market_Order:
            if order.side == "BUY":
                self.match_market_buy_order(order)
            else:
                self.match_market_sell_order(order)
    
    def match_buy_order(self,order:Limit_Order):
        if order.quantity == 0:
            return        
        # Remove non active orders
        while self.sell_orders and not self.sell_orders[0].active:
            heapq.heappop(self.sell_orders)
        # If both orders are from same trader pop the best order temporarily.
        sell_temp = []
        while self.sell_orders and order.owner_id == self.sell_orders[0].owner_id:
            sell_temp.append(heapq.heappop(self.sell_orders))
        if not self.sell_orders:
            heapq.heappush(self.buy_orders,order)
            while sell_temp:
                heapq.heappush(self.sell_orders,sell_temp.pop())
            return
        best_sell_order = self.sell_orders[0]
        # Buy_price >= Best Ask then trade
        if order.price >= best_sell_order.price: # Matched
            # Trade 
            if order.quantity < best_sell_order.quantity:
                self.trades.append(Trade(best_sell_order.price,order.quantity,order.owner_id,best_sell_order.owner_id,order.order_id,best_sell_order.order_id))
                best_sell_order.quantity -= order.quantity 
       
            else:
                order.quantity -= best_sell_order.quantity
                self.trades.append(Trade(best_sell_order.price,best_sell_order.quantity,order.owner_id,best_sell_order.owner_id,order.order_id,best_sell_order.order_id))
                heapq.heappop(self.sell_orders)
                self.match_buy_order(order)
        else:
            heapq.heappush(self.buy_orders,order)

        while sell_temp:
            heapq.heappush(self.sell_orders,sell_temp.pop())

    def match_sell_order(self,order:Limit_Order):
        if order.quantity == 0:
            return
        # Remove non-active orders
        while self.buy_orders and not self.buy_orders[0].active:
            heapq.heappop(self.buy_orders)
        buy_temp = []
        while self.buy_orders and order.owner_id == self.buy_orders[0].owner_id:
            buy_temp.append(heapq.heappop(self.buy_orders))
        if not self.buy_orders:
            heapq.heappush(self.sell_orders,order)
            while buy_temp:
                heapq.heappush(self.buy_orders,buy_temp.pop())
            return
        best_buy_order = self.buy_orders[0]
        
        # Sell_price <= Best buy bid price then trade        
        if order.price <= best_buy_order.price: # Trade
            # You can do full trade
            if order.quantity < best_buy_order.quantity:
                best_buy_order.quantity -= order.quantity
                self.trades.append(Trade(best_buy_order.price,order.quantity,best_buy_order.owner_id,order.owner_id,best_buy_order.order_id,order.order_id))
            # Partial fill add the new sell order to the book.
            else:
                self.trades.append(Trade(best_buy_order.price,best_buy_order.quantity,best_buy_order.owner_id,order.owner_id,best_buy_order.order_id,order.order_id))
                order.quantity -= best_buy_order.quantity
                heapq.heappop(self.buy_orders)
                self.match_sell_order(order)
        else:
            heapq.heappush(self.sell_orders,order)

        while buy_temp:
            heapq.heappush(self.buy_orders,buy_temp.pop())

    def match_market_buy_order(self,order:Market_Order):
        if order.quantity == 0:
            return        
        # Remove non active orders
        while self.sell_orders and not self.sell_orders[0].active:
            heapq.heappop(self.sell_orders)
        # If both orders are from same trader pop the best order temporarily.
        sell_temp = []
        while self.sell_orders and order.owner_id == self.sell_orders[0].owner_id:
            sell_temp.append(heapq.heappop(self.sell_orders))    
        if not self.sell_orders:
            while sell_temp:
                heapq.heappush(self.sell_orders,sell_temp.pop())
            return    
        # Price doesn't matter
        best_sell_order = self.sell_orders[0]
        # Auto match
        if order.quantity < best_sell_order.quantity:
            self.trades.append(Trade(best_sell_order.price,order.quantity,order.owner_id,best_sell_order.owner_id,order.order_id,best_sell_order.order_id))
            best_sell_order.quantity -= order.quantity 
        else:
            order.quantity -= best_sell_order.quantity
            self.trades.append(Trade(best_sell_order.price,best_sell_order.quantity,order.owner_id,best_sell_order.owner_id,order.order_id,best_sell_order.order_id))
            heapq.heappop(self.sell_orders)
            self.match_market_buy_order(order)  

        while sell_temp:
            heapq.heappush(self.sell_orders,sell_temp.pop())  

    def match_market_sell_order(self,order:Market_Order):
        if order.quantity == 0:
            return
        # Remove non-active orders
        while self.buy_orders and not self.buy_orders[0].active:
            heapq.heappop(self.buy_orders)
        buy_temp = []
        while self.buy_orders and order.owner_id == self.buy_orders[0].owner_id:
            buy_temp.append(heapq.heappop(self.buy_orders))
        if not self.buy_orders:
            while buy_temp:
                heapq.heappush(self.buy_orders,buy_temp.pop())
            return
        best_buy_order = self.buy_orders[0]
        # Auto match    
        # You can do full trade
        if order.quantity < best_buy_order.quantity:
            best_buy_order.quantity -= order.quantity
            self.trades.append(Trade(best_buy_order.price,order.quantity,best_buy_order.owner_id,order.owner_id,best_buy_order.order_id,order.order_id))
        # Partial fill.
        else:
            self.trades.append(Trade(best_buy_order.price,best_buy_order.quantity,best_buy_order.owner_id,order.owner_id,best_buy_order.order_id,order.order_id))
            order.quantity -= best_buy_order.quantity
            heapq.heappop(self.buy_orders)
            self.match_market_sell_order(order)

        while buy_temp:
            heapq.heappush(self.buy_orders,buy_temp.pop())

    def compute_mid_price(self):

        best_bid = None if not self.buy_orders else self.buy_orders[0].price
        best_ask = None if not self.sell_orders else self.sell_orders[0].price
        if best_bid and best_ask:
            mid_price = (best_bid+best_ask)//2
        elif best_bid:
            mid_price = best_bid
        elif best_ask:
            mid_price = best_ask
        else:
            mid_price = 100 # Reference or last_trade_price

        return mid_price
 
    def print_order_book(self):
        print(" BASIC STATISTICS:\n")
        # Total_orders, total_trades, total_volume, best_bid, best_ask and spread.
        print(f" Total_orders = {self.next_order_id-1} \n Total_trades = {Trade.next_trade_id-1} \n Total_volume = {Trade.total_volume}  ")
        Best_Bid = None if not self.buy_orders else self.buy_orders[0].price
        Best_Ask = None if not self.sell_orders else self.sell_orders[0].price
        Spread = (Best_Ask - Best_Bid) if Best_Ask and Best_Bid else None
        print(f" Best_Bid = {Best_Bid}\n Best_Ask = {Best_Ask}\n Spread = {Spread}")
        print("\n  BUY ORDERS: \n ")
        if not self.buy_orders:
            print("  Empty")
        else:
            print("Order_ID : Bid : Quantity : Owner_ID : Status")
            for order in self.buy_orders:
                print(f"   {order.order_id} \t:  {order.price}\t:   {order.quantity}  :\t{order.owner_id}  :\t{"Active" if order.active else "Inactive"}")
        print("\n------------------------------")
        print("\n  SELL ORDERS: \n")
        if not self.sell_orders:
            print("  Empty")
        else:
            print("Order_ID : Ask : Quantity : Owner_ID  : Status")
            for order in self.sell_orders:
                print(f"   {order.order_id} \t:  {order.price}\t:   {order.quantity}  :\t{order.owner_id}  :\t{"Active" if order.active else "Inactive"}")

    def print_trades(self):
        if not self.trades:
            print("\nNo trades done yet")
            return
        print("\nTrades:\n")
        print("Trade_ID Prices Quantity Buyer_ID Seller_ID Buy_Order_ID Sell_Order_ID")
        for trade in self.trades:
            print(f"   {trade.trade_id}\t   {trade.price}\t   {trade.quantity}\t   {trade.buyer_id}\t    {trade.seller_id}\t     {trade.buy_order_id}\t\t{trade.sell_order_id}")
            
