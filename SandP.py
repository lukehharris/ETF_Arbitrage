from itertools import imap
import math
import time

## Data: idx 0 is 7/26/13; idx 142 is 1/2/13 ##
SP500 = [1691.65,1690.25,1685.94,1692.39,1695.53,1692.09,1689.37,1680.91,1676.26,1682.5,1680.19,1675.02,1652.62,1652.32,1640.46,1631.89,1615.41,1614.08,1614.96,1606.28,1613.2,1603.26,1588.03,1573.09,1592.43,1588.19,1628.93,1651.81,1639.04,1626.73,1636.6,1612.52,1626.13,1642.81,1643.38,1622.56,1608.9,1631.38,1640.42,1630.74,1654.41,1648.36,1660.06,1649.6,1650.51,1655.35,1669.16,1666.29,1667.47,1650.47,1658.78,1650.34,1633.77,1633.7,1626.67,1632.69,1625.96,1617.5,1614.42,1597.59,1582.7,1597.57,1593.61,1582.24,1585.16,1578.79,1578.78,1562.5,1555.25,1541.61,1552.01,1574.57,1552.36,1588.85,1593.37,1587.73,1568.61,1563.07,1553.8,1559.98,1553.69,1570.25,1562.17,1569.19,1562.85,1563.77,1551.69,1556.89,1545.8,1558.71,1548.34,1552.1,1560.7,1563.23,1554.52,1552.48,1556.22,1551.18,1544.26,1541.46,1539.79,1525.2,1518.2,1514.68,1515.99,1496.94,1487.85,1515.6,1502.42,1511.95,1530.94,1519.79,1521.38,1520.33,1519.43,1517.01,1517.93,1509.39,1512.12,1511.29,1495.71,1513.17,1498.11,1501.96,1507.84,1500.18,1502.96,1494.82,1494.81,1492.56,1485.98,1480.94,1472.63,1472.34,1470.68,1472.05,1472.12,1461.02,1457.15,1461.89,1466.47,1459.37,1462.42]

#single long
SPY = [169.11,168.93,168.52,169.14,169.5,169.17,168.87,167.95,167.52,168.15,167.51,167.44,165.19,165.13,163.95,163.02,161.28,161.21,161.36,160.42,161.08,160.14,158.57,157.06,159.07,159.4,163.45,165.74,164.44,163.18,164.21,161.75,163.1,164.8,164.8,162.73,161.27,163.56,164.35,163.45,165.83,165.22,166.3,165.31,165.45,165.93,167.17,166.93,166.94,165.34,166.12,165.23,163.54,163.41,162.88,163.34,162.6,161.78,161.37,159.75,158.28,159.68,159.3,158.24,158.52,157.88,157.78,156.17,155.48,154.14,155.11,157.41,155.12,158.8,159.19,158.67,156.75,156.21,155.16,155.86,155.23,156.82,156.05,156.67,156.19,156.19,154.95,155.6,154.36,155.69,154.61,154.97,155.83,156.73,155.9,155.68,156.03,155.44,154.78,154.5,154.29,152.92,152.11,151.61,151.91,150.02,149,151.9,150.42,151.34,153.25,152.11,152.29,152.15,152.02,151.77,151.8,150.96,151.16,151.05,149.54,151.24,149.7,150.07,150.66,150.07,150.25,149.41,149.37,149.13,148.33,148,147.05,147.07,146.97,147.07,147.08,145.92,145.55,145.97,146.37,145.73,146.06]

#double long
SSO = [85.18,85,84.67,85.31,85.67,85.37,85.01,84.11,83.66,84.37,83.58,83.6,81.37,81.33,80.15,79.28,77.58,77.4,77.59,76.73,77.4,76.51,75.14,73.72,75.59,75.18,79.09,81.27,80.07,78.86,79.87,77.57,78.84,80.42,80.42,78.47,77.11,79.4,80.09,79.25,81.6,81.04,82,81.1,81.32,81.61,83.03,82.74,82.79,81.2,81.97,81.12,79.45,79.35,78.86,79.25,78.53,77.78,77.25,75.77,74.43,75.8,75.38,74.44,74.72,74.2,74.01,72.53,71.76,70.6,71.51,73.67,71.63,75.08,75.47,75,73.15,72.69,71.7,72.36,71.77,73.27,72.53,72.98,72.64,72.71,71.62,72.11,71.04,72.2,71.31,71.67,72.43,72.62,71.85,71.69,72.02,71.52,70.93,70.63,70.4,69.14,68.43,67.99,68.27,66.6,65.77,68.28,67.01,67.79,69.54,68.58,68.74,68.59,68.46,68.24,68.25,67.57,67.71,67.63,66.29,67.75,66.55,66.79,67.3,66.82,66.95,66.17,66.12,65.93,65.25,64.93,64.12,64.14,64.03,64.18,64.13,63.2,62.85,63.23,63.53,62.98,63.29]

#single short
SH = [28.04,28.08,28.12,28.03,27.97,28.01,28.07,28.24,28.31,28.19,28.32,28.31,28.72,28.73,28.94,29.1,29.41,29.45,29.4,29.69,29.46,29.64,29.92,30.22,29.85,29.95,29.21,28.83,29.04,29.28,29.1,29.54,29.3,29,29,29.4,29.65,29.24,29.1,29.27,28.83,28.96,28.76,28.94,28.93,28.83,28.63,28.65,28.67,28.93,28.82,28.96,29.27,29.29,29.4,29.3,29.45,29.59,29.7,29.99,30.26,29.98,30.07,30.27,30.23,30.35,30.36,30.69,30.84,31.08,30.92,30.44,30.88,30.22,30.11,30.24,30.62,30.72,30.92,30.79,30.93,30.62,30.78,30.69,30.74,30.74,30.98,30.87,31.11,30.85,31.07,31,30.82,30.78,30.95,31.01,30.94,31.05,31.17,31.23,31.28,31.59,31.74,31.89,31.79,32.2,32.4,31.8,32.13,31.94,31.54,31.77,31.73,31.78,31.81,31.86,31.86,32.03,31.99,32,32.32,31.95,32.31,32.23,32.09,32.25,32.21,32.39,32.4,32.46,32.61,32.71,32.92,32.91,32.93,32.89,32.92,33.16,33.24,33.15,33.05,33.2,33.18]

#double short
SDS = [36.7,36.76,36.89,36.63,36.51,36.65,36.77,37.18,37.38,37.09,37.29,37.42,38.46,38.51,39.07,39.51,40.39,40.44,40.35,40.85,40.48,40.99,41.79,42.61,41.62,41.84,39.84,38.8,39.41,40.04,39.54,40.78,40.11,39.33,39.34,40.34,41.1,39.97,39.58,40.04,38.88,39.17,38.72,39.15,39.08,38.94,38.29,38.42,38.43,39.17,38.81,39.21,40.09,40.11,40.4,40.16,40.52,40.95,41.17,42.04,42.83,42.12,42.34,42.87,42.72,43.1,43.13,44.04,44.42,45.2,44.73,43.38,44.66,42.72,42.51,42.81,43.91,44.2,44.79,44.42,44.78,43.88,44.3,43.94,44.27,44.24,44.87,44.6,45.31,44.56,45.17,44.98,44.49,44.37,44.88,44.98,44.78,45.1,45.48,45.68,45.79,46.67,47.11,47.45,47.26,48.49,49.12,47.4,48.28,47.75,46.61,47.27,47.13,47.27,47.33,47.51,47.49,47.99,47.87,47.98,48.88,47.87,48.86,48.64,48.24,48.68,48.56,49.08,49.14,49.27,49.78,50.08,50.73,50.67,50.75,50.71,50.7,51.44,51.76,51.46,51.17,51.66,51.4]


dates = ['7/26/2013','7/25/2013','7/24/2013','7/23/2013','7/22/2013','7/19/2013','7/18/2013','7/17/2013','7/16/2013','7/15/2013','7/12/2013','7/11/2013','7/10/2013','7/9/2013','7/8/2013','7/5/2013','7/3/2013','7/2/2013','7/1/2013','6/28/2013','6/27/2013','6/26/2013','6/25/2013','6/24/2013','6/21/2013','6/20/2013','6/19/2013','6/18/2013','6/17/2013','6/14/2013','6/13/2013','6/12/2013','6/11/2013','6/10/2013','6/7/2013','6/6/2013','6/5/2013','6/4/2013','6/3/2013','5/31/2013','5/30/2013','5/29/2013','5/28/2013','5/24/2013','5/23/2013','5/22/2013','5/21/2013','5/20/2013','5/17/2013','5/16/2013','5/15/2013','5/14/2013','5/13/2013','5/10/2013','5/9/2013','5/8/2013','5/7/2013','5/6/2013','5/3/2013','5/2/2013','5/1/2013','4/30/2013','4/29/2013','4/26/2013','4/25/2013','4/24/2013','4/23/2013','4/22/2013','4/19/2013','4/18/2013','4/17/2013','4/16/2013','4/15/2013','4/12/2013','4/11/2013','4/10/2013','4/9/2013','4/8/2013','4/5/2013','4/4/2013','4/3/2013','4/2/2013','4/1/2013','3/28/2013','3/27/2013','3/26/2013','3/25/2013','3/22/2013','3/21/2013','3/20/2013','3/19/2013','3/18/2013','3/15/2013','3/14/2013','3/13/2013','3/12/2013','3/11/2013','3/8/2013','3/7/2013','3/6/2013','3/5/2013','3/4/2013','3/1/2013','2/28/2013','2/27/2013','2/26/2013','2/25/2013','2/22/2013','2/21/2013','2/20/2013','2/19/2013','2/15/2013','2/14/2013','2/13/2013','2/12/2013','2/11/2013','2/8/2013','2/7/2013','2/6/2013','2/5/2013','2/4/2013','2/1/2013','1/31/2013','1/30/2013','1/29/2013','1/28/2013','1/25/2013','1/24/2013','1/23/2013','1/22/2013','1/18/2013','1/17/2013','1/16/2013','1/15/2013','1/14/2013','1/11/2013','1/10/2013','1/9/2013','1/8/2013','1/7/2013','1/4/2013','1/3/2013','1/2/2013']


def pearsonr(x, y):
  # Assume len(x) == len(y)
  n = len(x)
  sum_x = float(sum(x))
  sum_y = float(sum(y))
  sum_x_sq = sum(map(lambda x: pow(x, 2), x))
  sum_y_sq = sum(map(lambda x: pow(x, 2), y))
  psum = sum(imap(lambda x, y: x * y, x, y))
  num = psum - (sum_x * sum_y/n)
  den = pow((sum_x_sq - pow(sum_x, 2) / n) * (sum_y_sq - pow(sum_y, 2) / n), 0.5)
  if den == 0: return 0
  return num / den


print 'Correlations: '
correl = pearsonr(SP500,SPY)
print 'SP500 - SPY: ',correl
correl = pearsonr(SP500,SSO)
print 'SP500 - SSO: ',correl
correl = pearsonr(SP500,SH)
print 'SP500 - SH: ',correl
correl = pearsonr(SP500,SDS)
print 'SP500 - SDS: ',correl

print ''
correl = pearsonr(SPY,SSO)
print 'SPY - SSO: ',correl
correl = pearsonr(SPY,SH)
print 'SPY - SH: ',correl
correl = pearsonr(SPY,SDS)
print 'SPY - SDS: ',correl

print ''
correl = pearsonr(SSO,SH)
print 'SSO - SH: ',correl
correl = pearsonr(SSO,SDS)
print 'SSO - SDS: ',correl

print ''
correl = pearsonr(SH,SDS)
print 'SH - SDS: ',correl


print '\nSH vs SDS:'

#the data was entered in reverse-chrono order; fix that here for clarity/simplicity
SH.reverse()
SDS.reverse()
dates.reverse()

#store the dates according to day of the year (makes it easy to calculate holding period)
dates_doy = [] # doy = day of year
for date in dates:
	date_obj = time.strptime(date,'%m/%d/20%y')
	dates_doy.append(date_obj.tm_yday)


#calculate the daily percentage price changes
SH_pct_change = []
for x in range(1,len(SH)):
	change = (SH[x]/SH[x-1]) - 1
	SH_pct_change.append(change)

SDS_pct_change = []
for x in range(1,len(SDS)):
	change = (SDS[x]/SDS[x-1]) - 1
	SDS_pct_change.append(change)

Weighted_difference = []
for x in range(0,len(SH_pct_change)):
	#calculate the relative change in values. 
	#if difference is high, SH rose in value proportionally more (or fell less) than SDS did - ie SH is overvalued, SDS is undervalued; sell SH, buy SDS
	#if difference is low, SH fell more (or rose less) than SDS did - ie SH is undervalued, SDS is overvalued; buy SH, sell SDS
	difference = 2.0 * SH_pct_change[x] - SDS_pct_change[x]
	Weighted_difference.append(difference)


def buy_to_open(SH_share_price, SDS_share_price, doy, day_index):
	#long SH, short SDS
	price_ratio = SH_share_price / SDS_share_price
	trade = {
		'type':'BTO',
		'doy':doy,
		'day_index':day_index,
		'num_SH_shares':2,
		'SH_share_price':SH_share_price,
		'num_SDS_shares':price_ratio,
		'SDS_share_price':SDS_share_price,
	}
	current_position = 'Long'
	return trade, current_position

def buy_to_close(SH_share_price, SDS_share_price, doy, day_index):
	price_ratio = SH_share_price / SDS_share_price
	trade = {
		'type':'BTC',
		'doy':doy,
		'day_index':day_index,
		'SH_share_price':SH_share_price,
		'SDS_share_price':SDS_share_price
	}
	current_position = None
	return trade, current_position

def sell_to_open(SH_share_price, SDS_share_price, doy, day_index):
	#short SH, long SDS
	price_ratio = SH_share_price / SDS_share_price
	trade = {
		'type':'STO',
		'doy':doy,
		'day_index':day_index,
		'num_SH_shares':2,
		'SH_share_price':SH_share_price,
		'num_SDS_shares':price_ratio,
		'SDS_share_price':SDS_share_price
	}
	current_position = 'Short'
	return trade, current_position

def sell_to_close(SH_share_price, SDS_share_price, doy, day_index):
	price_ratio = SH_share_price / SDS_share_price
	trade = {
		'type':'STC',
		'doy':doy,
		'day_index':day_index,
		'SH_share_price':SH_share_price,
		'SDS_share_price':SDS_share_price
	}
	current_position = None
	return trade, current_position


def get_action(threshold, change):
	if change > threshold:
		return 'Sell'
	elif change < -1 * threshold:
		return 'Buy'
	else:
		return None



THRESHOLD = 0.0005
DAILY_FINANCING_COST = 0.05 / 365.0 #5% annual
DAILY_LENDING_ROR = 0.005 / 365.0 #0.5% annual
COMMISSION = 3 * 0.005 #3 shares, half cent per share

#define a unit to be: long/(short) [2 shares of SH] and short/(long) [1 share of SDS times the ratio of the share price of SH to the share price of SDS]
#this scheme gives us twice as much dollar exposure to SH as SDS, which should align our dollar exposure for any change in the S&P. ie, if we buy $50 worth of SH and sell $25 of SDS, and then the S&P falls 1%, our position in SH should rise 1% to $50.50 and our position in SDS should rise 2% to $25.50, which is a $0.50 change in each, which offset each other.

current_position = None
trade_log = []
for idx,change in enumerate(Weighted_difference):
	action = get_action(THRESHOLD, change)
	day_index = idx + 1;
	if action == 'Buy':
		if current_position == None:
			#open a long posiiton
			trade, current_position = buy_to_open(SH[idx+1],SDS[idx+1],dates_doy[idx+1],day_index)
			trade_log.append(trade)
		elif current_position == 'Short':
			#close the short position, open a long position
			trade, current_position = buy_to_close(SH[idx+1],SDS[idx+1],dates_doy[idx+1],day_index)
			trade_log.append(trade)
			trade, current_position = buy_to_open(SH[idx+1],SDS[idx+1],dates_doy[idx+1],day_index)
			trade_log.append(trade)
		elif current_position == 'Long':
			#add-on long
			trade, current_position = buy_to_open(SH[idx+1],SDS[idx+1],dates_doy[idx+1],day_index)
			trade_log.append(trade)
	elif action == 'Sell':
		if current_position == None:
			#open a short position
			trade, current_position = sell_to_open(SH[idx+1],SDS[idx+1],dates_doy[idx+1],day_index)
			trade_log.append(trade)
		elif current_position == 'Short':
			#add-on short
			trade, current_position = sell_to_open(SH[idx+1],SDS[idx+1],dates_doy[idx+1],day_index)
			trade_log.append(trade)
		elif current_position == 'Long':
			#close the long position, open a short position
			trade, current_position = sell_to_close(SH[idx+1],SDS[idx+1],dates_doy[idx+1],day_index)
			trade_log.append(trade)
			trade, current_position = sell_to_open(SH[idx+1],SDS[idx+1],dates_doy[idx+1],day_index)
			trade_log.append(trade)


#number of shares long or short
active_trades = []

PnL = 0
completed_trades = []

for trade in trade_log:
	print 'Action: ', trade['type']
	
	if trade['type'] == 'BTO':
		active_trades.append(trade)

		SH_cost = trade['num_SH_shares']*trade['SH_share_price']
		print '  Buy ',trade['num_SH_shares'],' shares of SH at ',trade['SH_share_price'],' for ',SH_cost

		SDS_proceeds = trade['num_SDS_shares']*trade['SDS_share_price']
		print '  Sell ',round(trade['num_SDS_shares'],2),' shares of SDS at ',trade['SDS_share_price'],' for ',SDS_proceeds

	elif trade['type'] == 'STC':
		#loop through all active trades since we could have had add-ons
		for this_trade in active_trades:
			SH_proceeds = this_trade['num_SH_shares'] * trade['SH_share_price']
			print '  Sell ',this_trade['num_SH_shares'],' shares of SH at ',trade['SH_share_price'],' for ',SH_proceeds

			SDS_cost = this_trade['num_SDS_shares'] * trade['SDS_share_price']
			print '  Buy',round(this_trade['num_SDS_shares'],2),' shares of SDS at ',trade['SDS_share_price'],' for ',round(SDS_cost,2)

			SH_cost_basis = this_trade['SH_share_price']*this_trade['num_SH_shares']
			SDS_total_proceeds = this_trade['SDS_share_price']*this_trade['num_SDS_shares']
			
			holding_period = trade['doy'] - this_trade['doy']
			print '  Trade Holding Period: ',holding_period,'days'

			trade_base_pnl = (SH_proceeds - SH_cost_basis) + (SDS_total_proceeds - SDS_cost)
			print '  Trade Base PnL: ',round(trade_base_pnl,4)

			long_capital = this_trade['num_SH_shares'] * this_trade['SH_share_price']
			short_capital = this_trade['num_SDS_shares'] * this_trade['SDS_share_price']
			net_committed_capital = long_capital - short_capital
			holding_cost = net_committed_capital * DAILY_FINANCING_COST * holding_period
			print '  Trade Holding Cost: ',round(holding_cost,4)
			print '  Commission: ',COMMISSION

			trade_pnl = trade_base_pnl - holding_cost - COMMISSION
			print '  Trade Total PnL: ',round(trade_pnl,4)

			trade_summary = {
				'type':trade['type'],
				'pnl':trade_pnl,
				'start_date': this_trade['doy'],
				'start_date_index': this_trade['day_index'],
				'end_date': trade['doy'],
				'end_date_index': trade['day_index'],
				'num_SH_shares':this_trade['num_SH_shares'],
				'num_SDS_shares':this_trade['num_SDS_shares'],
				'holding_period':holding_period,
				'long_capital': long_capital,
				'short_capital': short_capital,
				'net_committed_capital': net_committed_capital,
				'holding_cost': holding_cost
			}
			completed_trades.append(trade_summary)

			PnL += trade_pnl
		active_trades = []	
		

	if trade['type'] == 'STO':
		active_trades.append(trade)

		SH_proceeds = trade['num_SH_shares']*trade['SH_share_price']
		print '  Sell ',trade['num_SH_shares'],' shares of SH at ',trade['SH_share_price'],' for ',SH_proceeds

		SDS_cost = trade['num_SDS_shares']*trade['SDS_share_price']
		print '  Buy ',round(trade['num_SDS_shares'],2),' shares of SDS at ',trade['SDS_share_price'],' for ',SDS_cost

	elif trade['type'] == 'BTC':
		#loop through all active trades since we could have had add-ons
		for this_trade in active_trades:
			SH_cost = this_trade['num_SH_shares'] * trade['SH_share_price']
			print '  Buy ',this_trade['num_SH_shares'],' shares of SH at ',trade['SH_share_price'],' for ',SH_cost

			SDS_proceeds = this_trade['num_SDS_shares'] * trade['SDS_share_price']
			print '  Sell',round(this_trade['num_SDS_shares'],2),' shares of SDS at ',trade['SDS_share_price'],' for ',round(SDS_proceeds,2)

			SH_total_proceeds = this_trade['SH_share_price']*this_trade['num_SH_shares']
			SDS_cost_basis = this_trade['SDS_share_price']*this_trade['num_SDS_shares']
			
			holding_period = trade['doy'] - this_trade['doy']
			print '  Trade Holding Period: ',holding_period,' days'

			trade_base_pnl = (SH_total_proceeds - SH_cost) + (SDS_proceeds - SDS_cost_basis)
			print '  Trade Base PnL: ',round(trade_base_pnl,4)

			long_capital = this_trade['num_SDS_shares'] * this_trade['SDS_share_price']
			short_capital = this_trade['num_SH_shares'] * this_trade['SH_share_price']
			net_committed_capital = long_capital - short_capital
			holding_cost = net_committed_capital * DAILY_LENDING_ROR * holding_period
			print '  Trade Holding Cost: ',round(holding_cost,4)
			print '  Commission: ',COMMISSION
			
			trade_pnl = trade_base_pnl - holding_cost - COMMISSION
			print '  Trade Total PnL: ',round(trade_pnl,4)

			trade_summary = {
				'type':trade['type'],
				'pnl':trade_pnl,
				'start_date': this_trade['doy'],
				'start_date_index': this_trade['day_index'],
				'end_date': trade['doy'],
				'end_date_index': trade['day_index'],
				'num_SH_shares':this_trade['num_SH_shares'],
				'num_SDS_shares':this_trade['num_SDS_shares'],
				'holding_period':holding_period,
				'long_capital': long_capital,
				'short_capital': short_capital,
				'net_committed_capital': net_committed_capital,
				'holding_cost': holding_cost
			}
			completed_trades.append(trade_summary)

			PnL += trade_pnl
		active_trades = []	

print ''
print 'Total PnL: ',round(PnL,4)
print 'Total Trades Made: ',len(completed_trades)
print 'Avg PnL per Trade: ',round(PnL/len(completed_trades),4)

max_drawdown = 0
total_holding_period = 0
for trade in completed_trades:
	trade_max_drawdown = 0
	total_holding_period += trade['holding_period']
	if trade['type'] == 'BTC':
		#was short SH/long SDS, now closing
		for x in range(trade['start_date_index']+1,trade['end_date_index']+1):
			short_position_value = trade['num_SH_shares'] * SH[x]
			long_position_value = trade['num_SDS_shares'] * SDS[x]
			net_position_value = long_position_value - short_position_value
			if net_position_value < trade['net_committed_capital']:
				#position moved against us
				trade_drawdown = trade['net_committed_capital'] - net_position_value
				if trade_drawdown > trade_max_drawdown:
					trade_max_drawdown = trade_drawdown
	elif trade['type'] == 'STC':
		#was long SH/short SDS, now closing
		for x in range(trade['start_date_index']+1,trade['end_date_index']+1):
			short_position_value = trade['num_SDS_shares'] * SDS[x]
			long_position_value = trade['num_SH_shares'] * SH[x]
			net_position_value = long_position_value - short_position_value
			if net_position_value < trade['net_committed_capital']:
				#position moved against us
				trade_drawdown = trade['net_committed_capital'] - net_position_value
				if trade_drawdown > trade_max_drawdown:
					trade_max_drawdown = trade_drawdown
					
	if trade_max_drawdown > max_drawdown:
		max_drawdown = trade_max_drawdown

print 'Avg Holding Period: ',round(float(total_holding_period)/float(len(completed_trades)),1)
print 'Max Drawdown: ',round(max_drawdown,4)
capital_at_risk = 5.0 * max_drawdown
print 'Capital at Risk (5X Max Drawdown): ',round(capital_at_risk,4)
try:
	print 'Return on Capital at Risk (Annualized): ',int(round((PnL/capital_at_risk)/(7.0/12.0)*100)),'%'
except ZeroDivisionError:
	print 'N/A (no trade realized a drawdown over the test period)'