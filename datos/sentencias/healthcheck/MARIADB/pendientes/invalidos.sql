SELECT object_name, object_type 
INTO OUTFILE '#SPOOLFILE#'
FROM user_objects
WHERE object_name NOT LIKE 'BIN$%' 
AND status='INVALID';
