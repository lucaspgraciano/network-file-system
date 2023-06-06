# TCP File System

## Description

A simple file system that uses TCP sockets to communicate with a server.

## Usage

### Server

```bash
python3 start.py server
```

```bash
Enter IP:
Enter Port:
```

### Client

```bash 
python3 start.py client
```

```bash
Enter IP:
Enter Port:
```
<hr>

## Commands

### Help
List all commands
```bash
help
```
### List directories
List files and directories in the given path
```bash
ls <path>
```

### Create directory
Create a new directory in the server workspace
```bash
mkdir <name>
```

### Send file
Send a file to the server workspace
```bash
put <file>
Enter a file path: <file path>
```

### Remove file or directory
Remove a file or directory in the server workspace
```bash
rm <path>
```

### Exit
Exit the program
```bash
exit
```