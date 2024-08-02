CREATE TABLE datadoc (
	article_id  text  PRIMARY KEY,
	topic text,
	href text,
	publish_date date,
	newspaper text,
	created_date date,
	language text,
	sapo text,
	content text,
	feature_image text DEFAULT 'https://photo2.tinhte.vn/data/attachment-files/2023/04/6407049_236601_Social_media_is_doomed_to_die_HHerrera.png'
);
CREATE TABLE post (
  uid text PRIMARY KEY,
  message text,
  from_uid text,
  created_time timestamp,
  updated_time timestamp NULL,
  shares integer,
  reaction integer,
  id_uid text,
  created_at timestamp,
  updated_at timestamp
);
CREATE TABLE uid (
  uid text PRIMARY KEY,
  name text,
  image text NULL ,
  reaction integer,
  type_id integer,
  created_at timestamp,
  updated_at timestamp
);
CREATE TABLE comment (
  uid text PRIMARY KEY,
  message text,
  from_uid text,
  created_time timestamp,
  shares integer,
  reaction integer,
  uid_post text,
  created_at timestamp,
  updated_at timestamp
);
-- nhớ không viết in hoa--