DROP DATABASE IF EXISTS objects;
CREATE DATABASE objects;

\c objects;

DROP EXTENSION IF EXISTS CITEXT CASCADE;

-- DROP OWNED BY  iot_api_user CASCADE;
-- DROP USER IF EXISTS iot_api_user;
-- CREATE USER iot_api_user WITH PASSWORD 'qwerty';

DROP TABLE IF EXISTS OBJECTS CASCADE;
DROP TABLE IF EXISTS CONTROLLERS CASCADE;
DROP TABLE IF EXISTS SENSOR CASCADE;

CREATE EXTENSION IF NOT EXISTS CITEXT WITH SCHEMA public;


CREATE TABLE IF NOT EXISTS OBJECTS (
  id                SERIAL PRIMARY KEY,
  name              VARCHAR(256)              NOT NULL,
  user_id           INT,
  adres             TEXT
);

CREATE TABLE IF NOT EXISTS CONTROLLERS (
  id                SERIAL PRIMARY KEY,
  name              VARCHAR(256)              NOT NULL UNIQUE,
  object_id         INT REFERENCES OBJECTS (id),
  meta              TEXT                      NOT NULL,
  activation_date   DATE DEFAULT NULL,
  status            INT  DEFAULT NULL,
  mac               MACADDR                   NOT NULL,
  deactivation_date DATE DEFAULT NULL,
  controller_type   INT  DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS SENSOR (
  id                SERIAL PRIMARY KEY,
  name              VARCHAR(256)                    NOT NULL UNIQUE,
  controller_id     INT REFERENCES CONTROLLERS (id) ,
  activation_date   DATE                    DEFAULT NULL,
  status            INT                     DEFAULT NULL,
  deactivation_date DATE                    DEFAULT NULL,
  sensor_type       INT                     DEFAULT NULL,
  company           VARCHAR(256)            DEFAULT NULL
);

INSERT INTO  OBJECTS VALUES (
  default,
  'Имя Объекта',
  1,
  'Улица Пушкина, Дом Колотушкина'
);


INSERT INTO CONTROLLERS VALUES (
  1,
  'test_controller',
  1,
  'Улица Пушкина, Дом Колотушкина',
  '2001-01-01',
  1,
  '6B-45-CD-97-48-48',
  NULL,
  1
);

INSERT INTO CONTROLLERS VALUES (
  2,
  'test_controller2',
  null,
  'Улица Пушкина, Дом Колотушкина2',
  '2001-01-02',
  1,
  '6B-45-CD-97-48-48',
  NULL,
  1
);

INSERT INTO SENSOR VALUES (
  1,
  'test_sensor',
  1,
  '2001-01-01',
  1,
  NULL,
  1,
  'GASPROM'
);

INSERT INTO SENSOR VALUES (
  2,
  'test_sensor2',
  null,
  '2001-01-01',
  1,
  NULL,
  1,
  'GASPROM2'
);
