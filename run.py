from src.config.config_loader import config
from src.models.file_handler.os_file_handler.os_file_handler import OSFileHandler

os_file_handler = OSFileHandler(
    file_type_to_filename_extension_mapping=config["file_type_to_filename_extension_mapping"],
    base_route=config["base_route"],
    os_file_handling_action_to_encoding_mapping=config["os_file_handling_action_to_encoding_mapping"],
    action_to_error_message_mapping=config["action_to_error_message_mapping"])

os_file_handler.create_file_and_write(path="tests", filename="test1", file_type="text", text="amitos is the best")
