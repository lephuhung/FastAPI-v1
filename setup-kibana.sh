#!/bin/bash

# Đợi Elasticsearch khởi động hoàn toàn
until curl -s http://elasticsearch:9200 >/dev/null; do
  echo "Waiting for Elasticsearch to start..."
  sleep 5
done

# Cấu hình mật khẩu cho tài khoản kibana_system
echo "Setting up kibana_system password..."
curl -X POST -u elastic:${ELASTIC_PASSWORD} \
  -H "Content-Type: application/json" \
  -d "{\"password\":\"${KIBANA_SYSTEM_PASSWORD}\"}" \
  http://elasticsearch:9200/_security/user/kibana_system/_password

# Cấu hình role cho kibana_system
echo "Setting up kibana_system role..."
curl -X PUT -u elastic:${ELASTIC_PASSWORD} \
  -H "Content-Type: application/json" \
  -d '{
    "cluster": ["monitor", "manage_index_templates", "manage_ilm"],
    "indices": [
      {
        "names": [".kibana*", ".reporting-*", ".apm-*", ".ml-*"],
        "privileges": ["all"]
      }
    ]
  }' \
  http://elasticsearch:9200/_security/role/kibana_system

# Tạo service account cho Kibana
echo "Creating Kibana service account..."
curl -X POST -u elastic:${ELASTIC_PASSWORD} \
  -H "Content-Type: application/json" \
  -d '{
    "name": "kibana",
    "role_descriptors": {
      "kibana_system": {
        "cluster": ["monitor", "manage_index_templates", "manage_ilm"],
        "index": [
          {
            "names": [".kibana*", ".reporting-*", ".apm-*", ".ml-*"],
            "privileges": ["all"]
          }
        ]
      }
    }
  }' \
  http://elasticsearch:9200/_security/service/elastic/kibana

# Lấy token
echo "Getting service account token..."
TOKEN=$(curl -s -u elastic:${ELASTIC_PASSWORD} \
  -H "Content-Type: application/json" \
  -d '{"name": "kibana"}' \
  http://elasticsearch:9200/_security/service/elastic/kibana/credential/token/kibana-token | jq -r '.token.value')

# Lưu token vào file .env
echo "KIBANA_SERVICE_ACCOUNT_TOKEN=$TOKEN" >> .env

echo "Kibana service account setup completed!"

echo "Kibana setup completed!" 