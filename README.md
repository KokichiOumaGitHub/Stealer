# Stealer
App can steals other file from USB drive


# Config

- fromaddr = your email
- password = your password
- toaddr = email who will receive files

- file_ext = extensions of files [list]
- list_drive = default name of drives [tuple] exp: ('C', 'D', )


# Build
To build this app first you should install pyinstaller

--- pip install pyinstaller

Second you should run this command:

--- pyinstaller -w -F -i path/to/icon application.py
