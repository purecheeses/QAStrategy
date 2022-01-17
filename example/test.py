import QUANTAXIS as QA
from QAStrategy.qastockbase import QAStrategyStockBase
import math

# 上手测试，收盘价大于5日均线就买，低于就买

class strategy(QAStrategyStockBase):
        ## 在你订阅分钟级别的数据的时候, 你需要继承并改写on_bar函数
    def on_bar(self, data):
        code = data.name[1]
        res = self.ma()
        # print(self.get_cash())
        # print(self.init_cash)
        # print(self.cash_avalia)
        if data.close > res.MA5[-1] :
            self.buy(code,data.close,self.get_cash())
        else :
            self.sell(code,data.close)

    def buy(self,code,price,amount):
        if self.get_positions(code).volume_long <=0:
            shou = math.floor(amount/price/100)
            self.send_order( direction='BUY', offset='OPEN', code=code, price=price, volume=shou*100)   
            print( str(price) + " 买" + str(shou*100)+ "股")
        #      print(self.get_positions(code).static_message)

    def sell(self,code,price):
        volume = self.get_positions(code).volume_long
        if volume>0:
            self.send_order(direction='SELL', offset='CLOSE', code=code, price=price, volume=volume) 
            print( str(price) + " 卖" + str(volume)+ "股")
        #      print(self.get_positions(code).static_message)

    def ma(self,):
        return QA.QA_indicator_MA(self.market_data, 5)

if __name__ == '__main__':
    s = strategy(code=['000001'], frequence='day', start='2016-01-01', end='2021-02-01', strategy_id='test1',init_cash = 10000)
    s.run_backtest()