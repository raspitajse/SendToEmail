import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#############################################
 
fromaddr = "your.email@address" # raspitajse@gmail.com"
toaddr = "target.email@address" # mojpismonosa@gmail.com"
password = "moj pass lalala"
messageText = "ovo je automatska poruka poslana skriptom s radionice Istrazivackog Centra Mladih"

#############################################

msg = MIMEMultipart('alternative')
msg['Subject'] = 'Datoteke s RaspitajSe radionice'
msg['From'] = fromaddr

content = MIMEText(messageText, 'plain')
msg.attach(content)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(fromaddr, password)

server.sendmail(fromaddr, [toaddr], msg.as_string())
print ('email sent')

server.quit()
