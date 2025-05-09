-- =============================================
-- BỔ SUNG DỮ LIỆU DEMO CHO TÌM KIẾM
-- =============================================

INSERT INTO "individuals" ("full_name", "id_number", "date_of_birth", "is_male", "hometown", "additional_info", "phone_number", "is_kol") VALUES
('Phạm Thị D', '038195001122', '1995-05-15', false, 'Nghệ An', 'Có nhiều bài viết tiêu cực về chính sách đền bù đất đai', '0912345678', false),
('Hoàng Văn E', '040080002233', '1980-11-20', true, 'Hà Tĩnh', 'Là admin của nhóm "Yêu Hà Tĩnh", thường xuyên đăng tin tức địa phương', '0988112233', false),
('Đặng Thuỳ F', '027199003344', '1999-07-01', false, 'Đà Nẵng', 'Beauty blogger, influencer mảng mỹ phẩm, đôi khi có phát ngôn gây tranh cãi', '0333444555', true),
('Vũ Tiến G', '001075004455', '1975-03-10', true, 'Hà Nội', 'Nghiên cứu về lịch sử, có các bài phân tích sâu sắc', '0777888999', false),
('Bùi Minh H', '051092005566', '1992-09-25', true, 'Hải Phòng', 'Thành viên tích cực trong các diễn đàn ô tô', '0888999000', false);


INSERT INTO "social_accounts" ("uid", "name", "reaction_count", "phone_number", "status_id", "account_type_id", "note", "is_linked") VALUES
('10000123456789', 'Pham Thi D', 150, '0912345678', 1, 1, 'TK chính của Phạm Thị D', true),
('10001548796548', 'Group Yêu Hà Tĩnh', 5000, '0988112233', 1, 2, 'Nhóm cộng đồng lớn', true), -- account_type_id=2: Nhóm Facebook
('tiktok_dangthuyf', 'Dang Thuy F Official', 150000, '0333444555', 1, 1, 'KOL TikTok', true), -- Giả sử type 1 cũng dùng cho TikTok
('zalo_vutieng', 'Vũ Tiến (NCLS)', 50, '0777888999', 1, 6, 'Zalo cá nhân', true), -- account_type_id=6: Zalo
('10002366484847', 'Bui Minh H', 250, '0888999000', 1, 1, 'Hay đăng về xe cộ', true);


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