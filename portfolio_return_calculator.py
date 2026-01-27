import yfinance as yf
from datetime import datetime,timedelta
from decimal import Decimal
def get_prices(symbol):
    try:
     prices=[]
     end=datetime.today()
     start=end-timedelta(days=10)
     data=yf.download(symbol,start=start,end=end,progress=False)
     column='Close'if 'Close'in data.columns else 'Adj Close'
     if column in data.columns:
        prices=data[column].dropna()
       
        if len(prices)>=2:
         return prices.values.flatten().tolist()
     else:
        return []
    except Exception as e:
        print(f' THERE IS SOMETHING ERROR {e}!')
        return []
    
    




def cal_total_returns(prices):
   total_returns={}
   for key in prices.keys():
      if len(prices[key])<2:
         print('cannot calculate the price for this stock as there is insufficientdata')
         total_returns[key]=Decimal('0')
         continue
         
      else:
         first=Decimal(str(prices[key][0]))
         last=Decimal(str(prices[key][-1]))
         total_return=(last-first)/first
         total_returns[key]=total_return
   return total_returns   


def cal_portfolio_ret(total_returns,weights):
   if len(total_returns)!=len(weights):
        print('there is something wrong pls check !')
        return Decimal('0')
   if abs(sum(weights)-1)>0.001:
        print('warning! weights do not sum 1 so results may be incorrect')
        
    
   portfolio_return=Decimal('0')
   for stocks,weight in zip(total_returns.values(),weights):
          portfolio_return+=stocks*Decimal(str(weight))
   return  portfolio_return


def cal_daily_returns(prices):
   daily_returns={}
   for keys in prices.keys():
      if len(prices[keys])<2:
         daily_returns[keys]=[]
         continue
      else:
         returns=[]
         for i in range(1,len(prices[keys])):
            pre=Decimal(str(prices[keys][i-1]))
            curr=Decimal(str(prices[keys][i]))
            daily_return=(curr-pre)/pre
            returns.append(daily_return)
         daily_returns[keys]=returns
   return daily_returns 
        

def best_worst_stock(total_returns):
    if not total_returns:
        print('there are no stocks provided')
        return 'N/A'
    else:
     return f' best return {max(total_returns.values())*100:0.2f}%\n worst return {min(total_returns.values())*100:0.2f}%'

   

def risk_indicator(daily_returns):
   risk_dict={}
   for key in daily_returns.keys():
      if any(daily_returns[key])<Decimal(str('-0.3')):
         risk_dict[key]='HIGH VOLATILITY'
      risk_dict[key]='LOW VOLATILITY' 
   return risk_dict
 

def investment_analysis(total_returns,weights):
    investment_return=cal_portfolio_ret(total_returns,weights)
    if investment_return<Decimal(str('0.15')):
        return f' HOLD: NO FURTHER CAPITAL ADDITION' 
    return f'INVEST MORE: PORTFOLIO IS PERFORMING WELL'
  
# Fetch
reliance = get_prices('RELIANCE.NS')
hdfc = get_prices('HDFCBANK.NS')
tcs = get_prices('TCS.NS')

prices = {'RELIANCE': reliance, 'HDFC': hdfc, 'TCS': tcs}

# Total returns (once)
total_returns = cal_total_returns(prices)

# Portfolio
portfolio_return = cal_portfolio_ret(total_returns, [0.4, 0.3, 0.3])

# Daily returns
daily_returns = cal_daily_returns(prices)

# Print everything nicely

print(f"Portfolio Return: {float(portfolio_return * 100):.3f}%")
print(investment_analysis(total_returns, [0.4, 0.3, 0.3]))
print(best_worst_stock(total_returns))
print(risk_indicator(daily_returns))  # fix this function first

print('start date: 11/1/2026   end date: 21/01/2026')
