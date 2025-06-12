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
CREATE INDEX IF NOT EXISTS idx_tags_id ON "tags" ("id");

CREATE TABLE "statuses" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "color" varchar(7) CHECK ("color" ~ '^#[0-9A-Fa-f]{6}$'),
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_status_name UNIQUE ("name")
);
CREATE INDEX IF NOT EXISTS idx_statuses_id ON "statuses" ("id");

CREATE TABLE "characteristics" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "color" varchar(7) CHECK ("color" ~ '^#[0-9A-Fa-f]{6}$'),
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_characteristic_name UNIQUE ("name")
);
CREATE INDEX IF NOT EXISTS idx_characteristics_id ON "characteristics" ("id");

CREATE TABLE "tasks" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL, 
  -- "description" text, -- Removed as not in model Task
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_task_name UNIQUE ("name")
);
CREATE INDEX IF NOT EXISTS idx_tasks_id ON "tasks" ("id");

CREATE TABLE "account_types" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_account_type_name UNIQUE ("name") 
);
CREATE INDEX IF NOT EXISTS idx_account_types_id ON "account_types" ("id");

CREATE TABLE "relationships" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(100) NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT unique_relationship_name UNIQUE ("name")
);
CREATE INDEX IF NOT EXISTS idx_relationships_id ON "relationships" ("id");

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
CREATE INDEX IF NOT EXISTS idx_permissions_id ON "permissions" ("id");

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

CREATE TABLE "color" ( -- New table from color.py
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(20) NOT NULL,
    "color" VARCHAR(20) NOT NULL,
    "created_at" TIMESTAMP DEFAULT NOW(),
    "updated_at" TIMESTAMP DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_color_id ON "color" ("id");


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
  CONSTRAINT unique_social_accounts_uid UNIQUE ("uid"), -- Changed from unique_uid
  CONSTRAINT fk_social_accounts_status FOREIGN KEY ("status_id") REFERENCES "statuses" ("id") ON DELETE RESTRICT,
  CONSTRAINT fk_social_accounts_account_type FOREIGN KEY ("type_id") REFERENCES "account_types" ("id") ON DELETE RESTRICT -- Changed from fk_social_accounts_type
);
CREATE INDEX IF NOT EXISTS idx_social_accounts_id ON "social_accounts" ("id");
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
CREATE INDEX IF NOT EXISTS idx_individual_tags_id ON "individual_tags" ("id");
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
CREATE INDEX IF NOT EXISTS idx_individual_social_accounts_id ON "individual_social_accounts" ("id");
CREATE INDEX idx_individual_social_accounts_individual_id ON "individual_social_accounts" ("individual_id");
CREATE INDEX idx_individual_social_accounts_social_account_uid ON "individual_social_accounts" ("social_account_uid");

CREATE TABLE "administrators" (
  "id" SERIAL PRIMARY KEY,
  "uid_administrator" varchar(100) NOT NULL,
  "social_account_uid" varchar(100) NOT NULL, 
  "relationship_id" int NOT NULL,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_administrators_social_account FOREIGN KEY ("social_account_uid") REFERENCES "social_accounts" ("uid") ON DELETE CASCADE,
  CONSTRAINT fk_administrators_relationship FOREIGN KEY ("relationship_id") REFERENCES "relationships" ("id") ON DELETE RESTRICT
);
CREATE INDEX idx_administrators_uid_administrator ON "administrators" ("uid_administrator");

CREATE TABLE "group_statuses" (
  "id" SERIAL PRIMARY KEY,
  "status_id" int, 
  "social_account_uid" varchar(100) NOT NULL, 
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_group_statuses_status FOREIGN KEY ("status_id") REFERENCES "statuses" ("id") ON DELETE RESTRICT,
  CONSTRAINT fk_group_statuses_social_account FOREIGN KEY ("social_account_uid") REFERENCES "social_accounts" ("uid") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_group_statuses_id ON "group_statuses" ("id");
CREATE INDEX idx_group_statuses_social_account_uid ON "group_statuses" ("social_account_uid");

CREATE TABLE "group_characteristics" (
  "id" SERIAL PRIMARY KEY,
  "characteristic_id" int,
  "social_account_uid" varchar(100) NOT NULL, 
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_group_characteristics_characteristic FOREIGN KEY ("characteristic_id") REFERENCES "characteristics" ("id") ON DELETE RESTRICT,
  CONSTRAINT fk_group_characteristics_social_account FOREIGN KEY ("social_account_uid") REFERENCES "social_accounts" ("uid") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_group_characteristics_id ON "group_characteristics" ("id");
CREATE INDEX idx_group_characteristics_social_account_uid ON "group_characteristics" ("social_account_uid");

CREATE TABLE "reports" (
  "id" SERIAL PRIMARY KEY,
  "social_account_uid" varchar(100) NOT NULL, 
  "content_note" text, -- Model String(1000)
  "comment" text, -- Model String(1000)
  "action" text, -- Model String(1000)
  "related_social_account_uid" varchar(100), 
  "user_id" uuid,
  "created_at" timestamp DEFAULT NOW(),
  "updated_at" timestamp DEFAULT NOW(),
  CONSTRAINT fk_reports_user FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE SET NULL
);
CREATE INDEX IF NOT EXISTS idx_reports_id ON "reports" ("id");
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
CREATE INDEX IF NOT EXISTS idx_individual_units_id ON "individual_units" ("id");
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
CREATE INDEX IF NOT EXISTS idx_unit_groups_id ON "unit_groups" ("id");
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
CREATE INDEX IF NOT EXISTS idx_user_permissions_id ON "user_permissions" ("id");
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
CREATE INDEX IF NOT EXISTS idx_user_roles_id ON "user_roles" ("id");
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
CREATE INDEX IF NOT EXISTS idx_role_permissions_id ON "role_permissions" ("id");
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
CREATE INDEX IF NOT EXISTS idx_social_account_links_id ON "social_account_links" ("id");
CREATE INDEX idx_social_account_links_group_social_account_uid ON "social_account_links" ("group_social_account_uid");


CREATE TABLE "model_has_tags" ( 
    "id" SERIAL PRIMARY KEY,
    "model_id" VARCHAR(255), 
    "tags_id" INTEGER NOT NULL,
    "created_at" TIMESTAMP DEFAULT NOW(),
    "updated_at" TIMESTAMP DEFAULT NOW(),
    CONSTRAINT fk_model_has_tags_tag FOREIGN KEY ("tags_id") REFERENCES "tags" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_model_has_tags_id ON "model_has_tags" ("id");


INSERT INTO "units" ("name") VALUES
('PA01'), ('PA02'), ('PA03'), ('PA04'), ('PA05'), ('PA06'), ('PA08'), ('PA09'),
('PC01'), ('PC02'), ('PC03'), ('PC04'), ('PC06'), ('PC07'), ('PC08'), ('PC09'),
('PC10'), ('PC11'), ('PK02'), ('Thành phố Hà Tĩnh'), ('Thị xã Hồng Lĩnh'),
('Thị xã Kỳ Anh'), ('Huyện Nghi Xuân'), ('Huyện Đức Thọ'), ('Huyện Hương Sơn'),
('Huyện Hương Khê'), ('Huyện Vũ Quang'), ('Huyện Can Lộc'), ('Huyện Thạch Hà'),
('Huyện Lộc Hà'), ('Huyện Cẩm Xuyên'), ('Huyện Kỳ Anh'), ('Đơn vị khác');


INSERT INTO "roles" ("name") VALUES
('superadmin'), ('admin'), ('phong'), ('cax'), ('doi');


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

INSERT INTO "statuses" ("name", "color") VALUES
('Hoạt động', '#00FF00'),
('Riêng tư', '#FF0000'),
('Khóa trang cá nhân', '#FFFF00'),
('Dừng hoạt động', '#00FFFF'),
('Cần theo dõi', '#FF00FF');


INSERT INTO "characteristics" ("name", "color") VALUES
('Công giáo', '#FF0000'),
('Tôn giáo khác', '#FFA500'),
('Khiếu kiện', '#00FF00'),
('is_kol', '#FFFF00'),
('Xấu độc', '#00FFFF');


INSERT INTO "tasks" ("name") VALUES -- Removed description
('Theo dõi'),
('Vai ảo'),
('Điều tra cơ bản'),
('Quản lý nghiệp vụ'),
('Kiểm tra nghiệp vụ'),
('Chuyên án');


INSERT INTO "account_types" ("name") VALUES
('Facebook cá nhân'), -- Corrected typo Fcebook
('Nhóm Facebook'),
('Trang Facebook '),
('Vai ảo'),
('Telegram'),
('Zalo');


INSERT INTO "relationships" ("name") VALUES
('Thành viên'),
('Quản trị viên'),
('Người theo dõi'),
('Bạn bè'),
('Khác');


INSERT INTO "tags" ("name", "color") VALUES
('Quan trọng', '#FF0000'),
('Khẩn cấp', '#FFA500'),
('Cần xem xét', '#FFFF00'),
('Đã xử lý', '#00FF00'),
('Theo dõi', '#00FFFF');


INSERT INTO "individuals" ("full_name", "national_id", "date_of_birth", "is_male", "hometown", "phone_number", "is_kol") VALUES -- Changed id_card to national_id, removed kols_type
('Nguyễn Văn A', '123456789012', '1990-01-01', true, 'Hà Tĩnh', '0123456789', true),
('Trần Thị B', '987654321098', '1992-02-02', false, 'Hà Nội', '0987654321', false),
('Lê Văn C', '456789123045', '1988-03-03', true, 'TP.HCM', '0456789123', true);


INSERT INTO "social_accounts" ("uid", "name", "reaction_count", "phone_number", "status_id", "type_id", "note", "is_active") VALUES -- Changed to type_id and is_active
('100001', 'Nguyễn Văn A', 1000, '0123456789', 1, 1, 'Tài khoản chính', true),
('100002', 'Trần Thị B', 500, '0987654321', 2, 1, 'Tài khoản phụ', true),
('100003', 'Lê Văn C', 2000, '0456789123', 3, 1, 'Tài khoản quan trọng', true);


INSERT INTO "individual_social_accounts" ("individual_id", "social_account_uid", "relationship_id") VALUES
((SELECT id FROM individuals WHERE full_name = 'Nguyễn Văn A'), '100001', 1),
((SELECT id FROM individuals WHERE full_name = 'Trần Thị B'), '100002', 1),
((SELECT id FROM individuals WHERE full_name = 'Lê Văn C'), '100003', 1);


INSERT INTO "individual_units" ("unit_id", "individual_id", "task_id") VALUES
((SELECT id FROM units WHERE name = 'PA05'), (SELECT id FROM individuals WHERE full_name = 'Nguyễn Văn A'), 1),
((SELECT id FROM units WHERE name = 'PA05'), (SELECT id FROM individuals WHERE full_name = 'Trần Thị B'), 2),
((SELECT id FROM units WHERE name = 'PA05'), (SELECT id FROM individuals WHERE full_name = 'Lê Văn C'), 3);


INSERT INTO "unit_groups" ("unit_id", "social_account_uid", "task_id") VALUES
((SELECT id FROM units WHERE name = 'PA05'), '100001', 1),
((SELECT id FROM units WHERE name = 'PA05'), '100002', 2),
((SELECT id FROM units WHERE name = 'PA05'), '100003', 3);


INSERT INTO "users" ("username", "password", "salt", "is_active") VALUES
('Luongvinhlong', '$2b$12$DX9Vfw30CNbLmc/EbmO3f.DYUVvBOLPgGwFD1dOKtuA6tPgZrG0ca', 'tPOnMZQU', true),
('Nguyendangphi', '$2b$12$9XOKGE9Af7AEWwyn1910DOyTk6/DhkVG3MznKaR.cOanrvY3AQQTW', 'WmmGtMWb', true),
('lephuhung77', '$2b$12$H4uylt0IhI5vGYx4nFt.4uTTTxcO1.QEDJOkN9pHW9qK6uFX2.53u', 'K4cfyXcw', true);



INSERT INTO "role_permissions" ("role_id", "permission_id")
SELECT r.id, p.id
FROM roles r
CROSS JOIN permissions p
WHERE r.name = 'superadmin';


INSERT INTO "user_roles" ("user_id", "role_id")
SELECT u.id, r.id
FROM users u
CROSS JOIN roles r
WHERE u.username = 'Luongvinhlong' AND r.name = 'superadmin';


INSERT INTO "user_roles" ("user_id", "role_id")
SELECT u.id, r.id
FROM users u
CROSS JOIN roles r
WHERE u.username IN ('lephuhung77', 'Nguyendangphi') 
AND r.name = 'superadmin'
AND NOT EXISTS ( 
    SELECT 1 FROM user_roles ur_inner
    WHERE ur_inner.user_id = u.id AND ur_inner.role_id = r.id
);



INSERT INTO "user_permissions" ("user_id", "permission_id")
SELECT u.id, p.id
FROM users u
CROSS JOIN permissions p
WHERE u.username = 'Luongvinhlong';


INSERT INTO "user_permissions" ("user_id", "permission_id")
SELECT u.id, p.id
FROM users u
CROSS JOIN permissions p
WHERE u.username IN ('lephuhung77', 'Nguyendangphi') 
AND NOT EXISTS ( 
    SELECT 1 FROM user_permissions up_inner
    WHERE up_inner.user_id = u.id AND up_inner.permission_id = p.id
);


INSERT INTO "user_units" ("user_id", "unit_id")
SELECT u.id, un.id
FROM users u
CROSS JOIN units un
WHERE u.username IN ('lephuhung77', 'Nguyendangphi', 'Luongvinhlong')
AND un.name = 'PA05';

-- =============================================
-- BỔ SUNG DỮ LIỆU DEMO CHO TÌM KIẾM
-- =============================================

INSERT INTO "individuals" ("full_name", "national_id", "date_of_birth", "is_male", "hometown", "additional_info", "phone_number", "is_kol") VALUES -- Changed id_number to national_id
('Phạm Thị D', '038195001122', '1995-05-15', false, 'Nghệ An', 'Có nhiều bài viết tiêu cực về chính sách đền bù đất đai', '0912345678', false),
('Hoàng Văn E', '040080002233', '1980-11-20', true, 'Hà Tĩnh', 'Là admin của nhóm "Yêu Hà Tĩnh", thường xuyên đăng tin tức địa phương', '0988112233', false),
('Đặng Thuỳ F', '027199003344', '1999-07-01', false, 'Đà Nẵng', 'Beauty blogger, influencer mảng mỹ phẩm, đôi khi có phát ngôn gây tranh cãi', '0333444555', true),
('Vũ Tiến G', '001075004455', '1975-03-10', true, 'Hà Nội', 'Nghiên cứu về lịch sử, có các bài phân tích sâu sắc', '0777888999', false),
('Bùi Minh H', '051092005566', '1992-09-25', true, 'Hải Phòng', 'Thành viên tích cực trong các diễn đàn ô tô', '0888999000', false);


INSERT INTO "social_accounts" ("uid", "name", "reaction_count", "phone_number", "status_id", "type_id", "note", "is_active") VALUES -- Changed type_id to type_id and is_linked to is_active
('10000123456789', 'Pham Thi D', 150, '0912345678', 1, 1, 'TK chính của Phạm Thị D', true),
('10001548796548', 'Group Yêu Hà Tĩnh', 5000, '0988112233', 2, 2, 'Nhóm cộng đồng lớn', true), -- type_id=2: Nhóm Facebook
('tiktok_dangthuyf', 'Dang Thuy F Official', 150000, '0333444555', 1, 1, 'KOL TikTok', true), -- Giả sử type 1 cũng dùng cho TikTok
('zalo_vutieng', 'Vũ Tiến (NCLS)', 50, '0777888999', 3, 6, 'Zalo cá nhân', true), -- type_id=6: Zalo
('10002366484847', 'Bui Minh H', 250, '0888999000', 4, 1, 'Hay đăng về xe cộ', true);


INSERT INTO "individual_social_accounts" ("individual_id", "social_account_uid", "relationship_id") VALUES
((SELECT id FROM individuals WHERE full_name = 'Phạm Thị D'), '10000123456789', 1),
((SELECT id FROM individuals WHERE full_name = 'Hoàng Văn E'), '10001548796548', 2),
((SELECT id FROM individuals WHERE full_name = 'Đặng Thuỳ F'), 'tiktok_dangthuyf', 1),
((SELECT id FROM individuals WHERE full_name = 'Vũ Tiến G'), 'zalo_vutieng', 1),
((SELECT id FROM individuals WHERE full_name = 'Bùi Minh H'), '10002366484847', 1);

INSERT INTO "reports" ("social_account_uid", "content_note", "comment", "action", "related_social_account_uid", "user_id") VALUES
('10000123456789', 'Đối tượng đăng bài về đền bù X', 'Bài viết có nhiều bình luận trái chiều, cần theo dõi thêm', 'Giao PA06 theo dõi', NULL, (SELECT id FROM users WHERE username = 'Luongvinhlong')),
('10001548796548', 'Nhóm đăng tin sai sự thật về dự án Y', 'Admin đã gỡ bài nhưng thông tin đã lan truyền', 'Yêu cầu admin đính chính', NULL, (SELECT id FROM users WHERE username = 'Nguyendangphi')),
('tiktok_dangthuyf', 'KOL này quảng cáo sản phẩm không rõ nguồn gốc', 'Video có lượng tương tác cao', 'Đề xuất làm việc, nhắc nhở', NULL, (SELECT id FROM users WHERE username = 'lephuhung77')),
('10002366484847', 'Tài khoản này tương tác với tài khoản 10000123456789', 'Có bình luận ủng hộ quan điểm của Phạm Thị D', 'Bổ sung thông tin vào hồ sơ', '10000123456789', (SELECT id FROM users WHERE username = 'Luongvinhlong')),
('100001', 'Tài khoản Nguyễn Văn A có hoạt động mới đáng chú ý', 'Tham gia nhóm chống đối mới thành lập', 'Cập nhật vào hồ sơ ĐTCB', NULL, (SELECT id FROM users WHERE username = 'Nguyendangphi'));

-- Thêm vài liên kết tài khoản (ví dụ)
INSERT INTO "social_account_links" ("group_social_account_uid", "linked_social_account_uid") VALUES
('10001548796548', '10000123456789'),
('10001548796548', '100001');