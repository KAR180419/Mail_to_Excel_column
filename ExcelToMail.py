import pandas as pd
import smtplib, ssl
import getpass

emails = pd.read_excel(r'NameEmails.xlsx')
bcc = list(emails['E mail'])

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = input("Enter Sender Email: ")  # Enter your address
receiver_email = input("Enter Receiver Email: ")  # Enter receiver address
password = getpass.getpass('Password:')
sub = input("Enter Subject line: ")
message_text = input("Enter body of Email: ")
message = "From: %s\r\n" % sender_email + "To: %s\r\n" % receiver_email + "Subject: %s\r\n" % sub + "\r\n" + message_text
total = [sender_email] + bcc

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, total, message)