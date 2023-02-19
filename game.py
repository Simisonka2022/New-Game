import os
import smtplib
import time
import urllib.request

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# E-mail beállítások
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'zalansimi@gmail.com'
smtp_password = 'jelszó'

# Címzett
to_email = 'zalansimi@gmail.com'

# Kép neve
image_name = 'photo.jpg'

# Kamera elérése
os.system('termux-camera-photo -c 0 ' + image_name)

# Várakozás a kép elkészülésére
time.sleep(3)

# Kép betöltése és e-mail mellékletként való elküldése
with open(image_name, 'rb') as f:
    img_data = f.read()

msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = to_email
msg['Subject'] = 'Kép a kamerából'

image = MIMEImage(img_data, name=image_name)
msg.attach(image)

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)
server.sendmail(smtp_username, to_email, msg.as_string())
server.quit()

# Kép törlése
os.remove(image_name)
