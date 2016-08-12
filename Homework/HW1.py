import random

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
			if self.cash >= stock.price*num_shares:
			    self.cash -= stock.price*num_shares
			    if stock.symbol in self.stocks.keys():
				    self.stocks[stock.symbol]+= num_shares
			    else:
			        self.stocks[stock.symbol] = num_shares
			else: raise NotImplementedError("Insufficient funds to complete purchase")
		else: raise NotImplementedError("Stock shares may only be transacted in whole values")
		
    def buyMutualFund(self, num_shares, mf):
		if self.cash >= mf.price*num_shares:
			    self.cash -= mf.price*num_shares
			    if mf.symbol in self.mut_funds.keys():
				    self.mut_funds[mf.symbol]+= num_shares
			    else:
			        self.mut_funds[mf.symbol] = num_shares
		else: raise NotImplementedError("Insufficient funds to complete purchase")
		
    def sellStock(self, num_shares, stock):
		if isinstance(num_shares, int):
			if self.stocks[stock.symbol]>=num_shares:
				self.cash += random.uniform(0.5,1.5)*num_shares*stock.price
				if stock.symbol in self.stocks.keys():
					self.stocks[stock.symbol]-= num_shares
					if self.stocks[stock.symbol]==0:
						self.stocks.pop(stock.symbol, None)
				else:
					raise NotImplementedError("No shares of %s available to sell" %stock)
			else: raise NotImplementedError("Insufficient shares of %s to sell" %stock)
		else: raise NotImplementedError("Stock shares may only be transacted in whole values")
		
    def sellMutualFund(self, num_shares, mf):
		self.cash += random.uniform(0.5,1.5)*num_shares
		if mf.symbol in self.mut_funds.keys():
			self.mut_funds[mf.symbol]-= num_shares
			if self.mut_funds[mf.symbol]==0:
					self.mut_funds.pop(mf.symbol, None)
		else:
			raise NotImplementedError("No shares of %s available to sell" %mf)
	
    def __str__(self):
        output = ''
        output += 'Cash: $%d' % self.cash
        for stocks_in in self.stocks.keys():
            output += '\nStock(s) %s: %s \n' % (stocks_in, str(self.stocks[stocks_in]))
        for mf_in in self.mut_funds.keys():
            output += 'Mutual Fund(s) %s: %s \n' % (mf_in, str(self.mut_funds[mf_in]))
        return output
	
class Stock(object):
    def __init__(self, price,symbol):
        self.symbol = symbol
        self.price = price
		
class MutualFund(object):
    def __init__(self, symbol):
        self.symbol = symbol
        self.price = 1