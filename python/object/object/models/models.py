import psycopg2
import psycopg2.extras
import logging
from collections import defaultdict

# TODO: Рефакторинг и декомпозиция часть два
# оптимизировать все запросы и декомпозировать


class Model:
    def __init__(self, dbconf):
        logging.info("Connecting to {} with username: {}, host: {}".format(dbconf["database"],
                                                                           dbconf["username"],
                                                                           dbconf["host"]))
        self.driver = psycopg2.connect(dbname=dbconf["database"],
                                       user=dbconf["username"],
                                       password=dbconf["password"],
                                       host=dbconf["host"])

    def __extract_fields(self, row, prefix):
        result = {}
        prefix += "."
        for key, value in row.items():
            if key.startswith(prefix):
                result[key[len(prefix):]] = value
        return result

    def _extract_sensors(self, row, result):
        sensor_id = row["sensor.id"]
        if sensor_id is None:
            return
        if sensor_id in result:
            return
        result[sensor_id] = self.__extract_fields(row, "sensor")

    def _extract_controllers(self, row, result):
        controller_id = row["controllers.id"]
        if controller_id is None:
            return
        if controller_id not in result:
            result[controller_id] = self.__extract_fields(row, "controllers")
        # TODO переписать на нормальный defaultdict
            result[controller_id]["sensors"] = {}
        self._extract_sensors(row, result[controller_id]["sensors"])

    def _extract_objects(self, row, result):
        object_id = row["objects.id"]
        if object_id is None:
            return
        if object_id not in result:
            result[object_id] = self.__extract_fields(row, "objects")
        # TODO переписать на нормальный defaultdict
            result[object_id]["controllers"] = {}
        self._extract_controllers(row, result[object_id]["controllers"])

    def _extract_user_info(self, row, result):
        user_id = row["objects.user_id"]
        if user_id not in result:
            result[user_id] = {}
            # TODO переписать на нормальный defaultdict
            result[user_id]["objects"] = {}
            result[user_id]["id"] = user_id
        self._extract_objects(row, result[user_id]["objects"])

    def get_user_info(self, user_id):
        query = """
        SELECT
            objects.id as "objects.id"
            , objects.name as "objects.name"
            , objects.user_id as "objects.user_id"
            , objects.address as "objects.address"
            , objects.meta as "objects.meta"
            , controllers.id as "controllers.id"
            , controllers.name as "controllers.name"
            , controllers.meta as "controllers.meta"
            , controllers.activation_date as "controllers.activation_date"
            , controllers.status as "controllers.status"
            , controllers.mac as "controllers.mac"
            , controllers.deactivation_date as "controllers.deactivation_date"
            , controllers.controller_type as "controllers.controller_type"
            , controllers.meta as "controllers.meta"
            , controllers.object_id as "controllers.object_id"
            , sensor.id as "sensor.id"
            , sensor.name as "sensor.name"
            , sensor.activation_date as "sensor.activation_date"
            , sensor.status as "sensor.status"
            , sensor.deactivation_date as "sensor.deactivation_date"
            , sensor.sensor_type as "sensor.sensor_type"
            , sensor.company as "sensor.company"
            , sensor.meta as "sensor.meta"
            , sensor.controller_id as "sensor.controller_id"

        FROM objects
            LEFT JOIN controllers
            ON controllers.object_id = objects.id

            LEFT JOIN sensor
            ON sensor.controller_id = controllers.id

        WHERE user_id = %s ;"""
        cur = self.driver.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(query, (user_id,))
        rows = cur.fetchall()
        users = {}
        for row in rows:
            self._extract_user_info(row, users)
        result = {"users": users}
        return result

    def get_controller_info(self, controller_id):
        query = """
        SELECT
            controllers.id as "controllers.id"
            , controllers.name as "controllers.name"
            , controllers.meta as "controllers.meta"
            , controllers.activation_date as "controllers.activation_date"
            , controllers.status as "controllers.status"
            , controllers.mac as "controllers.mac"
            , controllers.deactivation_date as "controllers.deactivation_date"
            , controllers.controller_type as "controllers.controller_type"
            , controllers.meta as "controllers.meta"
            , controllers.object_id as "controllers.object_id"
            , sensor.id as "sensor.id"
            , sensor.name as "sensor.name"
            , sensor.activation_date as "sensor.activation_date"
            , sensor.status as "sensor.status"
            , sensor.deactivation_date as "sensor.deactivation_date"
            , sensor.sensor_type as "sensor.sensor_type"
            , sensor.company as "sensor.company"
            , sensor.meta as "sensor.meta"
            , sensor.controller_id as "sensor.controller_id"

        FROM controllers
            LEFT JOIN sensor
            ON sensor.controller_id = controllers.id

        WHERE controllers.id = %s ;"""
        cur = self.driver.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(query, (controller_id,))
        rows = cur.fetchall()
        controllers = {}
        for row in rows:
            self._extract_controllers(row, controllers)
        result = {"controllers": controllers}
        return result

    def get_object_info(self, object_id):
        query = """
        SELECT
            objects.id as "objects.id"
            , objects.name as "objects.name"
            , objects.user_id as "objects.user_id"
            , objects.address as "objects.address"
            , objects.meta as "objects.meta"
            , controllers.id as "controllers.id"
            , controllers.name as "controllers.name"
            , controllers.meta as "controllers.meta"
            , controllers.activation_date as "controllers.activation_date"
            , controllers.status as "controllers.status"
            , controllers.mac as "controllers.mac"
            , controllers.deactivation_date as "controllers.deactivation_date"
            , controllers.controller_type as "controllers.controller_type"
            , controllers.object_id as "controllers.object_id"
            , sensor.id as "sensor.id"
            , sensor.name as "sensor.name"
            , sensor.activation_date as "sensor.activation_date"
            , sensor.status as "sensor.status"
            , sensor.deactivation_date as "sensor.deactivation_date"
            , sensor.sensor_type as "sensor.sensor_type"
            , sensor.company as "sensor.company"
            , sensor.meta as "sensor.meta"
            , sensor.controller_id as "sensor.controller_id"

        FROM objects
            LEFT JOIN controllers
            ON controllers.object_id = objects.id

            LEFT JOIN sensor
            ON sensor.controller_id = controllers.id

        WHERE objects.id = %s ;"""
        cur = self.driver.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(query, (object_id,))
        rows = cur.fetchall()
        objects = {}
        for row in rows:
            self._extract_objects(row, objects)
        result = {"objects": objects}
        return result

    def get_sensor_info(self, controller_id):
        query = """
        SELECT
            sensor.id as "sensor.id"
            , sensor.name as "sensor.name"
            , sensor.activation_date as "sensor.activation_date"
            , sensor.status as "sensor.status"
            , sensor.deactivation_date as "sensor.deactivation_date"
            , sensor.sensor_type as "sensor.sensor_type"
            , sensor.company as "sensor.company"
            , sensor.meta as "sensor.meta"
            , sensor.controller_id as "sensor.controller_id"

        FROM sensor
        WHERE sensor.id = %s ;"""
        cur = self.driver.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(query, (controller_id,))
        rows = cur.fetchall()
        sensors = {}
        for row in rows:
            self._extract_sensors(row, sensors)
        result = {"sensors": sensors}
        return result

    def create_object(self, uid, name, address, meta):
        try:
            with self.driver.cursor() as cur:
                qry = """
                    INSERT INTO OBJECTS (name, address, user_id, meta)
                    VALUES (%(name)s, %(address)s, %(user_id)s, %(meta)s)
                    RETURNING id;"""
                args = {
                    "name": name,
                    "user_id": uid,
                    "address": address,
                    "meta": meta,
                }
                cur.execute(qry, args)
                rows = cur.fetchall()
                object_id = rows[0][0]
                self.driver.commit()
                logging.info("Executed query")
        except Exception as e:
            logging.error("Failed query {}".format(str(e)))
            self.driver.rollback()
            raise e
        return self.get_object_info(object_id)

    def create_controller(self, name, object_id, meta, controller_type, mac):
        try:
            with self.driver.cursor() as cur:
                qry = """
                    INSERT INTO CONTROLLERS (name, object_id, meta, controller_type, mac)
                    VALUES (%(name)s, %(object_id)s, %(meta)s, %(controller_type)s, %(mac)s)
                    RETURNING id;
                """
                args = {
                    "name": name,
                    "object_id": object_id,
                    "meta": meta,
                    "controller_type": controller_type,
                    "mac": mac
                }
                cur.execute(qry, args)
                rows = cur.fetchall()
                controller_id = rows[0][0]
                self.driver.commit()
                logging.info("Executed query")
        except Exception as e:
            logging.error("Failed query {}".format(str(e)))
            self.driver.rollback()
            raise e
        return self.get_controller_info(controller_id)

    def create_sensor(self, name, meta, controller_id, sensor_type, company):
        try:
            with self.driver.cursor() as cur:
                qry = """
                    INSERT INTO sensor (name, meta, controller_id, sensor_type, company)
                    VALUES (%(name)s, %(meta)s, %(controller_id)s, %(sensor_type)s, %(company)s)
                    RETURNING id;
                """
                args = {
                    "name": name,
                    "meta": meta,
                    "controller_id": controller_id,
                    "sensor_type": sensor_type,
                    "company": company
                }
                cur.execute(qry, args)
                rows = cur.fetchall()
                sensor_id = rows[0][0]
                self.driver.commit()
            logging.info("Executed query")
        except Exception as e:
            logging.error("Failed query {}".format(str(e)))
            self.driver.rollback()
            raise e
        return self.get_sensor_info(sensor_id)

    def activate_controller(self, controller_id, name, meta, object_id, status):
        try:
            with self.driver.cursor() as cur:
                qry = """
                    UPDATE controllers
                        SET name = %(name)s,
                            meta = %(meta)s,
                            object_id = %(object_id)s,
                            status = %(status)s,
                            activation_date = now()
                    where id = %(id)s;
                """
                args = {
                    "name": name,
                    "meta": meta,
                    "object_id": object_id,
                    "status": status,
                    "id": controller_id,
                }
                cur.execute(qry, args)
                self.driver.commit()
                logging.info("Executed query")
        except Exception as e:
            logging.error("Failed query {}".format(str(e)))
            self.driver.rollback()
            raise e
        return self.get_controller_info(controller_id)

    def delete_object(self, object_id):
        try:
            with self.driver.cursor() as cur:
                cur.execute("""
                    DELETE FROM OBJECTS
                    where id = %s;
                """, (object_id,))
                deleted = cur.rowcount
                self.driver.commit()
                logging.info("Executed query")
        except Exception as e:
            logging.error("Failed query {}".format(str(e)))
            self.driver.rollback()
            raise e
        return deleted

    def delete_sensor(self, sensor_id):
        try:
            with self.driver.cursor() as cur:
                cur.execute("""
                    DELETE FROM SENSOR
                    where id = %s;
                """, (sensor_id,))
                deleted = cur.rowcount
                self.driver.commit()
                logging.info("Executed query")
        except Exception as e:
            logging.error("Failed query {}".format(str(e)))
            self.driver.rollback()
            raise e
        return deleted

    def delete_controller(self, controller_id):
        try:
            with self.driver.cursor() as cur:
                cur.execute("""
                    DELETE FROM controllers
                    where id = %s;
                """, (controller_id,))
                deleted = cur.rowcount
                self.driver.commit()
                logging.info("Executed query")
        except Exception as e:
            logging.error("Failed query {}".format(str(e)))
            self.driver.rollback()
            raise e
        return deleted

    def deactivate_controller(self, controller_id):
        try:
            with self.driver.cursor() as cur:
                cur.execute("""
                    UPDATE controllers
                        SET name = NULL,
                            meta = NULL,
                            object_id = NULL,
                            deactivation_date = now(),
                            status = 0
                    where id = %s;
                """, (controller_id,))
                self.driver.commit()
                logging.info("Executed query")
        except Exception as e:
            logging.error("Failed query {}".format(str(e)))
            self.driver.rollback()
            raise e
        return self.get_controller_info(controller_id)
