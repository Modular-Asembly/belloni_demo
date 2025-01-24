import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional


class EmailClient:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(
        self, to_email: str, subject: str, body: str, is_html: bool = False
    ) -> bool:
        try:
            message = MIMEMultipart()
            message["From"] = self.username
            message["To"] = to_email
            message["Subject"] = subject

            content_type = "html" if is_html else "plain"
            message.attach(MIMEText(body, content_type))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(message)
            return True
        except Exception:
            return False


def get_email_client(
    smtp_server: str, smtp_port: int, username: str, password: str
) -> Optional[EmailClient]:
    return EmailClient(smtp_server, smtp_port, username, password)
