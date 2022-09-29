SELECT s1.variable_value / s2.variable_value
INTO OUTFILE '#SPOOLFILE#'
FROM information_schema.global_status s1, information_schema.global_status s2
WHERE s1.variable_name='queries'
AND s2.variable_name ='uptime';


