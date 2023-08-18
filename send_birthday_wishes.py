import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# API URL details
api_url = 'http://<your_opac_url>>/cgi-bin/koha/svc/report?id=<<REPORT_ID>>'
response = requests.get(api_url)
json_data = response.json()

# Email server settings
smtp_server = '<<Your_smtp_server>>' (Example: smtp.gmail.com)
smtp_port = 587
smtp_username = 'your-email@gmail.com'
smtp_password = 'your-email-password'

# Iterate through the JSON data and send emails
for entry in json_data:
    first_name = entry[0]
    last_name = entry[1]
    email = entry[2]

    # Create email body
    message_body = f"Dear {first_name} {last_name},\n\nHappy birthday! I hope all your birthday wishes and dreams come true.\n\nRegards,\nLearning Resource Centre."

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = email
    msg['Subject'] = 'Birthday Wishes'
    msg.attach(MIMEText(message_body, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(smtp_username, smtp_password)
        smtp_connection.sendmail(smtp_username, email, msg.as_string())
        smtp_connection.quit()
        print(f"Email sent successfully to {email}.")
    except Exception as e:
        print(f"An error occurred while sending the email to {email}: {e}")

