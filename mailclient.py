import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("mail@box.com", 25)

server.ehlo()

server.login("mail@box.com","sfsdafsdaf")

msg = MIMEMultipart()
msg["From"] = "NeuralNine"
msg["To"] = "qhlznihxaayvkwwyxr@pp7rvv.com"
msg["Subject"] = "Just A Test"

with open("message.txt", "r") as f:
    message = f.read()

msg.attach(MIMEText(message,"plain"))


filename = "word-image-181.png"
attachment = open(filename, "rb")

p = MIMEBase("application", "octet-stream")
p.set_payload((attachment).read())

encoders.encode_base64(p)
p.add_header("Content-Disposition", f'attachment; filename={filename}')
msg.attach(p)

txt = msg.as_string()
server.sendmail("mail@box.com", "qhlznihxaayvkwwyxr@pp7rvv.com", text)