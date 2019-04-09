import smtplib, ssl
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

subject = "bathroom app"
sender_email = "xxx@mail.com"  # Enter your address
receiver_email = "xxxx@mail.com"  # Enter receiver address
text='''FROM moviepass on Techcrunch:
To be clear, “gaming the system” doesn’t just mean watching a lot of movies — Farnsworth says he’s happy to have “hardcore” users, even if they’re buying way more than $9.95 or $14.95 worth of tickets. Instead, his concern is users who are doing things like sharing their subscription or just using a MoviePass ticket to use the theater’s restroom — something surprisingly common in places like Times Square, where public bathrooms are hard to come by.
https://techcrunch.com/2019/03/21/moviepass-parents-ceo-says-its-rebooted-subscription-service-is-already-profitable/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+Techcrunch+%28TechCrunch%29
'''

for l in range(1):
    now = datetime.datetime.now()
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    message = MIMEMultipart("alternative")
    #message["Subject"] = "%s" %now.strftime("%Y-%m-%d %H:%M")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email
    password = 'xxxxxxxxx'#input("Type your password and press enter: ")
    text = """\
     %s
      """ % text
    context = ssl.create_default_context()
    part1 = MIMEText(text, "plain")
    message.attach(part1)
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
        sender_email, receiver_email, message.as_string()
        )
    print(l,'st email')
    time.sleep(1800)
