from blockchain import exchangerates

ticker = exchangerates.get_ticker()

print("Bitcoin Prices : ")
for i in ticker:

	print(i, ticker[i].p15min)


btc = exchangerates.to_btc('SGD', 100000)
print("\n100000 SGD in Bitcoin : %s" %(btc))