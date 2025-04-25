--   -- use this line to using UUID generation--
-- CREATE EXTENSION "uuid-ossp";

-- CREATE TABLE "doituong" (
--   "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
--   "client_name" varchar,
--   "CMND" varchar,
--   "CCCD" varchar,
--   "Image" varchar,
--   "Ngaysinh" date,
--   "Gioitinh" boolean,
--   "Quequan" varchar,
--   "Thongtinbosung" varchar,
--   "SDT" varchar,
--   "KOL" boolean,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );


-- CREATE TABLE "tags" (
--   "id" SERIAL PRIMARY KEY,
--   "name" varchar,
--   "color" varchar,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "model_has_tags" (
--   "id" SERIAL PRIMARY KEY,
--   "model_id" varchar,
--   "tags_id" int,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "uid" (
--   "id" SERIAL PRIMARY KEY,
--   "uid" varchar,
--   "name" varchar,
--   "reaction" int,
--   "SDT" varchar,
--   "trangthai_id" int,
--   "type_id" int,
--   "ghichu" varchar,
--   "Vaiao" boolean,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "doituong_uid" (
--   "id" SERIAL PRIMARY KEY,
--   "doituong_id" uuid,
--   "uid" varchar,
--   "Moiquanhe_id" int,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "quantrivien" (
--   "id" SERIAL PRIMARY KEY,
--   "uid_facebook" varchar,
--   "uid" varchar,
--   "Moiquanhe_id" int,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "trangthai" (
--   "id" SERIAL PRIMARY KEY,
--   "name" varchar,
--   "color" varchar,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "tinhchat" (
--   "id" SERIAL PRIMARY KEY,
--   "name" varchar,
--   "color" varchar,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "color" (
--   "id" SERIAL PRIMARY KEY,
--   "name"varchar,
--   "color" varchar,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "trangthai_hoinhom" (
--   "id" SERIAL PRIMARY KEY,
--   "trangthai_id" int,
--   "uid" varchar,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "ctnv" (
--   "id" SERIAL PRIMARY KEY,
--   "name" varchar,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "tinhchat_hoinhom" (
--   "id" SERIAL PRIMARY KEY,
--   "tinhchat_id" int,
--   "uid" varchar,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "type" (
--   "id" SERIAL PRIMARY KEY,
--   "name" varchar,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "moiquanhe" (
--   "id" SERIAL PRIMARY KEY,
--   "name" varchar,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "donvi" (
--   "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
--   "name" varchar,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "trichtin" (
--   "id" SERIAL PRIMARY KEY,
--   "uid" varchar,
--   "ghichu_noidung" varchar,
--   "nhanxet" varchar,
--   "xuly" varchar,
--   "uid_vaiao" varchar,
--   "user_id" uuid,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );
-- CREATE TABLE "doituong_donvi" (
--   "id" SERIAL PRIMARY KEY,
--   "donvi_id" uuid NOT NULL,
--   "doituong_id" uuid,
--   "CTNV_ID" int,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );
-- CREATE TABLE "donvi_hoinhom" (
--   "id" SERIAL PRIMARY KEY,
--   "donvi_id" uuid NOT NULL,
--   "uid" varchar,
--   "CTNV_ID" int,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "user_donvi" (
--   "id" SERIAL PRIMARY KEY,
--   "user_id" uuid,
--   "donvi_id" uuid,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "vaiao" (
--   "id" SERIAL PRIMARY KEY,
--   "uid_hoinhom" varchar,
--   "uid_vaiao" varchar,
--   "active" boolean,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "role" (
--   "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
--   "name" varchar,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "permission" (
--   "id" SERIAL PRIMARY KEY,
--   "name" varchar,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "user_has_permissions" (
--   "id" SERIAL PRIMARY KEY,
--   "user_id" uuid,
--   "permission_id" int,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "user_has_role" (
--   "id" SERIAL PRIMARY KEY,
--   "user_id" uuid,
--   "role_id" uuid,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "role_has_permission" (
--   "id" SERIAL PRIMARY KEY,
--   "role_id" uuid,
--   "permission_id" int,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );

-- CREATE TABLE "user" (
--   "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
--   "username" varchar,
--   "password" varchar,
--   "salt" varchar,
--   "active" varchar,
--   "donvi_id" uuid NULL,
--   "created_at" timestamp,
--   "updated_at" timestamp
-- );
-- Kích hoạt tiện ích UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Tạo các bảng cơ bản không có khóa ngoại
CREATE TABLE "individuals" (
  "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  "full_name" varchar(255) NOT NULL,
  "national_id" varchar(20),
  "citizen_id" varchar(20),
  "image_url" varchar(255),
  "date_of_birth" date,
  "is_male" boolean,
  "hometown" varchar(255),
  "additional_info" text,
  "phone_number" varchar(15) CHECK ("phone_number" ~ '^[0-9]{10,15}$'),
  "is_kol" boolean DEFAULT false,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW()
);
CREATE INDEX idx_individuals_phone_number ON "individuals" ("phone_number");

CREATE TABLE "tags" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "color" varchar(7) CHECK ("color" ~ '^#[0-9A-Fa-f]{6}$'),
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_tag_name UNIQUE ("name")
);

CREATE TABLE "statuses" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "color" varchar(7) CHECK ("color" ~ '^#[0-9A-Fa-f]{6}$'),
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_status_name UNIQUE ("name")
);

CREATE TABLE "characteristics" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "color" varchar(7) CHECK ("color" ~ '^#[0-9A-Fa-f]{6}$'),
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_characteristic_name UNIQUE ("name")
);

CREATE TABLE "tasks" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(255) NOT NULL,
  "description" text,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_task_name UNIQUE ("name")
);

CREATE TABLE "account_types" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_type_name UNIQUE ("name")
);

CREATE TABLE "relationships" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_relationship_name UNIQUE ("name")
);

CREATE TABLE "units" (
  "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  "name" varchar(255) NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_unit_name UNIQUE ("name")
);

CREATE TABLE "roles" (
  "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_role_name UNIQUE ("name")
);

CREATE TABLE "permissions" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_permission_name UNIQUE ("name")
);

CREATE TABLE "users" (
  "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  "username" varchar(100) NOT NULL,
  "password" varchar(255) NOT NULL,
  "salt" varchar(255) NOT NULL,
  "is_active" boolean DEFAULT true,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_username UNIQUE ("username")
);
CREATE INDEX idx_users_username ON "users" ("username");

-- 2. Tạo các bảng có khóa ngoại
CREATE TABLE "social_accounts" (
  "id" SERIAL PRIMARY KEY,
  "uid" varchar(100) NOT NULL,
  "name" varchar(255),
  "reaction_count" int DEFAULT 0,
  "phone_number" varchar(15) CHECK ("phone_number" ~ '^[0-9]{10,15}$'),
  "status_id" int,
  "type_id" int,
  "note" text,
  "is_active" boolean DEFAULT true,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_uid UNIQUE ("uid"),
  CONSTRAINT fk_social_accounts_status FOREIGN KEY ("status_id") REFERENCES "statuses" ("id") ON DELETE RESTRICT,
  CONSTRAINT fk_social_accounts_type FOREIGN KEY ("type_id") REFERENCES "account_types" ("id") ON DELETE RESTRICT
);
CREATE INDEX idx_social_accounts_uid ON "social_accounts" ("uid");

CREATE TABLE "individual_tags" (
  "id" SERIAL PRIMARY KEY,
  "individual_id" uuid NOT NULL,
  "tag_id" int NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_individual_tags_individual FOREIGN KEY ("individual_id") REFERENCES "individuals" ("id") ON DELETE CASCADE,
  CONSTRAINT fk_individual_tags_tag FOREIGN KEY ("tag_id") REFERENCES "tags" ("id") ON DELETE CASCADE
);
CREATE INDEX idx_individual_tags_individual_id ON "individual_tags" ("individual_id");
CREATE INDEX idx_individual_tags_tag_id ON "individual_tags" ("tag_id");

CREATE TABLE "individual_social_accounts" (
  "id" SERIAL PRIMARY KEY,
  "individual_id" uuid NOT NULL,
  "social_account_uid" varchar(100) NOT NULL,
  "relationship_id" int NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_individual_social_accounts_individual FOREIGN KEY ("individual_id") REFERENCES "individuals" ("id") ON DELETE CASCADE,
  CONSTRAINT fk_individual_social_accounts_social_account FOREIGN KEY ("social_account_uid") REFERENCES "social_accounts" ("uid") ON DELETE CASCADE,
  CONSTRAINT fk_individual_social_accounts_relationship FOREIGN KEY ("relationship_id") REFERENCES "relationships" ("id") ON DELETE RESTRICT
);
CREATE INDEX idx_individual_social_accounts_individual_id ON "individual_social_accounts" ("individual_id");
CREATE INDEX idx_individual_social_accounts_social_account_uid ON "individual_social_accounts" ("social_account_uid");

CREATE TABLE "administrators" (
  "id" SERIAL PRIMARY KEY,
  "facebook_uid" varchar(100) NOT NULL,
  "social_account_uid" varchar(100) NOT NULL,
  "relationship_id" int NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_facebook_uid UNIQUE ("facebook_uid"),
  CONSTRAINT fk_administrators_social_account FOREIGN KEY ("social_account_uid") REFERENCES "social_accounts" ("uid") ON DELETE CASCADE,
  CONSTRAINT fk_administrators_relationship FOREIGN KEY ("relationship_id") REFERENCES "relationships" ("id") ON DELETE RESTRICT
);
CREATE INDEX idx_administrators_facebook_uid ON "administrators" ("facebook_uid");

CREATE TABLE "group_statuses" (
  "id" SERIAL PRIMARY KEY,
  "status_id" int NOT NULL,
  "social_account_uid" varchar(100) NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_group_statuses_status FOREIGN KEY ("status_id") REFERENCES "statuses" ("id") ON DELETE RESTRICT,
  CONSTRAINT fk_group_statuses_social_account FOREIGN KEY ("social_account_uid") REFERENCES "social_accounts" ("uid") ON DELETE CASCADE
);
CREATE INDEX idx_group_statuses_social_account_uid ON "group_statuses" ("social_account_uid");

CREATE TABLE "group_characteristics" (
  "id" SERIAL PRIMARY KEY,
  "characteristic_id" int NOT NULL,
  "social_account_uid" varchar(100) NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_group_characteristics_characteristic FOREIGN KEY ("characteristic_id") REFERENCES "characteristics" ("id") ON DELETE RESTRICT,
  CONSTRAINT fk_group_characteristics_social_account FOREIGN KEY ("social_account_uid") REFERENCES "social_accounts" ("uid") ON DELETE CASCADE
);
CREATE INDEX idx_group_characteristics_social_account_uid ON "group_characteristics" ("social_account_uid");

CREATE TABLE "reports" (
  "id" SERIAL PRIMARY KEY,
  "social_account_uid" varchar(100) NOT NULL,
  "content_note" text,
  "comment" text,
  "action" text,
  "related_social_account_uid" varchar(100),
  "user_id" uuid,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_reports_social_account FOREIGN KEY ("social_account_uid") REFERENCES "social_accounts" ("uid") ON DELETE CASCADE,
  CONSTRAINT fk_reports_related_social_account FOREIGN KEY ("related_social_account_uid") REFERENCES "social_accounts" ("uid") ON DELETE SET NULL,
  CONSTRAINT fk_reports_user FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE SET NULL
);
CREATE INDEX idx_reports_social_account_uid ON "reports" ("social_account_uid");

CREATE TABLE "individual_units" (
  "id" SERIAL PRIMARY KEY,
  "unit_id" uuid NOT NULL,
  "individual_id" uuid NOT NULL,
  "task_id" int NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_individual_units_unit FOREIGN KEY ("unit_id") REFERENCES "units" ("id") ON DELETE RESTRICT,
  CONSTRAINT fk_individual_units_individual FOREIGN KEY ("individual_id") REFERENCES "individuals" ("id") ON DELETE CASCADE,
  CONSTRAINT fk_individual_units_task FOREIGN KEY ("task_id") REFERENCES "tasks" ("id") ON DELETE RESTRICT
);
CREATE INDEX idx_individual_units_unit_id ON "individual_units" ("unit_id");
CREATE INDEX idx_individual_units_individual_id ON "individual_units" ("individual_id");

CREATE TABLE "unit_groups" (
  "id" SERIAL PRIMARY KEY,
  "unit_id" uuid NOT NULL,
  "social_account_uid" varchar(100) NOT NULL,
  "task_id" int NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_unit_groups_unit FOREIGN KEY ("unit_id") REFERENCES "units" ("id") ON DELETE RESTRICT,
  CONSTRAINT fk_unit_groups_social_account FOREIGN KEY ("social_account_uid") REFERENCES "social_accounts" ("uid") ON DELETE CASCADE,
  CONSTRAINT fk_unit_groups_task FOREIGN KEY ("task_id") REFERENCES "tasks" ("id") ON DELETE RESTRICT
);
CREATE INDEX idx_unit_groups_unit_id ON "unit_groups" ("unit_id");
CREATE INDEX idx_unit_groups_social_account_uid ON "unit_groups" ("social_account_uid");

CREATE TABLE "user_units" (
  "id" SERIAL PRIMARY KEY,
  "user_id" uuid NOT NULL,
  "unit_id" uuid NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_user_units_user FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE,
  CONSTRAINT fk_user_units_unit FOREIGN KEY ("unit_id") REFERENCES "units" ("id") ON DELETE RESTRICT
);
CREATE INDEX idx_user_units_user_id ON "user_units" ("user_id");
CREATE INDEX idx_user_units_unit_id ON "user_units" ("unit_id");

CREATE TABLE "user_permissions" (
  "id" SERIAL PRIMARY KEY,
  "user_id" uuid NOT NULL,
  "permission_id" int NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_user_permissions_user FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE,
  CONSTRAINT fk_user_permissions_permission FOREIGN KEY ("permission_id") REFERENCES "permissions" ("id") ON DELETE CASCADE
);
CREATE INDEX idx_user_permissions_user_id ON "user_permissions" ("user_id");

CREATE TABLE "user_roles" (
  "id" SERIAL PRIMARY KEY,
  "user_id" uuid NOT NULL,
  "role_id" uuid NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_user_roles_user FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE,
  CONSTRAINT fk_user_roles_role FOREIGN KEY ("role_id") REFERENCES "roles" ("id") ON DELETE CASCADE
);
CREATE INDEX idx_user_roles_user_id ON "user_roles" ("user_id");

CREATE TABLE "role_permissions" (
  "id" SERIAL PRIMARY KEY,
  "role_id" uuid NOT NULL,
  "permission_id" int NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_role_permissions_role FOREIGN KEY ("role_id") REFERENCES "roles" ("id") ON DELETE CASCADE,
  CONSTRAINT fk_role_permissions_permission FOREIGN KEY ("permission_id") REFERENCES "permissions" ("id") ON DELETE CASCADE
);
CREATE INDEX idx_role_permissions_role_id ON "role_permissions" ("role_id");

CREATE TABLE "social_account_links" (
  "id" SERIAL PRIMARY KEY,
  "group_social_account_uid" varchar(100) NOT NULL,
  "linked_social_account_uid" varchar(100) NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_social_account_links_group FOREIGN KEY ("group_social_account_uid") REFERENCES "social_accounts" ("uid") ON DELETE CASCADE,
  CONSTRAINT fk_social_account_links_linked FOREIGN KEY ("linked_social_account_uid") REFERENCES "social_accounts" ("uid") ON DELETE CASCADE
);
CREATE INDEX idx_social_account_links_group_social_account_uid ON "social_account_links" ("group_social_account_uid");