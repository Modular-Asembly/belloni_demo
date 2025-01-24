import os
from sqlalchemy.orm import Session
from app.models.Alert import Alert
from app.modassembly.email.get_email_client import get_email_client, EmailClient
from app.modassembly.database.sql.get_sql_session import get_sql_session
from typing import Iterator, Optional


def send_alert_email() -> None:
    smtp_server: str = os.environ["SMTP_SERVER"]
    smtp_port: int = int(os.environ["SMTP_PORT"])
    username: str = os.environ["SMTP_USERNAME"]
    password: str = os.environ["SMTP_PASSWORD"]

    email_client: Optional[EmailClient] = get_email_client(smtp_server, smtp_port, username, password)

    if email_client is None:
        raise ValueError("Failed to initialize EmailClient")

    session_iterator: Iterator[Session] = get_sql_session()
    session: Session = next(session_iterator)

    try:
        alerts = session.query(Alert).all()

        for alert in alerts:
            to_email: str = os.environ["ALERT_RECIPIENT_EMAIL"]
            subject: str = f"Alert: Transaction {alert.transaction_id.__str__()} Triggered Rule {alert.rule_id.__str__()}"
            body: str = (
                f"Alert ID: {alert.alert_id.__str__()}\n"
                f"Transaction ID: {alert.transaction_id.__str__()}\n"
                f"Rule ID: {alert.rule_id.__str__()}\n"
                f"Timestamp: {alert.timestamp.__str__()}\n"
                f"Message: {alert.message.__str__()}"
            )

            email_client.send_email(to_email, subject, body)
    finally:
        session.close()
