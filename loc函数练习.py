import pandas as pd
from  mysqldb import MysqlDb

MYSQL_URL = 'mysql+pymysql://root:HONGhong1225@123.56.254.64/mcquant'
session = MysqlDb()
engline = session.connect_mysql(MYSQL_URL)

df = pd.read_sql_table('dict_table', engline)
ts_codes = df['股票代码'].tolist()
company_names = df['公司名称'].tolist()
trade_dates = df['交易日期'].tolist()
df_dict_table = pd.read_sql_table('dict_table', engline)
datas = list(zip(ts_codes, company_names, trade_dates))
for data in datas:
    if data[0] in df_dict_table['ts_code'].tolist():
        # 更新涨停次数
        df_dict_table.loc[(df_dict_table[
                               'ts_code'] == data[
                               0]), 'limit_increases_number'] = \
        df_dict_table.loc[(df_dict_table[
                               'ts_code'] == data[
                               0]), 'limit_increases_number'] + 1
        # 更新涨停时间
        df_dict_table.loc[(df_dict_table[
                               'ts_code'] == data[0]), 'end_time'] = data[2]
        # print(type(limit_increases_number))
        logging.info("df_dict_table 更新 limit_increases_number %s",
                     df_dict_table)

    else:
        new_dict = {'ts_code': data[0], 'company_name': data[1],
                    'start_time': data[2], 'limit_increases_number': 1}
        new_df = pd.DataFrame(new_dict, index=[0])
        # logging.info(new_df)
        df_dict_table = pd.concat([new_df, df_dict_table])
        logging.info('dict_table %s', df_dict_table)
self.session.write_to_mysql(df_dict_table, self.session.mysql_eng,
                            self.mysql_table2,
                            )
