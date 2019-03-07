 import smtplib

regularPort = 587
att_verizon_port = 465

Gmail = 'smtp.gmail.com'
Outlook = 'smtp-mail.outlook.com'
Yahoo_Mail = 'smtp.mail.yahoo.com'
AT&T = 'smpt.mail.att.net'
Comcast = 'smtp.comcast.net'
Verizon = 'smtp.verizon.net'




smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')
smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So')
smtpObj.quit()



def Gmail(provider, port):
    smtpObj = smtplib.SMTP('smtp.example.com', regularPort)
    smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So')
    smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')
    smtpObj.quit()
def Outlook(provider, port):
    smtpObj = smtplib.SMTP('smtp.example.com', regularPort)
    smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So')
    smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')
    smtpObj.quit()
def Yahoo_Mail(provider, port):
    smtpObj = smtplib.SMTP('smtp.example.com', regularPort)
    smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So')
    smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')
    smtpObj.quit()
def att(provider, port):
    smtpObj = smtplib.SMTP('smtp.example.com', regularPort)
    smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So')
    smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')
    smtpObj.quit()


print("pick from service provider:\n 1. Gmail\n2. Outlook\n3. Yahoo Mail\n4. AT&T\n5. Comcast\n6. Verizon")
smtpConnection = input("What is the email provider you wish to use\n> ")

EMAIL = input("Please type in the email for the provider\n> ")
MY_SECRET_PASSWORD = input("please type in the passowrd:\n> ")
MESSAGE = input("type in a message for the email\n> ")
while True:
    for message in MESSAGE:


try:
    if smtpConnection == "1.":
