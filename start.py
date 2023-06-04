from src.server import Server
from src.client import Client

import sys

if __name__ == "__main__":
    try:
        argument = str(sys.argv[1])

        if (argument == "server"):
            server = Server()
            server.run()

        elif (argument == "client"):
            client = Client()
            client.run()
        
        else:
            print("Invalid argument")
    except Exception as error:
        print("Error: ", error)  