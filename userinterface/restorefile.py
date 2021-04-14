import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:Silver@123@localhost:3306/salesordersdb')


df_ui = pd.read_csv("static/restore_column.csv")

df_ui.to_sql(
    name='ui',
    con=engine,
    index=False,
    if_exists='fail'
)