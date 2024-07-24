import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import json
import argparse
import os

def send_email(config, msg):
    try:
        server = smtplib.SMTP(config['smtp_server'], config['smtp_port'])
        server.starttls()
        server.login(config['smtp_user'], config['smtp_password'])
        server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

def load_config(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    required_keys = ['smtp_server', 'smtp_port', 'smtp_user', 'smtp_password', 'receiver', 'subject']
    assert all(key in config for key in required_keys), f"Missing required keys in config. Required: {required_keys}"
    return config

def create_message(sender, receiver, subject, body_type, body_content, attachments=None):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    # Handle body content
    if body_type == 'plain':
        msg.attach(MIMEText(body_content, 'plain'))
    elif body_type == 'html':
        if os.path.isfile(body_content):
            with open(body_content, 'r', encoding='utf-8') as file:
                html_content = file.read()
            msg.attach(MIMEText(html_content, 'html'))
        else:
            msg.attach(MIMEText(body_content, 'html'))
    else:
        raise ValueError("Invalid body_type. Choose 'plain' or 'html'.")

    # Handle attachments
    if attachments:
        for attachment in attachments:
            with open(attachment, 'rb') as file:
                part = MIMEApplication(file.read(), Name=os.path.basename(attachment))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment)}"'
            msg.attach(part)

    return msg

def main():
    parser = argparse.ArgumentParser(description="Send email")
    parser.add_argument('--config', required=True, help="Path to the config file")
    parser.add_argument('--body-type', choices=['plain', 'html'], required=True, help="Type of email body")
    parser.add_argument('--body-content', required=True, help="Content or file path for email body")
    parser.add_argument('--attachments', nargs='*', help="File paths for attachments")
    args = parser.parse_args()

    config = load_config(args.config)
    msg = create_message(
        config['smtp_user'], 
        config["receiver"], 
        config["subject"], 
        args.body_type, 
        args.body_content, 
        args.attachments
    )
    send_email(config, msg)

if __name__ == '__main__':
    main()