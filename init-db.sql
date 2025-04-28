-- Kích hoạt tiện ích UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Bảng đối tượng (individuals)
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

-- Bảng nhãn (tags)
CREATE TABLE "tags" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "color" varchar(7) CHECK ("color" ~ '^#[0-9A-Fa-f]{6}$'),
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_tag_name UNIQUE ("name")
);

-- Bảng liên kết giữa đối tượng và nhãn
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

-- Bảng tài khoản mạng xã hội (social_accounts)
CREATE TABLE "social_accounts" (
  "id" SERIAL PRIMARY KEY,
  "uid" varchar(100) NOT NULL,
  "name" varchar(255),
  "reaction_count" int DEFAULT 0,
  "phone_number" varchar(15) CHECK ("phone_number" ~ '^[0-9]{10,15}$'),
  "status_id" int,
  "account_type_id" int,
  "note" text,
  "is_active" boolean DEFAULT true,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_uid UNIQUE ("uid")
);
CREATE INDEX idx_social_accounts_uid ON "social_accounts" ("uid");

-- Bảng liên kết giữa đối tượng và tài khoản mạng xã hội
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

-- Bảng quản trị viên (administrators)
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

-- Bảng trạng thái (statuses)
CREATE TABLE "statuses" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "color" varchar(7) CHECK ("color" ~ '^#[0-9A-Fa-f]{6}$'),
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_status_name UNIQUE ("name")
);

-- Bảng tính chất (characteristics)
CREATE TABLE "characteristics" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "color" varchar(7) CHECK ("color" ~ '^#[0-9A-Fa-f]{6}$'),
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_characteristic_name UNIQUE ("name")
);

-- Bảng trạng thái hội nhóm (group_statuses)
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

-- Bảng nhiệm vụ (tasks)
CREATE TABLE "tasks" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(255) NOT NULL,
  "description" text,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_task_name UNIQUE ("name")
);

-- Bảng tính chất hội nhóm (group_characteristics)
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

-- Bảng loại tài khoản (account_types)
CREATE TABLE "account_types" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_type_name UNIQUE ("name")
);

-- Bảng mối quan hệ (relationships)
CREATE TABLE "relationships" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_relationship_name UNIQUE ("name")
);

-- Bảng đơn vị (units)
CREATE TABLE "units" (
  "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  "name" varchar(255) NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_unit_name UNIQUE ("name")
);

-- Bảng trích tin (reports)
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

-- Bảng liên kết giữa đối tượng và đơn vị
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

-- Bảng liên kết giữa đơn vị và hội nhóm
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

-- Bảng liên kết giữa người dùng và đơn vị
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

-- Bảng vai trò (roles)
CREATE TABLE "roles" (
  "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_role_name UNIQUE ("name")
);

-- Bảng quyền (permissions)
CREATE TABLE "permissions" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_permission_name UNIQUE ("name")
);

-- Bảng liên kết giữa người dùng và quyền
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

-- Bảng liên kết giữa người dùng và vai trò
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

-- Bảng liên kết giữa vai trò và quyền
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

-- Bảng người dùng (users)
CREATE TABLE "users" (
  "id" uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  "username" varchar(50) NOT NULL,
  "password" varchar(255) NOT NULL,
  "salt" varchar(255) NOT NULL,
  "is_active" boolean DEFAULT true,
  "unit_id" uuid,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_username UNIQUE ("username"),
  CONSTRAINT fk_users_unit FOREIGN KEY ("unit_id") REFERENCES "units" ("id") ON DELETE SET NULL
);
CREATE INDEX idx_users_username ON "users" ("username");

-- Bảng liên kết tài khoản mạng xã hội (social_account_links)
CREATE TABLE "social_account_links" (
  "id" SERIAL PRIMARY KEY,
  "group_social_account_uid" varchar(100) NOT NULL,
  "related_social_account_uid" varchar(100) NOT NULL,
  "is_active" boolean DEFAULT true,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_social_account_links_group_social_account FOREIGN KEY ("group_social_account_uid") REFERENCES "social_accounts" ("uid") ON DELETE CASCADE,
  CONSTRAINT fk_social_account_links_related_social_account FOREIGN KEY ("related_social_account_uid") REFERENCES "social_accounts" ("uid") ON DELETE CASCADE
);
CREATE INDEX idx_social_account_links_group_social_account_uid ON "social_account_links" ("group_social_account_uid");