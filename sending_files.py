# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 06:36:10 2017

@author: user
"""

import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
 
# fill in the variables
smtp_server = "smtp.gmail.com"
smtp_port = 587                                 
from_address = input('your email address: ')            
from_password = input('your password: ')  
to_address = input("other person's email address: ")  
folder_name = input('the folder name: ')  
subject = 'Your files'              
files = os.listdir('C:\\Users\\user\\Desktop\\{}'.format(folder_name)) 
file_list = []
for f in files:
    f = 'C:\\Users\\user\\Desktop\\{}\\{}'.format(folder_name,f)
    file_list.append(f)


mail_body = 'your files as reqeusted'

 
msg = MIMEMultipart()
msg['Subject'] =  subject
msg['To'] = to_address
msg.attach(MIMEText(mail_body))
 



for file in file_list:
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(file, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(file)))
    msg.attach(part)
 
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(from_address, from_password)
server.sendmail(from_address, to_address, msg.as_string())
server.quit()

# e.g. file = r"C:\Folder1\text1.txt" # if you attach more than two files here, be sure to append them to the files dictionary below, as done for attachemnt_1 and attachment_2.





