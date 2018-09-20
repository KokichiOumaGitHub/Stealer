import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from transliterate import slugify


def send_mail(fromaddr, toaddr, password, files):
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "FILES"

    body = "time {}".format(datetime.now())

    msg.attach(MIMEText(body, 'plain'))

    print(files)
    for file in files:
        attachment = open(file, "rb")
        print(file)

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
