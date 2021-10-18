CREATE ROLE my_user WITH LOGIN PASSWORD 'Jt567Y2';

CREATE SCHEMA IF NOT EXISTS test_schema AUTHORIZATION my_user;
GRANT USAGE ON SCHEMA test_schema TO my_user;


CREATE TABLE IF NOT EXISTS test_schema.users
(
    id       SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL
);

INSERT INTO test_schema.users(username)
VALUES ('username1'),
       ('username3'),
       ('username3');

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA test_schema TO my_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA test_schema TO my_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA test_schema TO my_user;