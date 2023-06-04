class InvalidPathException(RuntimeError):
    def __init__(self, path):
        super().__init__(f"The given path '{path}' is invalid!\n"+
                         "Please enter a valid one.")