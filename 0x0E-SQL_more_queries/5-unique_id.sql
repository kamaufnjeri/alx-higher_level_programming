-- id must be unique and also set default
CREATE TABLE IF NOT EXISTS unique_id
(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
