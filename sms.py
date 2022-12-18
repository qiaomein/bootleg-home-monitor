from dotenv import load_dotenv
import email, smtplib, ssl, os
from providers import PROVIDERS

def send_sms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    subject: str = "sent using etext",
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
):
    sender_email, email_password = sender_credentials
    receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'

    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(
        smtp_server, smtp_port, context=ssl.create_default_context()
    ) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)


def send_sms(message):
    load_dotenv()
    number = os.getenv("NUMBER")
    provider = os.getenv("PROVIDER")

    sender_credentials = ("jackqiao2002@gmail.com", os.getenv("PASS"))

    send_sms_via_email(number, message, provider, sender_credentials)

if __name__ == "__main__":
    load_dotenv()
    number = os.getenv("NUMBER")
    provider = os.getenv("PROVIDER")
    message = "I can smell you..."

    sender_credentials = ("jackqiao2002@gmail.com", os.getenv("PASS"))

    send_sms_via_email(number, message, provider, sender_credentials)