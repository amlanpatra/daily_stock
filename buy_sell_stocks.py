import math

def stocks_needed(initial_price, final_price, initial_stocks):
	change = ((abs(final_price - initial_price))/initial_price) *100
	final_change = initial_price * initial_stocks * change
	x = final_change/initial_price
	return x

print("No of stocks needed : {}".format(str(stocks_needed(399,400,13000))))
