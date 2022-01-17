import QUANTAXIS as QA
from QAStrategy.qastockbase import QAStrategyStockBase

class Strategy(QAStrategyStockBase):

    def on_bar(self, bar):
	    print(bar)

s = Strategy(code='000001', frequence='1min', strategy_id= 'xxx1' ) 
s.run_sim()
