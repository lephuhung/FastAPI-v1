#!/bin/bash

# Đợi các service khởi động
echo "Waiting for PostgreSQL..."
wait-for-it $PG_HOST:5432 -t 60
echo "Waiting for Elasticsearch..."
wait-for-it $ELASTICSEARCH_HOST:9200 -t 120

# Cập nhật tên database trong schema.json
echo "Updating database name in schema.json..."
jq '.[].database = env.PG_DATABASE' schema.json | sponge schema.json

# Kiểm tra và tạo replication slots
echo "Checking replication slots..."
if ! psql -h $PG_HOST -U $PG_USER -d $PG_DATABASE -c "SELECT * FROM pg_replication_slots;" > /dev/null 2>&1; then
    echo "Creating replication slots..."
    psql -h $PG_HOST -U $PG_USER -d $PG_DATABASE -c "SELECT * FROM pg_create_logical_replication_slot('pgsync_slot', 'pgoutput');"
fi

# Kiểm tra và tạo các bảng cần thiết
echo "Checking and creating required tables..."
psql -h $PG_HOST -U $PG_USER -d $PG_DATABASE -f /app/init-db.sql

# Kiểm tra xem các bảng đã tồn tại chưa
echo "Verifying tables exist..."
if ! psql -h $PG_HOST -U $PG_USER -d $PG_DATABASE -c "\dt" | grep -q "relationships"; then
    echo "Error: Table 'relationships' not found"
    exit 1
fi
if ! psql -h $PG_HOST -U $PG_USER -d $PG_DATABASE -c "\dt" | grep -q "reports"; then
    echo "Error: Table 'reports' not found"
    exit 1
fi
if ! psql -h $PG_HOST -U $PG_USER -d $PG_DATABASE -c "\dt" | grep -q "social_accounts"; then
    echo "Error: Table 'social_accounts' not found"
    exit 1
fi
if ! psql -h $PG_HOST -U $PG_USER -d $PG_DATABASE -c "\dt" | grep -q "individuals"; then
    echo "Error: Table 'individuals' not found"
    exit 1
fi

# Chạy populate.sql để thêm dữ liệu mẫu
echo "Populating database with sample data..."
psql -h $PG_HOST -U $PG_USER -d $PG_DATABASE -f /app/populate.sql

# Chạy bootstrap và kiểm tra kết quả
echo "Running bootstrap..."
bootstrap --config ./schema.json
if [ $? -eq 0 ]; then
    echo "Bootstrap completed successfully"
else
    echo "Bootstrap failed"
    exit 1
fi

# Chạy pgsync với chế độ daemon
echo "Starting pgsync..."
pgsync --config ./schema.json -d

# Kiểm tra trạng thái pgsync
echo "Checking pgsync status..."
sleep 5
if pgrep -f "pgsync" > /dev/null; then
    echo "pgsync is running"
else
    echo "pgsync failed to start"
    exit 1
fi
