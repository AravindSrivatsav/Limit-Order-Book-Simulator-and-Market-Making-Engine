from order import *
#from trade import Trade
from order_book import Order_Book
from traders import *
from market_maker import Market_Maker

book = Order_Book()
All_traders =  [ Noise_Trader(), Aggressive_Buyer(), Aggressive_Seller(), Large_Trader(), Noise_Trader(), Aggressive_Buyer(), Aggressive_Seller(), Large_Trader() ]
maker = Market_Maker()

order1 = Limit_Order("BUY",100,4,owner_id = 1)
book.add_order(order1)
mm_orders = maker.generate_limit_orders(book)
order2 = Limit_Order("BUY",102,1,owner_id = 2)
book.add_order(order2)
for order in mm_orders:
    book.add_order(order)
order3 = Market_Order("SELL",5,owner_id = 3)
book.add_order(order3)
'''
for i in range(10): # Ten simulation steps
    for trader in All_traders:
        new_order = trader.generate_limit_order()
        book.add_order(new_order)

    maker.cancel_prev_orders()

    mm_orders = maker.generate_limit_orders(book)
    for new_order in mm_orders:
        book.add_order(new_order)

    for trader in All_traders:
        new_order = trader.generate_market_order()
        book.add_order(new_order)

    mm_orders = maker.generate_market_orders()
    for new_order in mm_orders:
        book.add_order(new_order)
'''
book.print_order_book()
book.print_trades()
maker.process_trades(book)
maker.compute_PnL(book)
maker.print_stats()
