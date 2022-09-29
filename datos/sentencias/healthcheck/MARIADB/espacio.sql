select table_schema, sum((data_length+index_length)/1024/1024) AS MB 
INTO OUTFILE '#SPOOLFILE#'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
from information_schema.tables 
group by 1;
