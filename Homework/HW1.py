class Portfolio(object):
    def __init__(self):
		self.cash = 0
		self.stocks = {}
		self.mut_funds = {}
	
    def addCash(self, new_cash):
		self.cash += new_cash

    def withdrawCash(self, new_cash):
		if self.cash > new_cash:
			self.cash -= new_cash
		else:
			raise NotImplementedError("Not enough cash in portfolio to execute withdrawal")
		
    def buyStock(self, num_shares, stock):
		if isinstance(num_shares, int):
			self.cash -= stock.price*num_shares
			if stock.symbol in self.stocks.keys:
				self.stocks[stock.symbol]+= num_shares
			else:
				self.stocks[stock.symbol].append(num_shares)
		else: raise NotImplementedError("Stock shares may only be transacted in whole values")
		
    def buyMutualFund(self, num_shares, mf):
		self.cash -= stock.price*num_shares
		if stock.symbol in self.stocks.keys:
			self.stocks[stock.symbol]+= num_shares
		else:
			self.stocks[stock.symbol].append(num_shares)
		
    def sellStock(self, num_shares, stock):
		if isinstance(num_shares, int): 
			self.cash += random.uniform(0.5,1.5,1)*num_shares
			if stock.symbol in self.stocks.keys:
				self.stocks[stock.symbol]+= num_shares
			else:
				raise NotImplementedError("No shares of %s available to sell" %stock)
		else: raise NotImplementedError("Stock shares may only be transacted in whole values")
		
    def sellMutualFund(self, num_shares, mf):
		self.cash += (0.9,1.2,1)*num_shares
		if stock.symbol in self.stocks.keys:
			self.stocks[stock.symbol]+= num_shares
		else:
			raise NotImplementedError("No shares of %s available to sell" %mf)
		
class Stock(object):
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
		
class MutualFund(object):
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price