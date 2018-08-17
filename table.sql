create table onion_urls(
url varchar(100) NOT NULL PRIMARY KEY,
html TEXT,
image longblob
)DEFAULT CHARSET=utf8;


-- +-------+--------------+------+-----+---------+-------+
-- | Field | Type         | Null | Key | Default | Extra |
-- +-------+--------------+------+-----+---------+-------+
-- | url   | varchar(100) | NO   | PRI | NULL    |       |
-- | html  | text         | YES  |     | NULL    |       |
-- | image | longblob     | YES  |     | NULL    |       |
-- +-------+--------------+------+-----+---------+-------+
