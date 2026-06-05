# Limit Order Book Simulator and Market Making Engine

A Python-based electronic exchange simulator that models a financial market using a **Limit Order Book (LOB)**. The project implements core exchange infrastructure including order matching, market orders, order cancellations, trade execution, and a market-making agent.

The goal of this project is to build a realistic environment for studying **Market Microstructure**, **Market Making**, **Inventory Risk**, **Adverse Selection**, and **Order Flow**.

---

## Features

### Order Management
- Limit Orders
- Market Orders
- Order Cancellation
- Price-Time Priority Matching

### Matching Engine
- Automatic trade execution when buy and sell orders cross
- Partial order fills
- Full order fills
- Trade history recording

### Object-Oriented Design
- Abstract `Order` base class
- `LimitOrder` subclass
- `MarketOrder` subclass
- Trader abstraction
- Market Maker agent

### Order Book
- Best Bid tracking
- Best Ask tracking
- Spread calculation
- Live order book maintenance

### Market Maker
- Continuous bid and ask quote placement
- Inventory tracking
- Cash tracking
- PnL tracking
- Quote cancellation and replacement

### Statistics
- Total orders processed
- Total trades executed
- Total traded volume
- Current Best Bid and Best Ask
- Market Maker inventory and PnL

---

## Matching Logic

### Buy Orders
A buy order matches against the lowest available asks.

### Sell Orders
A sell order matches against the highest available bids.

### Priority Rules

The simulator follows **Price-Time Priority**:

1. Better price first
2. Earlier arrival time first

This is the matching rule used by most modern electronic exchanges.

---

## Example Order Book

### Buy Side

| Price | Quantity |
|---------|---------|
| 100 | 10 |
| 99 | 15 |
| 98 | 20 |

### Sell Side

| Price | Quantity |
|---------|---------|
| 101 | 12 |
| 102 | 8 |
| 103 | 25 |

**Best Bid:** 100

**Best Ask:** 101

**Spread:** 1

---

## Market Maker

The market maker continuously places bid and ask quotes around the market.

### Objectives

- Earn the bid-ask spread
- Provide liquidity
- Manage inventory risk

The simulator tracks:

- Cash
- Inventory
- Realized PnL

throughout the simulation.

---

## Concepts Being Studied

### Market Microstructure
- Bid-Ask Spread
- Liquidity
- Price Impact
- Queue Position

### Inventory Risk
Risk arising from accumulating large long or short positions.

### Adverse Selection
Losses incurred when trading against informed participants.

### Order Flow
- Buy pressure
- Sell pressure
- Order flow imbalance

### Market Making
- Quoting strategies
- Inventory management
- Spread capture

---

## Sample Output

```text
Total Orders = 100
Total Trades = 71
Total Volume = 546

Best Bid = 94
Best Ask = 95
Spread = 1

Cash = 401
Inventory = -4
PnL = 25
```

---

## Future Improvements

- Inventory-aware market making
- Adaptive spread setting
- Order flow imbalance signals
- Adverse selection modeling
- Multi-asset support
- Latency simulation
- Transaction costs and exchange fees
- Risk management constraints
- Backtesting framework

---

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Abstract Base Classes (ABC)
- Priority Queues / Heaps
- Financial Market Simulation

---

## Project Structure

```text
project/
│
├── order.py
├── trader.py
├── market_maker.py
├── order_book.py
├── trade.py
├── main.py
└── README.md
```

---

## Author

**Sai Aravind Srivatsav**  
B.Tech, IIT Madras

**Project Status:** Ongoing

Current focus:
- Market Microstructure
- Inventory Risk
- Adverse Selection
- Order Flow
- Market Making
