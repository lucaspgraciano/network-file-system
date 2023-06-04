from src.server.commands import *
import socket

class Server:
    HOST = '127.0.0.1'
    BIN_CODE = "utf-8"
    PACKAGE_SIZE = 1024

    def __init__(self) -> None:
        self.create_directory_command = CreateDirectoryCommand()
        self.remove_item_by_path_command = RemoveItemByPathCommand()
        self.list_files_command = ListFilesCommand()
        self.send_file_command = SendFileCommand()
        
        self.server = None
        self.client = None
        self.__setup()
    
    def run(self):
        self.__welcome()

        while True:
            try:
                __input = self.__get_input()
                
                if ("exit" in __input):
                    self.__exit()
                    break

                elif ("help" in __input):
                    self.__help()

                elif ("mkdir" in __input):
                    message = self.create_directory_command.execute(__input.split(" ")[1])
                    self.__send_client_message(message)

                elif ("rm" in __input):
                    message = self.remove_item_by_path_command.execute(__input.split(" ")[1])
                    self.__send_client_message(message)

                elif ("ls" in __input):
                    message = self.list_files_command.execute(__input.split(" ")[1])
                    self.__send_client_message(message)

                elif ("send" in __input):
                    message = self.send_file_command.execute(__input.split(" ")[1], self.client)
                    
                else:
                    self.__unknown(__input)
            
            except Exception as error:
                self.__error(error)

        self.client.close()
        
    def __setup(self):
        port = int(input("Enter a port: "))
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.HOST, port))
        self.server.listen()

        self.client, address = self.server.accept()

        print("Client connected at: " + str(address))

    def __get_input(self):
        data = self.client.recv(self.PACKAGE_SIZE)
        return data.decode(self.BIN_CODE)
    
    def __send_client_message(self, message):
        self.client.send(message.encode(self.BIN_CODE))
    
    def __welcome(self):
        self.__send_client_message("Welcome to my TCP file system!\n"+ 
              "Type 'help' to see all commands.\n"+
              "To exit application, type 'exit'.\n")

    def __help(self):
        self.__send_client_message("Commands:\n" + 
              "mkdir <directory name> - Create a new directory in the server\n"+
              "rm <directory name> - Remove a directory in the server\n"+
              "ls <directory name> - List all files in given directory\n"+
              "put <file name> - Send a file to the server\n")
        
    def __exit(self):
        self.__send_client_message("Goodbye!")

    def __unknown(self, command):
        self.__send_client_message(f"Unknown command typed for '{command}'\n."+
              "Type 'help' to see all commands.\n")

    def __error(self, message):
        self.__send_client_message("Oops! Something went wrong.\n" + 
              f"ERROR: {message}\n")
