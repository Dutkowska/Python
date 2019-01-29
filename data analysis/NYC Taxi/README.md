This is sample analysis of data set from:

http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml

We have here informations about green taxies from NYC, 01.2018. 

Libraries: 
Pandas / Numpy / Seaborn / Matplotlib / Datetime


File Correlation is part of data cleaning, but I created new file for this part of job. 

1. data_cleaning:
  - check duplicates;
  - delete null values;
  - compare the range of columns to informations about datas;
  - delete outliers;
  - make right data type of datetime;
  - get days/hours/minutes from dates;
  - check if time values are valid (lpep_dropoff_datetime < lpep_pickup_datetime);
  - save to new file. 
2. Correlations:
  - find related columns;
  - delete datas such as: Column = sum_of_other_columns.
3. Analysis-time.
4. Analysis_simple.


Conclusions: 
1. Time:
  - HOURS:
    + rush hours: 17 - 20
    + the smallest traffic: 4 - 6
    + people get out of/go to work at: 8-10, after 15
    + we need more taxes after 15
  - DAYS:
    + we have some decrease on day 4. Solution: weather problems (blizzard)
    + we see when we had weekend (wave increase in every week)
2. Group rides:
  - there are no rides with RatecodeID='group_rides';
  - why? Maybe 'cause we had only 31(!) courses with more than 6 passengers
  - we don't need to but more "big" cars for group rides.
