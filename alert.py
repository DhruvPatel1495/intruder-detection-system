import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "pateldhruvp1495@gmail.com"
EMAIL_PASSWORD = "pron dkid wwws dowf"


def send_email_alert(image_path):
    msg = EmailMessage()
    msg['Subject'] = '⚠️ Intruder Alert Detected'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    msg.set_content('Intruder detected! See attached image.')

    with open(image_path, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype='jpeg', filename=file_name)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("[INFO] Email sent successfully")
    except Exception as e:
        print("[ERROR] Failed to send email:", e)
