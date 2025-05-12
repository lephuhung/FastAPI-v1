DEVELOPE:
docker-compose -f docker-compose.dev.yml exec qlcv_dev python manage.py migrate
docker-compose -f docker-compose.dev.yml restart qlcv_dev



docker save -o myimage.tar myimage:latest

docker save -o <output_path> <image_name1>:<tag1> <image_name2>:<tag2>
docker save -o qlcvd4.tar qlcv_api:latest qlcv_api_celery_worker:latest qlcv_api_flower:latest backend-nginx:latest qlcv_api_database:latest redis:7.2.4-alpine   


docker save <image_name>:<tag> | gzip > <output_path>.tar.gz


docker load -i <input_path>

docker network create qlcv_nw

docker exec -it --user root backend-qlcv-1 /bin/bash

docker cp . nginx:/usr/share/nginx/html/qlcv

copy:
	docker cp <container_id hoặc container_name>:<đường_dẫn_trong_container> <đường_dẫn_trên_host>



mont volume:

docker run -d --name backend-qlcv-1 -v /mnt/shared:/app_data my_image


build:
	docker compose -f docker-compose.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up -d

down:
	docker compose -f local.yml down

show-logs:
	docker compose -f local.yml logs
