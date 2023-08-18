# KOHA_Birthday_wishes
KOHA_Birthday_wishes automates sending personalized birthday emails via Python. It fetches data from KOHA library API, crafts heartfelt messages, and uses SMTP to send. Saves time and adds a personal touch.

## Birthday Wishes Email Sender
This script is designed to send birthday wishes to individuals using data from a provided API and email them using an SMTP server. It pulls data from the API, creates personalized birthday messages, and sends them via email.
### Prerequisites
- Python 3.x
- Requests library (`pip install requests`) 
- SMTP library (`pip install smtplib`)
### Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/aravindrnair05/KOHA_Birthday_wishes
   cd birthday-wishes
   ```
2. Modify the script (`send_birthday_wishes.py`) to include your API URL and SMTP server details:
   ```python
   api_url = 'http://<<your_opac_url>>/cgi-bin/koha/svc/report?id=<<REPORT_ID>>'
   smtp_server = '<<Your_smtp_server>>' (Example: smtp.gmail.com)
   smtp_port = 587
   smtp_username = 'your-email@gmail.com'
   smtp_password = 'your-email-password'
   ```
3. Run the script:
   ```bash
   python send_birthday_wishes.py
   ```
### Scheduling the Script
To run the script every morning using a cron job, follow these steps:
1. Open your terminal.
2. Edit your crontab file by running the command:
   ```bash
   crontab -e
   ```
3. Add a new line at the end of the file to schedule the script to run every morning at a specified time. For example, to run at 7:00 AM, use:
   ```bash
   0 7 * * * /path/to/python /path/to/birthday-wishes/send_birthday_wishes.py
   ```
   Replace `/path/to/python` with the actual path to your Python executable and `/path/to/birthday-wishes/send_birthday_wishes.py` with the full path to your script.
4. Save the file and exit the text editor.

The cron job is now set up to run the script every morning at the specified time.


## Features
- Pulls data from the provided API to get birthday information.
- Creates personalized birthday messages for each individual.
- Sends emails using the specified SMTP server and credentials.
## Contributing
If you'd like to contribute to this project, feel free to submit a pull request. Any contributions are welcome!

