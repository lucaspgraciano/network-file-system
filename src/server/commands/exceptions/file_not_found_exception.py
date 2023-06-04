class FileNotFoundException(RuntimeError):
    def __init__(self, file_name):
        super().__init__(f"File {file_name} not found!\n"+
                         "Please enter a valid one.")