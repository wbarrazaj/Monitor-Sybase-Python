SELECT '#SERVER#', '#BD#',( @@key_buffer_size
+ @@query_cache_size
+ @@innodb_buffer_pool_size
+ @@innodb_log_buffer_size
+ @@max_connections * ( 
    @@read_buffer_size
    + @@read_rnd_buffer_size
    + @@sort_buffer_size
    + @@join_buffer_size
    + @@binlog_cache_size
    + @@thread_stack
    + @@tmp_table_size )
) / (1024 * 1024 * 1024) AS MAX_MEMORY_GB
INTO OUTFILE '#SPOOLFILE#';
