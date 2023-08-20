from typing import Dict

from src.models.file_handler.abstract import FileHandler

class OSFileHandler(FileHandler):

    def __init__(self,
                 file_type_to_filename_extension_mapping: Dict[str, str],
                 base_route: str,
                 os_file_handling_action_to_encoding_mapping: Dict[str, str]) -> None:
        self.file_type_to_filename_extension_mapping = file_type_to_filename_extension_mapping
        self.base_route = base_route
        self.os_file_handling_action_to_encoding_mapping = os_file_handling_action_to_encoding_mapping

    def __build_route_for_file(self, path: str, filename: str, filename_extension: str):
        return f"{self.base_route}\\{path}\\{filename}.{filename_extension}"

    def __determine_filename_extension(self, file_type: str):
        if file_type in self.file_type_to_filename_extension_mapping.keys():
            return self.file_type_to_filename_extension_mapping[file_type]
        else:
            return self.file_type_to_filename_extension_mapping["default"]

    def __get_file_full_route(self, path: str, filename: str, file_type: str):
        filename_extension = self.__determine_filename_extension(file_type=file_type)
        file_full_route = self.__build_route_for_file(path=path,
                                                      filename=filename,
                                                      filename_extension=filename_extension)
        return file_full_route

    def create_file(self, path: str, filename: str, file_type: str):
        file_full_route = self.__get_file_full_route(path=path, filename=filename, file_type=file_type)
        open(file_full_route, self.os_file_handling_action_to_encoding_mapping["create"])


