from object.models import models
from object import config
import pprint


def main():
    confs = config.ConfigManager()
    confs["database"]["host"] = "localhost"
    confs["database"]["username"] = "object_service"
    confs["database"]["password"] = "object_service"
    md = models.Model(confs["database"])
    pp = pprint.PrettyPrinter(indent=4)
    # res = md.get_user_info(1)
    # pp.pprint(res)
    # res = md.get_object_info(1)
    # pp.pprint(res)
    # res = md.get_controller_info(1)
    # pp.pprint(res)
    # res = md.get_sensor_info(1)
    # pp.pprint(res)
    # res = md.create_object(1, "Name123", "address123", "meta123")
    # pp.pprint(res)
    # res = md.create_controller("name123", 56, "meta123", 0, "4e:1c:78:9c:38:a2")
    # pp.pprint(res)
    # res = md.create_sensor("name123", "meta", 58, 0, "company")
    # pp.pprint(res)
    # res = md.activate_controller(58, "name123activated", "meta123activated", 1, 1)
    # pp.pprint(res)
    # res = md.delete_object(57)
    # pp.pprint(res)
    # res = md.delete_controller(56)
    # pp.pprint(res)
    # res = md.delete_sensor(59)
    # pp.pprint(res)
    res = md.deactivate_controller(58)
    pp.pprint(res)
if __name__ == "__main__":
    main()
