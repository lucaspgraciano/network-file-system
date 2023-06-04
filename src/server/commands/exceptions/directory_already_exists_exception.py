class DirectoryAlreadyExistsException(RuntimeError):
    def __init__(self, directory_name):
        super().__init__(f"Directory {directory_name} already exists!\n"+
                         "Please enter a different directory name.")