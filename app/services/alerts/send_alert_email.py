import os
from sqlalchemy.orm import Session
from app.models.Alert import Alert
from app.modassembly.email.get_email_client import get_email_client
from app.modassembly.database.sql.get_sql_session import get_sql_session

def send_alert_email() -> None:
    smtp_server = os.environ["SMTP_SERVER"]
    smtp_port = int(os.environ["SMTP_PORT"])
    username = os.environ["EMAIL_USERNAME"]
    password = os.environ["EMAIL_PASSWORD"]

    email_client = get_email_client(smtp_server, smtp_port, username, password)

    if email_client is None:
        raise ValueError("Failed to initialize EmailClient")

    with get_sql_session() as session:
        alerts = session.query(Alert).all()

        for alert in alerts:
            to_email = os.environ["ALERT_RECIPIENT_EMAIL"]
            subject = f"Alert: Rule {alert.rule_id.__str__()} Triggered"
            body = f"Transaction ID: {alert.transaction_id.__str__()}\n" \
                   f"Rule ID: {alert.rule_id.__str__()}\n" \
                   f"Timestamp: {alert.timestamp.__str__()}\n" \
                   f"Message: {alert.message.__str__()}"

            email_client.send_email(to_email, subject, body)
