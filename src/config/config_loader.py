import yaml

config = None
route_to_config = "C:/dev/active/file_utils/src/config/config.yml"

with open(route_to_config, "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
