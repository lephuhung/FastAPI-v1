-- Cấu hình logical replication
ALTER SYSTEM SET wal_level = logical;
ALTER SYSTEM SET max_replication_slots = 5;
ALTER SYSTEM SET max_wal_senders = 5;
ALTER SYSTEM SET max_connections = 100;

-- Cấu hình bổ sung cho pgsync
ALTER SYSTEM SET track_commit_timestamp = on;
ALTER SYSTEM SET log_min_messages = 'debug1';
ALTER SYSTEM SET log_min_error_statement = 'debug1';

-- Áp dụng cấu hình
SELECT pg_reload_conf();

-- set this value to the number of tables you want to load into elastic
-- for now we only have one table called product
