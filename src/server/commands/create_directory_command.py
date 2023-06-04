import os
from src.server.commands.exceptions import DirectoryAlreadyExistsException
from src.server.utils.file_util import FileUtil

class CreateDirectoryCommand:
    def __init__(self):
        self.file_util = FileUtil()

    def execute(self, directory_name):
        full_path = self.file_util.get_root_path() + "/" + directory_name
        self.__check_if_directory_exists(full_path)
        os.mkdir(full_path)
        return "Directory created successfully!\n"
    
    def __check_if_directory_exists(self, directory_name):
        if (self.file_util.does_directory_exist(directory_name)):
            raise DirectoryAlreadyExistsException(directory_name)
            

