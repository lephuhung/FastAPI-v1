-- use this line to using UUID generation--
CREATE EXTENSION "uuid-ossp";

CREATE TABLE "individual" (
  "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  "full_name" varchar,
  "national_id" varchar,
  "citizen_id" varchar,
  "image_url" varchar,
  "date_of_birth" date,
  "is_male" boolean,
  "hometown" varchar,
  "additional_info" varchar,
  "phone_number" varchar,
  "is_kol" boolean,
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
  "phone_number" varchar,
  "status" int,
  "type_id" int,
  "note" varchar,
  "Vaiao" boolean,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "individual_uid" (
  "id" SERIAL PRIMARY KEY,
  "individual_id" uuid,
  "uid" varchar,
  "Moiquanhe_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "quantrivien" (
  "id" SERIAL PRIMARY KEY,
  "uid_facebook" varchar,
  "uid" varchar,
  "relationship_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "status" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "color" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "characteristic" (
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
  "status" int,
  "uid" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "task" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "characteristic_hoinhom" (
  "id" SERIAL PRIMARY KEY,
  "characteristic_id" int,
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

CREATE TABLE "relationship" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "unit" (
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
  "user_id" uuid
  "created_at" timestamp,
  "updated_at" timestamp
);
CREATE TABLE "individual_unit" (
  "id" SERIAL PRIMARY KEY,
  "unit_id" uuid NOT NULL,
  "individual_id" uuid,
  "CTNV_ID" int,
  "created_at" timestamp,
  "updated_at" timestamp
);
CREATE TABLE "unit_hoinhom" (
  "id" SERIAL PRIMARY KEY,
  "unit_id" uuid NOT NULL,
  "uid" varchar,
  "CTNV_ID" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "user_unit" (
  "id" SERIAL PRIMARY KEY,
  "user_id" uuid,
  "unit_id" uuid,
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
  "unit_id" uuid NULL,
  "created_at" timestamp,
  "updated_at" timestamp
);
