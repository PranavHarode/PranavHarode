import smtplib

To=input("Enter Receiver's Email Address :" )

message=input("Enter a message to send :")

def sendEmail(To,message):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("Sender's Email","password")
    server.sendmail("sendermail",To,message)
    server.close()

sendEmail(To,message)
