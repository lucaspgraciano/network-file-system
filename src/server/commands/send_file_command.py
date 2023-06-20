from src.server.utils import FileUtil


class SendFileCommand:
    PACKAGE_SIZE = 1024

    def __init__(self):
        self.file_util = FileUtil()

    def execute(self, file_name, client):
        file_path = self.file_util.get_root_path() + "/" + file_name

        with open(file_path, "wb") as file:
            while True:
                package = client.recv(self.PACKAGE_SIZE)
                if len(package) < self.PACKAGE_SIZE:
                    file.write(package)
                    break

                file.write(package)
    
        client.send("File received successfully!\n".encode("utf-8"))