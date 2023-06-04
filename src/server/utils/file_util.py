import os


class FileUtil:
    WORKSPACE_DIRECTORY = "/workspace"

    def does_directory_exist(self, directory_path):
        return os.path.isdir(directory_path)
    
    def get_root_path(self):
        return os.getcwd() + self.WORKSPACE_DIRECTORY
    
    def is_file(self, path):
        return os.path.isfile(path)

    def is_dir(self, path):
        return os.path.isdir(path)