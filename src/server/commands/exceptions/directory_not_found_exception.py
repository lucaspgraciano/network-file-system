class DirectoryNotFoundException(RuntimeError):
    def __init__(self, directory_name):
        super().__init__(f"Directory {directory_name} not found!\n"+
                         "Please enter a valid one.")