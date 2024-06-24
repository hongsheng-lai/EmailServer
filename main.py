import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import json
import argparse

def send_email(config, msg):
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(config['smtp_server'], config['smtp_port'])
        server.starttls()  # Secure the connection
        server.login(config['smtp_user'], config['smtp_password'])  # Login to the SMTP server
        server.send_message(msg)  # Send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()  # Close the connections
        
def load_config(config_path):
    """
    load config and check if it is valid
    {
        "smtp_server": "smtp.example.com", 
        "smtp_port": 587, 
        "smtp_user": "your_email@example.com", 
        "smtp_password": "your_password"
    } 
    """
    with open(config_path, 'r') as f:
        config = json.load(f)
        assert all(key in config for key in ['smtp_server', 'smtp_port', 'smtp_user', 'smtp_password'])
        
    return config
    
def create_msg_plain(sender, receiver, subject, body):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    return msg

def main():
    parser = argparse.ArgumentParser(description="Send email")
    parser.add_argument('--config', required=True, help="path to the config file")
    # parser.add_argument('--receiver', required=True, help="email address of the receiver")
    # parser.add_argument('--subject', required=True, help="subject of the email")
    # parser.add_argument('--body', required=True, help="body of the email")
    
    args = parser.parse_args()
    
    config = load_config(args.config)
    msg = create_msg_plain(config['smtp_user'], config["receiver"], config["subject"], config["body"])
    send_email(config, msg)


if __name__ == '__main__':
    main()