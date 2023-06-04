import shutil
import os
from src.server.commands.exceptions import InvalidPathException
from src.server.utils.file_util import FileUtil

class RemoveItemByPathCommand:
    def __init__(self):
        self.file_util = FileUtil()

    def execute(self, directory_name):
        full_path = self.file_util.get_root_path() + "/" + directory_name

        if self.file_util.is_file(full_path):
            os.remove(full_path)
            return "File removed successfully!\n"

        elif self.file_util.is_dir(full_path):
            shutil.rmtree(full_path)
            return "Directory removed successfully!\n"

        else:
            raise InvalidPathException(full_path)
