#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import sqlalchemy as db
from time import time

engine=db.create_engine('postgresql://root:root@localhost:5432/ny_taxi')


df_iter=pd.read_csv('yellow_tripdata_2023-01.csv',iterator=True, chunksize=100000)
df = next(df_iter)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)


engine.connect()

print(pd.io.sql.get_schema(df,name='yellow_taxi_data',con=engine))

df.head(n=0).to_sql(name='yellow_taxi_data',con=engine,if_exists='replace')
df.to_sql(name='yellow_taxi_data',con=engine,if_exists='append')

while True:
    t_start = time()
    df = next(df_iter)

    df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)


    t_end =time()
    
    print('inserted aonther chunks ...., took %.3f second' % (t_end - t_start))




