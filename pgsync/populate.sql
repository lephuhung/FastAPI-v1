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

-- Insert sample data for units
INSERT INTO "units" ("name") VALUES
('PA01'), ('PA02'), ('PA03'), ('PA04'), ('PA05'), ('PA06'), ('PA08'), ('PA09'),
('PC01'), ('PC02'), ('PC03'), ('PC04'), ('PC06'), ('PC07'), ('PC08'), ('PC09'),
('PC10'), ('PC11'), ('PK02'), ('Thành phố Hà Tĩnh'), ('Thị xã Hồng Lĩnh'),
('Thị xã Kỳ Anh'), ('Huyện Nghi Xuân'), ('Huyện Đức Thọ'), ('Huyện Hương Sơn'),
('Huyện Hương Khê'), ('Huyện Vũ Quang'), ('Huyện Can Lộc'), ('Huyện Thạch Hà'),
('Huyện Lộc Hà'), ('Huyện Cẩm Xuyên'), ('Huyện Kỳ Anh'), ('Đơn vị khác');

-- Insert sample data for roles
INSERT INTO "roles" ("name") VALUES
('superadmin'), ('admin'), ('Phong'), ('CAX'), ('DOI');

-- Insert sample data for permissions
INSERT INTO "permissions" ("name") VALUES
-- Quyền quản lý người dùng
('user.all'), ('user.read'), ('user.update'), ('user.delete'), ('user.create'),
-- Quyền quản lý vai trò
('role.all'), ('role.read'), ('role.update'), ('role.delete'), ('role.create'),
-- Quyền quản lý nhiệm vụ
('task.all'), ('task.read'), ('task.update'), ('task.delete'), ('task.create'),
-- Quyền quản lý cá nhân
('individual.all'), ('individual.read'), ('individual.update'), ('individual.delete'), ('individual.create'),
-- Quyền quản lý tài khoản mạng xã hội
('social_account.all'), ('social_account.read'), ('social_account.update'), ('social_account.delete'), ('social_account.create'),
-- Quyền quản lý thẻ
('tag.all'), ('tag.read'), ('tag.update'), ('tag.delete'), ('tag.create'),
-- Quyền quản lý đặc điểm
('characteristic.all'), ('characteristic.read'), ('characteristic.update'), ('characteristic.delete'), ('characteristic.create'),
-- Quyền quản lý trạng thái
('status.all'), ('status.read'), ('status.update'), ('status.delete'), ('status.create'),
-- Quyền quản lý báo cáo
('report.all'), ('report.read'), ('report.update'), ('report.delete'), ('report.create'),
-- Quyền quản lý đơn vị
('unit.all'), ('unit.read'), ('unit.update'), ('unit.delete'), ('unit.create'),
-- Quyền quản lý loại tài khoản
('account_type.all'), ('account_type.read'), ('account_type.update'), ('account_type.delete'), ('account_type.create'),
-- Quyền quản lý mối quan hệ
('relationship.all'), ('relationship.read'), ('relationship.update'), ('relationship.delete'), ('relationship.create'),
-- Quyền quản lý liên kết tài khoản mạng xã hội
('social_account_link.all'), ('social_account_link.read'), ('social_account_link.update'), ('social_account_link.delete'), ('social_account_link.create'),
-- Quyền quản lý đơn vị nhóm
('unit_group.all'), ('unit_group.read'), ('unit_group.update'), ('unit_group.delete'), ('unit_group.create'),
-- Quyền quản lý đơn vị cá nhân
('individual_unit.all'), ('individual_unit.read'), ('individual_unit.update'), ('individual_unit.delete'), ('individual_unit.create'),
-- Quyền quản lý đơn vị người dùng
('user_unit.all'), ('user_unit.read'), ('user_unit.update'), ('user_unit.delete'), ('user_unit.create'),
-- Quyền quản lý quản trị viên
('administrator.all'), ('administrator.read'), ('administrator.update'), ('administrator.delete'), ('administrator.create'),
-- Quyền quản lý trạng thái nhóm
('group_status.all'), ('group_status.read'), ('group_status.update'), ('group_status.delete'), ('group_status.create'),
-- Quyền quản lý đặc điểm nhóm
('group_characteristic.all'), ('group_characteristic.read'), ('group_characteristic.update'), ('group_characteristic.delete'), ('group_characteristic.create'),
-- Quyền quản lý thẻ cá nhân
('individual_tag.all'), ('individual_tag.read'), ('individual_tag.update'), ('individual_tag.delete'), ('individual_tag.create');

-- Insert sample data for statuses
INSERT INTO "statuses" ("name", "color") VALUES
('Hoạt động', '#00FF00'),
('Riêng tư', '#FF0000'),
('Khóa trang cá nhân', '#FFFF00'),
('Dừng hoạt động', '#00FFFF'),
('Cần theo dõi', '#FF00FF');

-- Insert sample data for characteristics
INSERT INTO "characteristics" ("name", "color") VALUES
('Công giáo', '#FF0000'),
('Tôn giáo khác', '#FFA500'),
('Khiếu kiện', '#00FF00'),
('KOL', '#FFFF00'),
('Xấu độc', '#00FFFF');

-- Insert sample data for tasks
INSERT INTO "tasks" ("name", "description") VALUES
('Theo dõi', 'Theo dõi hoạt động của đối tượng'),
('Điều tra cơ bản', 'Thu thập thông tin về một đối tượng ĐTCB'),
('Quản lý nghiệp vụ', 'Quản lý nghiệp vụ của đối tượng '),
('Kiểm tra nghiệp vụ', 'Kiểm tra nghiệp vụ của đối tượng ĐTCB'),
('Chuyên án', 'Xác lập chuyên án đối tượng');

-- Insert sample data for account_types
INSERT INTO "account_types" ("name") VALUES
('Cá nhân'),
('Nhóm Facebook'),
('Trang Facebook '),
('Fanpage Facebook'),
('Telegram'),
('Zalo');

-- Insert sample data for relationships
INSERT INTO "relationships" ("name") VALUES
('Thành viên'),
('Quản trị viên'),
('Người theo dõi'),
('Bạn bè'),
('Khác');

-- Insert sample data for tags
INSERT INTO "tags" ("name", "color") VALUES
('Quan trọng', '#FF0000'),
('Khẩn cấp', '#FFA500'),
('Cần xem xét', '#FFFF00'),
('Đã xử lý', '#00FF00'),
('Theo dõi', '#00FFFF');

-- Insert sample data for individuals
INSERT INTO "individuals" ("full_name", "national_id", "citizen_id", "date_of_birth", "is_male", "hometown", "phone_number", "is_kol") VALUES
('Nguyễn Văn A', '123456789', '123456789012', '1990-01-01', true, 'Hà Tĩnh', '0123456789', true),
('Trần Thị B', '987654321', '987654321098', '1992-02-02', false, 'Hà Nội', '0987654321', false),
('Lê Văn C', '456789123', '456789123045', '1988-03-03', true, 'TP.HCM', '0456789123', true);

-- Insert sample data for social_accounts
INSERT INTO "social_accounts" ("uid", "name", "reaction_count", "phone_number", "status_id", "type_id", "note", "is_active") VALUES
('100001', 'Nguyễn Văn A', 1000, '0123456789', 1, 1, 'Tài khoản chính', true),
('100002', 'Trần Thị B', 500, '0987654321', 1, 1, 'Tài khoản phụ', true),
('100003', 'Lê Văn C', 2000, '0456789123', 1, 1, 'Tài khoản quan trọng', true);

-- Insert sample data for individual_social_accounts
INSERT INTO "individual_social_accounts" ("individual_id", "social_account_uid", "relationship_id") VALUES
((SELECT id FROM individuals WHERE full_name = 'Nguyễn Văn A'), '100001', 1),
((SELECT id FROM individuals WHERE full_name = 'Trần Thị B'), '100002', 1),
((SELECT id FROM individuals WHERE full_name = 'Lê Văn C'), '100003', 1);

-- Insert sample data for individual_units
INSERT INTO "individual_units" ("unit_id", "individual_id", "task_id") VALUES
((SELECT id FROM units WHERE name = 'PA05'), (SELECT id FROM individuals WHERE full_name = 'Nguyễn Văn A'), 1),
((SELECT id FROM units WHERE name = 'PA05'), (SELECT id FROM individuals WHERE full_name = 'Trần Thị B'), 2),
((SELECT id FROM units WHERE name = 'PA05'), (SELECT id FROM individuals WHERE full_name = 'Lê Văn C'), 3);

-- Insert sample data for unit_groups
INSERT INTO "unit_groups" ("unit_id", "social_account_uid", "task_id") VALUES
((SELECT id FROM units WHERE name = 'PA05'), '100001', 1),
((SELECT id FROM units WHERE name = 'PA05'), '100002', 2),
((SELECT id FROM units WHERE name = 'PA05'), '100003', 3);

-- Insert sample data for role_permissions
INSERT INTO "role_permissions" ("role_id", "permission_id")
SELECT r.id, p.id
FROM roles r
CROSS JOIN permissions p
WHERE r.name = 'superadmin';

-- Insert sample data for user_roles
INSERT INTO "user_roles" ("user_id", "role_id")
SELECT u.id, r.id
FROM users u
CROSS JOIN roles r
WHERE u.username = 'Luongvinhlong' AND r.name = 'superadmin';

-- Insert sample data for user_permissions
INSERT INTO "user_permissions" ("user_id", "permission_id")
SELECT u.id, p.id
FROM users u
CROSS JOIN permissions p
WHERE u.username = 'Luongvinhlong';

-- Insert sample data for user_units
INSERT INTO "user_units" ("user_id", "unit_id")
SELECT u.id, un.id
FROM users u
CROSS JOIN units un
WHERE u.username = 'Luongvinhlong' AND un.name = 'PA05';

-- Insert sample data for users
INSERT INTO "users" ("username", "password", "salt", "is_active") VALUES
('Luongvinhlong', '$2b$12$DX9Vfw30CNbLmc/EbmO3f.DYUVvBOLPgGwFD1dOKtuA6tPgZrG0ca', 'tPOnMZQU', true),
('Nguyendangphi', '$2b$12$9XOKGE9Af7AEWwyn1910DOyTk6/DhkVG3MznKaR.cOanrvY3AQQTW', 'WmmGtMWb', true),
('lephuhung77', '$2b$12$wPHK2GdgI2.coKTi2DEXXeLCpqrQwGbrglltMGvC4nitdlzFG0ta2', 'xOxionLL', true),


-- Insert sample data for user_units
INSERT INTO "user_units" ("user_id", "unit_id")
SELECT u.id, un.id
FROM users u
CROSS JOIN units un
WHERE u.username = 'lephuhung77' AND un.name = 'PA05';

-- Insert sample data for user_roles
INSERT INTO "user_roles" ("user_id", "role_id")
SELECT u.id, r.id
FROM users u
CROSS JOIN roles r
WHERE u.username = 'lephuhung77' AND r.name = 'superadmin';

-- Insert sample data for user_permissions
INSERT INTO "user_permissions" ("user_id", "permission_id")
SELECT u.id, p.id
FROM users u
CROSS JOIN permissions p
WHERE u.username = 'lephuhung77';