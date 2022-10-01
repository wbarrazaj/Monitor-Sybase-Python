select '#SERVER#','#BD#', round(sum((data_length+index_length)/1024/1024),2) AS USED_MB, round(sum(data_free)/1024/1024,2) as FREE_MB 
INTO OUTFILE '#SPOOLFILE#'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
from information_schema.tables ;
