-- use this line to using UUID generation--
CREATE EXTENSION "uuid-ossp";

CREATE TABLE "doituong" (
  "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  "client_name" varchar,
  "CMND" varchar,
  "CCCD" varchar,
  "Image" varchar,
  "Ngaysinh" date,
  "Gioitinh" boolean,
  "Quequan" varchar,
  "Thongtinbosung" varchar,
  "SDT" varchar,
  "KOL" boolean,
  "created_at" timestamp,
  "updated_at" timestamp
);


CREATE TABLE "tags" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "color" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "model_has_tags" (
  "id" SERIAL PRIMARY KEY,
  "model_id" varchar,
  "tags_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "uid" (
  "id" SERIAL PRIMARY KEY,
  "uid" varchar,
  "name" varchar,
  "reaction" int,
  "SDT" varchar,
  "trangthai_id" int,
  "type_id" int,
  "ghichu" varchar,
  "Vaiao" boolean,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "doituong_uid" (
  "id" SERIAL PRIMARY KEY,
  "doituong_id" uuid,
  "uid" varchar,
  "Moiquanhe_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "quantrivien" (
  "id" SERIAL PRIMARY KEY,
  "uid_facebook" varchar,
  "uid" varchar,
  "moiquanhe_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "trangthai" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "color" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "tinhchat" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "color" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "color" (
  "id" SERIAL PRIMARY KEY,
  "name"varchar,
  "color" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "trangthai_hoinhom" (
  "id" SERIAL PRIMARY KEY,
  "trangthai_id" int,
  "uid" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "ctnv" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "tinhchat_hoinhom" (
  "id" SERIAL PRIMARY KEY,
  "tinhchat_id" int,
  "uid" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "type" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "moiquanhe" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "donvi" (
  "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  "name" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "trichtin" (
  "id" SERIAL PRIMARY KEY,
  "uid" varchar,
  "ghichu_noidung" varchar,
  "nhanxet" varchar,
  "xuly" varchar,
  "uid_vaiao" varchar,
  "user_id" uuid,
  "created_at" timestamp,
  "updated_at" timestamp
);
CREATE TABLE "doituong_donvi" (
  "id" SERIAL PRIMARY KEY,
  "donvi_id" uuid NOT NULL,
  "doituong_id" uuid,
  "CTNV_ID" int,
  "created_at" timestamp,
  "updated_at" timestamp
);
CREATE TABLE "donvi_hoinhom" (
  "id" SERIAL PRIMARY KEY,
  "donvi_id" uuid NOT NULL,
  "uid" varchar,
  "CTNV_ID" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "user_donvi" (
  "id" SERIAL PRIMARY KEY,
  "user_id" uuid,
  "donvi_id" uuid,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "vaiao" (
  "id" SERIAL PRIMARY KEY,
  "uid_hoinhom" varchar,
  "uid_vaiao" varchar,
  "active" boolean,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "role" (
  "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  "name" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "permission" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "user_has_permissions" (
  "id" SERIAL PRIMARY KEY,
  "user_id" uuid,
  "permission_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "user_has_role" (
  "id" SERIAL PRIMARY KEY,
  "user_id" uuid,
  "role_id" uuid,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "role_has_permission" (
  "id" SERIAL PRIMARY KEY,
  "role_id" uuid,
  "permission_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "user" (
  "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  "username" varchar,
  "password" varchar,
  "salt" varchar,
  "active" varchar,
  "donvi_id" uuid NULL,
  "created_at" timestamp,
  "updated_at" timestamp
);
