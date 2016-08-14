import random

### Create "Portfolio" class that will manage transactions.
### Initialization requires no user input, and creates attributes
### with which to track available cash, a dictionary of stocks and
### mutual funds held, and a list of actions taken.

class Portfolio(object):
    def __init__(self):
		self.cash = 0
		self.stocks = {}
		self.mut_funds = {}
		self.trans_history = []
	
	### Functions to add and withdraw cash
	
    def addCash(self, new_cash):
		self.cash += new_cash
		self.trans_history.append("Added $%.2f to the portfolio." %new_cash)

    def withdrawCash(self, new_cash):
		if self.cash > new_cash:
			self.cash -= new_cash
			self.trans_history.append("Withdrew $%.2f from the portfolio." %new_cash)
		else:
			raise NotImplementedError("Not enough cash in portfolio to execute withdrawal")
	
	### Functions with which to buy and sell stocks and mutual funds.
	### Will draw on functions within the classes for stocks and
	### mutual funds.
	
    def buyStock(self, num_shares, stock):
		return stock.buy(self, num_shares)
		
    def buyMutualFund(self, num_shares, mf):
		return mf.buy(self, num_shares)
		
    def sellStock(self, num_shares, stock):
		return stock.sell(self, num_shares)
		
    def sellMutualFund(self, num_shares, mf):
		return mf.sell(self, num_shares)
	
	### Specifies what will be displayed when an object of class Portfolio
	### is printed.
	
    def __str__(self):
        output = ''
        output += 'Cash:\t$%.2f' % self.cash
        for stocks_in in self.stocks.keys():
            output += '\nStock %s:\t%s \n' % (stocks_in, str(self.stocks[stocks_in]))
        for mf_in in self.mut_funds.keys():
            output += '\nMutual Fund %s:\t%s \n' % (mf_in, str(self.mut_funds[mf_in]))
        return output
	
	### Function which will print the history of all actions taken within a portfolio.
	
    def history(self):
		indexeditems = []
		for index in self.trans_history:
			indexeditems.append(str((index)))
		print '\n'.join(indexeditems)

### Creates a class Asset which will enable more specific the creation
### of subclasses which will pertain to particular types of assets.		
		
class Asset(object):
	def __init__(self, price, symbol):
		self.symbol = symbol
		self.price = price
		
	def buy(self):
		raise NotImplementedError("Subclass must implement abstract method")
		
	def sell(self):
		raise NotImplementedError("Subclass must implement abstract method")

### Creates a subclass of Asset, Stock, which inherits the basic attributes
### of Asset, and specifies how buying and selling is executed for objects
### of the subclass.
		
class Stock(Asset):
    def sell(self, portfolio, num_shares):
		if isinstance(num_shares, int):
			if portfolio.stocks[self.symbol]>=num_shares:
				sell_price = random.uniform(0.5,1.5)*self.price
				portfolio.cash += sell_price*num_shares
				portfolio.trans_history.append("Sold %d shares of %s for $%.2f." %(num_shares, self.symbol, sell_price*num_shares))
				if self.symbol in portfolio.stocks.keys():
					portfolio.stocks[self.symbol]-= num_shares
					if portfolio.stocks[self.symbol]==0:
						portfolio.stocks.pop(self.symbol, None)
			else: raise NotImplementedError("Insufficient shares of %s to sell" %self.symbol)
		else: raise NotImplementedError("Stock shares may only be transacted in whole values")
	
    def buy(self, portfolio, num_shares):
		if isinstance(num_shares, int):
			if portfolio.cash >= self.price*num_shares:
				portfolio.cash -= self.price*num_shares
				portfolio.trans_history.append("Purchased %d shares of %s for $%.2f ($%.2f per share)." %(num_shares, self.symbol, self.price*num_shares, self.price))
				if self.symbol in portfolio.stocks.keys():
					portfolio.stocks[self.symbol]+= num_shares
				else:
					portfolio.stocks[self.symbol] = num_shares
			else: raise NotImplementedError("Insufficient funds to complete purchase")
		else: raise NotImplementedError("Stock shares may only be transacted in whole values")

### Creates a subclass of Asset, MutualFund, which inherits the basic attributes
### of Asset, and specifies how buying and selling is executed for objects
### of the subclass.
		
class MutualFund(Asset):
    def __init__(self, symbol):
        Asset.__init__(self,1,symbol)
	
    def buy(self, portfolio, num_shares):
		if portfolio.cash >= self.price*num_shares:
				portfolio.cash -= self.price*num_shares
				portfolio.trans_history.append("Purchased %d shares of %s for $%.2f ($%.2f per share)." %(num_shares, self.symbol, num_shares, 1))
				if self.symbol in portfolio.mut_funds.keys():
					portfolio.mut_funds[self.symbol]+= num_shares
				else:
					portfolio.mut_funds[self.symbol] = num_shares
		else: raise NotImplementedError("Insufficient funds to complete purchase")
	
    def sell(self, portfolio, num_shares):
		if portfolio.mut_funds[self.symbol]>=num_shares:
				sell_price = random.uniform(0.9,1.2)
				portfolio.cash += sell_price*num_shares
				portfolio.trans_history.append("Sold %d shares of %s for $%.2f." %(num_shares, self.symbol, sell_price*num_shares))
				if self.symbol in portfolio.mut_funds.keys():
					portfolio.mut_funds[self.symbol]-= num_shares
					if portfolio.mut_funds[self.symbol]==0:
						portfolio.mut_funds.pop(self.symbol, None)
		else: raise NotImplementedError("Insufficient shares of %s to sell" %self.symbol)

### If we wanted to enable the script to account for bonds, we could create a new
### subclass of Assets, perhaps more similar to Stocks than Mutual Funds, where we
### would likely add an input to account for the bond yield.  Then, we would tweak
### the buy and sell functions for bonds to accordingly, given conditions we impose
### on bonds.
		
### Testing the script

portfolio = Portfolio()
portfolio.addCash(5000)
s = Stock(20, "APPL")
t = Stock(10, "MSFT")
mf1 = MutualFund("MF1")
mf2 = MutualFund("MF2")

portfolio.buyStock(5, s)
portfolio.buyStock(5, t)
portfolio.buyMutualFund(10.7, mf1)
portfolio.buyMutualFund(2, mf2)

print(portfolio)

portfolio.sellStock(3, s)
portfolio.sellMutualFund(1.2, mf1)

portfolio.withdrawCash(500)

print(portfolio)

portfolio.history()

### The following generate NotImplementedErrors built into the script:
### portfolio.withdrawCash(50000000000000000)
### portfolio.buyStock(1.3, s)
### portfolio.buyStock(999999, s)
### portfolio.sellStock(7778, s)
### portfolio.sellStock(1.2, t)
### portfolio.buyMutualFund(193944,mf1)
### portfolio.sellMutualFund(193944,mf2)