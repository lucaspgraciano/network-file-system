from src.server.utils.file_util import FileUtil
from src.server.commands.exceptions import DirectoryNotFoundException
import os


class ListFilesCommand:
    def __init__(self):
        self.file_util = FileUtil()

    def execute(self, directory_name):
        full_path = self.file_util.get_root_path() + "/" + directory_name
        self.__check_if_directory_exists(full_path)
        directory = os.listdir(full_path)
        return self.__find_files(directory)
    
    def __check_if_directory_exists(self, directory):
        if (not self.file_util.does_directory_exist(directory)):
            raise DirectoryNotFoundException(directory)
    
    def __find_files(self, directory):
        return "Files found: \n" + "\n".join([file for file in directory]) + "\n"
