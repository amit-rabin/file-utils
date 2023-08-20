from typing import Dict
import os

from src.models.file_handler.abstract import FileHandler


class OSFileHandler(FileHandler):

    def __init__(self,
                 file_type_to_filename_extension_mapping: Dict[str, str],
                 base_route: str,
                 os_file_handling_action_to_encoding_mapping: Dict[str, str],
                 action_to_error_message_mapping: Dict[str, str]) -> None:

        self.file_type_to_filename_extension_mapping = file_type_to_filename_extension_mapping
        self.base_route = base_route
        self.os_file_handling_action_to_encoding_mapping = os_file_handling_action_to_encoding_mapping
        self.action_to_error_message_mapping = action_to_error_message_mapping

    def __build_route_for_file(self, path: str, filename: str, filename_extension: str) -> str:
        return f"{self.base_route}/{path}/{filename}.{filename_extension}"

    def __determine_filename_extension(self, file_type: str) -> str:
        if file_type in self.file_type_to_filename_extension_mapping.keys():
            return self.file_type_to_filename_extension_mapping[file_type]
        else:
            return self.file_type_to_filename_extension_mapping["default"]

    def __get_file_full_route(self, path: str, filename: str, file_type: str) -> str:
        filename_extension = self.__determine_filename_extension(file_type=file_type)
        file_full_route = self.__build_route_for_file(path=path,
                                                      filename=filename,
                                                      filename_extension=filename_extension)
        return file_full_route

    def create_file(self, path: str, filename: str, file_type: str) -> None:
        file_full_route = self.__get_file_full_route(path=path, filename=filename, file_type=file_type)
        file = open(file_full_route, self.os_file_handling_action_to_encoding_mapping["create"])
        file.close()

    def delete_file_content(self, path: str, filename: str, file_type: str) -> None:
        file_full_route = self.__get_file_full_route(path=path, filename=filename, file_type=file_type)
        file = open(file_full_route, self.os_file_handling_action_to_encoding_mapping["delete_content"])
        file.close()

    def create_file_and_write(self, path: str, filename: str, file_type: str, text: str) -> None:
        file_full_route = self.__get_file_full_route(path=path, filename=filename, file_type=file_type)
        file = open(file_full_route, self.os_file_handling_action_to_encoding_mapping["create_and_write"])
        file.write(text)
        file.close()

    def add_to_file(self, path: str, filename: str, file_type: str, text: str) -> None:
        file_full_route = self.__get_file_full_route(path=path, filename=filename, file_type=file_type)
        file = open(file_full_route, self.os_file_handling_action_to_encoding_mapping["append_to_file"])
        file.write(text)
        file.close()

    def delete_file(self, path: str, filename: str, file_type: str) -> None:
        file_full_route = self.__get_file_full_route(path=path, filename=filename, file_type=file_type)
        if os.path.exists(file_full_route):
            os.remove(file_full_route)
        else:
            print(self.action_to_error_message_mapping["delete_file_non_existent"])

    def read_file(self, path: str, filename: str, file_type: str) -> str:
        file_full_route = self.__get_file_full_route(path=path, filename=filename, file_type=file_type)
        file = open(file_full_route, self.os_file_handling_action_to_encoding_mapping["read"])
        content = file.read()
        file.close()
        return content
