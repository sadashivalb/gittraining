import smtplib

SERVER = "mailserve"

FROM = "sada@gmail.com"
TO = ["sadamsrit@gmail.com"] # must be a list

SUBJECT = "Jiv544 site updated"

TEXT = """Hi Team,


Thanks
Sadashiv
"""

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()
