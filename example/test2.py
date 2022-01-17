import QUANTAXIS as QA
import pandas as pd
from QUANTAXIS.QAUtil import (
    DATABASE,
    QA_Setting,
    QA_util_date_stamp,
    QA_util_date_valid,
    QA_util_dict_remove_key,
    QA_util_log_info,
    QA_util_code_tolist,
    QA_util_date_str2int,
    QA_util_date_int2str,
    QA_util_sql_mongo_sort_DESCENDING,
    QA_util_time_stamp,
    QA_util_to_json_from_pandas,
    trade_date_sse
)

code_list = QA.QA_fetch_stock_list().index.tolist()
aaa = DATABASE.stock_list
print(aaa)
# print(code_list)
# data = QA.QA_fetch_stock_day_adv(code=code_list, start='2019-01-01', end='2019-12-01').to_qfq()
# df_adj = data.pivot('adj').ffill()
# df_adj.to_csv("20190101_20191201_adj.csv")