import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import email
import json
import os
from jarvis.features.speech import speak
from jarvis.features.listen import takecommand
from jarvis.config.configuration import password,username
import datetime
# import time
import threading

# Function to send an email
smtp_server = 'smtp.gmail.com'
smtp_port = 587
imap_server = 'imap.gmail.com'
imap_port = 993

username = username
password = password
output_dir = 'emails'

file_path = 'jarvis\database\email_user.json'
email_file_path ='jarvis\database\emails.json'
def get_sender():
    with open(file_path, 'r') as file:
        senders = json.load(file)
    return senders

def update_dic(senders):
    with open(file_path, 'w') as file:
        json.dump(senders, file)

def search_key(key):
    senders = get_sender()

    if key in senders:
        print(senders[key])
        return senders[key]
    else:
        speak(
            'Sir, the sender is not found in data base, would you like to add the sender name and email in data base ?')
        response = takecommand().lower()
        if 'yes' in response or 'definitely' in response:
            speak('Sir, please write down the sender email')
            sender_email = str(input(
                'Please write down email please note that write on username not domain because currently after @ is not workign: '))

            email1 = str(sender_email + '@gmail.com')
            senders[key] = email1

            update_dic(senders)
            return email1
        elif 'no' in response or 'nah' in response or 'not now' in response:
            speak('Okay, sir. will not update email in database, sir please write down sender email')
            sender_email = str(input(
                'Please write down email please note that write on username not domain because currently after @ is not workign: '))

            email1 = str(sender_email + '@gmail.com')
            print(email1)
            return email1

        else:
            sender_email = str(input(
                'Please write down email please note that write on username not domain because currently after @ is not workign: '))

            email1 = str(sender_email + '@gmail.com')

            print(email1)
            return email1

    return None

def send_email(subject, message, to_email):
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to_email
    msg['Subject'] = subject

    body = MIMEText(message, 'plain')
    msg.attach(body)
    # with open(attachment_path, 'rb') as file:
    #     # attachment = MIMEApplication(file.read(), Name='attachment')
    #     # attachment['Content-Disposition'] = f'attachment; filename="{attachment_path}"'
    #     msg.attach(attachment)
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        server.quit()
        speak('Sir, Mail has been sent successfully.')
    except Exception as e:
        print("Error sending email:", str(e))
        speak('Sir, mail can not sent due to error has occured')


def search_in_mail():
    read_and_save_emails()
    # Read emails from JSON file and search for specific sender or subject
    speak('Sir, reading emails from jeson file')
    with open(email_file_path, 'r') as file:
        emails = json.load(file)
        
    # print(type(emails))
    # speak(f'Sir, the type of emails is {type(emails)}')
    speak(f'Total emails are {int(len(emails))}')
    speak('Sir by which email you want to search ? by keyword or sender name or want to read all ?')
    userresponse = takecommand().lower()
  
    if 'all' in userresponse or 'read all' in userresponse:
        i = int(1)
        
        for email in emails:
            def reademails():
                speak(f"sir, the subject {i} of mail is {email['subject']} and sender is {email['from']}")
            def takeinput():
                inp = takecommand().lower() 
                if 'read this email' in inp or 'read body of email' in inp or 'read full email' in inp:
                    
                    speak('Ok, sir')
                    
                    speak(f'Ok, sir. Reading the body of the email {email["body"]}')
                else:
                    return   
            # t1  = threading.Thread(target=reademails,args=())
            
            # print(f"{i} ==> {email['from']}")
            # t2 = threading.Thread(target=takeinput,args=())
            # t1.start()
            # t2.start()
            # t1.join()
            # t2.join()
            # i = i + 1
        speak('Sir, all mails are read')
    elif 'by name ' in userresponse or 'namewise' in userresponse or 'name' in userresponse:
        speak('Sir, please say sender name')
        userresponse = takecommand().lower()
        results = []
        userresponse = userresponse.replace('jarvis', '').replace('please', '').replace('search', '')
        for data in emails:
            if "from" in data and userresponse in data["from"]:
                results.append(data)

        speak(f'Sir search complete, and total founds emails number is {str(len(results))}')
        speak('Sir, all are printed please check terminal ')
        print(results)

    elif 'by keyword' in userresponse or 'keyword' in userresponse:
        speak('Sir, please say keywor')
        userresponse = takecommand().lower()
        results = []
        userresponse = userresponse.replace('jarvis', '').replace('please', '').replace('search', '')
        for data in emails:
            if "from" in data and userresponse in data["from"]:
                results.append(data)
            elif 'subject' in data and userresponse in data["subject"]:
                results.append(data)
            elif 'body' in data and userresponse in data["body"]:
                results.append(data)

        speak(f'Sir search complete, and total founds emails number is {str(len(results))}')
        speak('Sir, all are printed please check terminal ')
        for i in range(len(results)):
            speak()
            
        print(results)
    

# Function to save emails in a JSON file
def save_emails_as_json(emails):
    email_data = []

    for email_message in emails:
        subject = email_message['Subject']
        date = email_message['Date']
        email_id = email_message['Message-ID']

        # Extract email body
        body = extract_email_body(email_message)

        # Create dictionary for email data
        email_data.append({
            'email_id': email_id,
            'subject': subject,
            'date': date,
            'from': email_message['From'],
            'to': email_message['To'],
            'body': body
        })

    # Save email data as a JSON file
    filepath = os.path.join(email_file_path)

    with open(filepath, 'w') as f:
        json.dump(email_data, f, indent=4)

    print("All emails saved as a JSON file!")


# Function to extract email body
def extract_email_body(email_message):
    if email_message.is_multipart():
        for part in email_message.walk():
            content_type = part.get_content_type()
            if content_type == 'text/plain' or content_type == 'text/html':
                return part.get_payload(decode=True).decode()
    else:
        return email_message.get_payload(decode=True).decode()


# Function to read and save emails as JSON
def read_and_save_emails():
    emails = []

    try:
        server = imaplib.IMAP4_SSL(imap_server, imap_port)
        server.login(username, password)
        server.select("INBOX")

        # Get the current month
        now = datetime.datetime.now()
        month = now.month
        year = now.year

        # Search for all emails from this month
        # search_query = '(UNSEEN OR FLAGGED) IMPORTANT'

        
        result, data = server.search(None, "UNSEEN")
        print(result)
        print(data)
        email_ids = data[0].split()
        print(email_ids)
        for email_id in email_ids:
            result, email_data = server.fetch( email_id, '(RFC822)')
            raw_email = email_data[0][1]

            # Parse the raw email data
            email_message = email.message_from_bytes(raw_email)

            emails.append(email_message)

        server.logout()
        print("All emails read successfully!")

        # Save emails as a JSON file
        save_emails_as_json(emails)
    except Exception as e:
        print("Error reading and saving emails:", str(e))
        speak('Sir, error is found please check terminal')
        speak(f'Sir, the error is {e}')
# read_and_save_emails()