import QUANTAXIS as QA
from QAStrategy.qactabase import QAStrategyCTABase

class Strategy(QAStrategyCTABase):

    def on_bar(self, bar):
	    print(bar)

s = Strategy(code='rb2205', frequence='1min', strategy_id= 'xxx1' ) 
s.run_sim()
