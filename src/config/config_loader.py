import yaml

config = None

with open("C:/dev/active/file_utils/src/config/config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
