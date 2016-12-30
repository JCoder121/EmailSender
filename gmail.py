import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage



# Import the email modules we'll need
from email.mime.text import MIMEText

# build the email

receive = "abc@gmail.com"
recv2 = "efg@gmail.com"
sender = "sender@gmail.com"
passwd = "password"
recv3 = "onemore@gmail.com"

body_txt = "This is 3rd test. From PY world!"

fp = open("Email Sender.py", 'rb')
body_txt = fp.read()
fp.close()

msg = MIMEMultipart()
msg.attach(MIMEText(body_txt))
msg.attach(MIMEImage(file("image.png").read()))


msg['Subject'] = 'Test Emails'
msg['From'] = sender
msg['To'] = receive



# Now send it

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, passwd)
 
#msg = "This is a second test. From PY world!"
server.sendmail(sender, recv3, msg.as_string())
server.quit()
print "sent"
