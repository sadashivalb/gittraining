import smtplib

fromaddr = 'sadashiv.99b@gmail.com'
toaddrs  = 'sadamsrit@gmail.com'
msg = 'There was a terrible error that occured and I wanted you to know!'

# Credentials (if needed)
username = 'sadashiv.99b'
password = ''

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
