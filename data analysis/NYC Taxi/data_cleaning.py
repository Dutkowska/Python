"""
i'm using dataset from: 
http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml
January/2018 - Green taxi.
-- quick cleaning for my own -- 
"""
#shorter version for importing
"""
my solution - i didn't delete correlations
f.e. total_amount & trip_distance & fare_amount
In real job I have should done this. 
Why? Heat map of correlation with seaborn using... and laziness ;)
"""

import numpy as np
import pandas as pd
path='green_tripdata_2018-01.csv'
taxi=pd.read_csv(path)

taxi.drop('ehail_fee', axis=1, inplace=True)
taxi=taxi[np.isfinite(taxi['trip_type'])]

taxi=taxi[taxi.passenger_count!=0]

total_amount_limity = [2, 100]
taxi = taxi[(taxi.total_amount.between(total_amount_limity[0], total_amount_limity[1], inclusive=False))]

tip_amount_limity = [0, 12]
taxi = taxi[(taxi.tip_amount.between(tip_amount_limity[0], tip_amount_limity[1],
inclusive=False))]

Distance_limity = [0, 20]
taxi = taxi[(taxi.trip_distance.between(Distance_limity[0], Distance_limity[1],inclusive=False))]

taxi["lpep_pickup_datetime"] = pd.to_datetime(taxi["lpep_pickup_datetime"])
taxi["Lpep_dropoff_datetime"] = pd.to_datetime(taxi["lpep_dropoff_datetime"])

taxi.to_csv('datas.csv', index=False)