# EmailServer

A flexible email sending script using SMTP protocols with support for plain text, HTML, and file attachments.

## Features

- Send emails using SMTP
- Support for plain text, HTML, and file attachment email bodies
- Configurable SMTP settings via JSON file
- Docker support for easy deployment

## Prerequisites

- Python 3.7+
- Docker (optional, for containerized deployment)

## Configuration

Create a `config.json` file with your SMTP settings:

```json
{
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "smtp_user": "your_email@example.com",
    "smtp_password": "your_password",
    "receiver": "recipient@example.com",
    "subject": "Email Subject"
}
```

## Local Usage
```bash
# Plain text with attachments
python email_server.py --config config.json --body-type plain --body-content "This is a plain text email" --attachments file1.pdf file2.jpg
# HTML
python email_server.py --config config.json --body-type html --body-content email_template.html
# Inline HTML 
python email_server.py --config config.json --body-type html --body-content "<html><body><h1>This is an HTML email</h1></body></html>"
```

## Docker Usage
```bash
docker build -t emailserver .
docker run -v $(pwd)/config.json:/app/config.json emailserver --config config.json --body-type plain --body-content "This is a plain text email"
```