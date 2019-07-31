DROP DATABASE IF EXISTS objects;
CREATE DATABASE objects;

\c objects;

DROP EXTENSION IF EXISTS CITEXT CASCADE;

DROP OWNED BY object_service CASCADE;
DROP USER IF EXISTS object_service;
CREATE USER object_service WITH PASSWORD 'object_service';

DROP TABLE IF EXISTS OBJECTS CASCADE;
DROP TABLE IF EXISTS CONTROLLERS CASCADE;
DROP TABLE IF EXISTS SENSOR CASCADE;

CREATE EXTENSION IF NOT EXISTS CITEXT WITH SCHEMA public;


CREATE TABLE IF NOT EXISTS OBJECTS (
  id                SERIAL PRIMARY KEY,
  name              VARCHAR(256)              NOT NULL,
  user_id           INT,
  address             TEXT
);

CREATE TABLE IF NOT EXISTS CONTROLLERS (
  id                SERIAL PRIMARY KEY,
  name              VARCHAR(256)            ,
  object_id         INT REFERENCES OBJECTS (id),
  meta              TEXT                      ,
  activation_date   DATE DEFAULT NULL,
  status            INT  DEFAULT NULL,
  mac               MACADDR  NOT NULL UNIQUE,
  deactivation_date DATE DEFAULT NULL,
  controller_type   INT  DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS SENSOR (
  id                SERIAL PRIMARY KEY,
  name              VARCHAR(256)                    NOT NULL,
  controller_id     INT REFERENCES CONTROLLERS (id) ,
  activation_date   DATE                    DEFAULT NULL,
  status            INT                     DEFAULT NULL,
  deactivation_date DATE                    DEFAULT NULL,
  sensor_type       INT                     DEFAULT NULL,
  company           VARCHAR(256)            DEFAULT NULL
);

INSERT INTO  OBJECTS VALUES (
  default,
  'Квартира',
  1,
  'Адрес: г. Москва, ул. Солдатская, д.3, кв. 379'
);

INSERT INTO  OBJECTS VALUES (
  default,
  'Не Квартира',
  1,
  'Не Адрес: г. Москва, ул. Солдатская, д.3, кв. 379'
);


INSERT INTO CONTROLLERS VALUES (
  DEFAULT,
  'Квартира',
  2,
  'Адрес: г. Москва, ул. Солдатская, д.3, кв. 379',
  '2001-01-01',
  1,
  '6B-45-CD-97-48-48',
  NULL,
  1
);

INSERT INTO CONTROLLERS VALUES (
  DEFAULT,
  'test_controller2',
  null,
  'Улица Пушкина, Дом Колотушкина2',
  '2001-01-02',
  1,
  '6B-45-CD-97-48-49',
  NULL,
  1
);

INSERT INTO SENSOR VALUES (
  DEFAULT,
  'Электричество',
  1,
  '2001-01-01',
  1,
  NULL,
  1,
  'Мосэнергосбыт'
);

INSERT INTO SENSOR VALUES (
  DEFAULT,
  'Холодная вода',
  1,
  '2001-01-01',
  1,
  NULL,
  2,
  'Мосводоканал'
);

INSERT INTO SENSOR VALUES (
  DEFAULT,
  'Горячая вода',
  1,
  '2001-01-01',
  1,
  NULL,
  3,
  'Мосводоканал'
);

INSERT INTO SENSOR VALUES (
  DEFAULT,
  'Газ',
  1,
  '2001-01-01',
  1,
  NULL,
  4,
  'Мосгаз'
);

INSERT INTO SENSOR VALUES (
  DEFAULT,
  'TEST_RAW_SENSOR',
  1,
  '2001-01-01',
  1,
  NULL,
  0,
  'Какая-то компания'
);

INSERT INTO SENSOR VALUES (
  DEFAULT,
  'OBD',
  1,
  '2001-01-01',
  1,
  NULL,
  0,
  'Какая-то компания'
);

INSERT INTO SENSOR VALUES (
  DEFAULT,
  'GPS',
  1,
  '2001-01-01',
  1,
  NULL,
  0,
  'Какая-то компания'
);


-- INSERT INTO SENSOR VALUES (
--   1,
--   'test_sensor',
--   1,
--   '2001-01-01',
--   1,
--   NULL,
--   1,
--   'GASPROM'
-- );

-- INSERT INTO SENSOR VALUES (
--   2,
--   'test_sensor2',
--   null,
--   '2001-01-01',
--   1,
--   NULL,
--   1,
--   'GASPROM2'
-- );

-- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO "user";
-- GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO "user";
GRANT ALL PRIVILEGES ON SCHEMA public TO object_service;
GRANT CONNECT ON DATABASE objects TO object_service;
GRANT USAGE ON SCHEMA public TO object_service;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO object_service;
GRANT ALL PRIVILEGES ON TABLE OBJECTS TO object_service;
GRANT ALL PRIVILEGES ON TABLE CONTROLLERS TO object_service;
GRANT ALL PRIVILEGES ON TABLE SENSOR TO object_service;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO object_service;
GRANT ALL PRIVILEGES ON DATABASE objects to object_service;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, UPDATE, INSERT, DELETE, TRIGGER ON TABLES TO object_service;
ALTER DATABASE objects OWNER TO object_service;