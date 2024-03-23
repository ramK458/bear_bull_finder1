import sys,os
os.chdir('..')
sys.path.append('/Users/rkarumugam/LocalFiles/Projects/trading/workspace/code/custom_stockfilter')
sys.path.append('/Users/rkarumugam/LocalFiles/Projects/trading/workspace/code')
print ("\n\n")
print(sys.path)
print ("\n\n")
import downloader.symRetriever_US_xbrlbased as downloader
import talib
import matplotlib.pyplot as plt

downloadObj = downloader.symbol_US_v1(0)

sym = ["cvx","ms","schw","gs","jpm"]
#
#sym = ["0700.HK","bidu","baba"]

for eachsym in sym:
    downloadObj.setSymbol(eachsym,r"%d-%M-%Y")
    #data_1d=downloadObj.data.history(period = "1y", interval="1d")
    data_1d=downloadObj.data.history(start = "2020-09-01",end="2023-12-31", interval="1d")
    data_30d=downloadObj.data.history(period="1mo")
    data_3m = downloadObj.data.history(period="3mo")
    data_6m=downloadObj.data.history(period="6mo")
    open = data_1d['Open'].values
    close = data_1d['Close'].values
    high = data_1d['High'].values
    low = data_1d['Low'].values
    ind = data_1d.index
    #ind=range(0,len(low))
    
    df = talib.CDLGRAVESTONEDOJI(open, high, low, close)
    
    #df = talib.ADX(high, low, close, timeperiod=14)
    fig,ax =plt.subplots(2,1)
    ax[0].plot(ind,close,'k')
    ax2=ax[0].twinx()
    ax2.plot(ind,data_1d['Volume'].values)
    
    ax1=ax[1].twinx()
    ax1.plot(ind,df)
    df = talib.CDLHAMMER(open, high, low, close)
    ax1.plot(ind,df)
    df = talib.CDLHARAMI(open, high, low, close)
    ax1.plot(ind,df)
    ax[0].set_title(f"Symbol = {eachsym}")
    ax1.legend(["Gravestone","Hammer","Harami"])
   # print(df,data_30d['Close'].values)
    plt.show()

