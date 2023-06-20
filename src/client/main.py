import socket

class Client:
    BIN_CODE = "utf-8"
    PACKAGE_SIZE = 1024
    
    def __init__(self) -> None:
        self.client = None
        self.host = None
        self.port = None
        self.__setup()
    
    def __setup(self):
        self.__get_host_and_port()
        self.__connect()
        
    def __get_host_and_port(self):
        self.host = input("Enter a host: ")
        self.port = int(input("Enter a port: "))

    def __connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def run(self):
        print(self.client.recv(self.PACKAGE_SIZE).decode(self.BIN_CODE))

        while True:
            message = input()

            if ("put" in message):
                file_path = input("Enter a file path: ")

                self.client.send(message.encode(self.BIN_CODE))

                with open(file_path, "rb") as file:
                    bytes = 0
                    while True:
                        bytes += self.PACKAGE_SIZE
                        package = file.read(bytes)

                        if not package:
                            break
                            
                        self.client.sendall(package)
                
                # self.client.send("EOF".encode(self.BIN_CODE))
            else:
                self.client.send(message.encode(self.BIN_CODE))
            
            response = self.client.recv(self.PACKAGE_SIZE).decode(self.BIN_CODE)
            print(response)
            
            if (response == "Goodbye!"):
                break
            
        self.client.close()
