import smtplib
import os

CARRIERS = {"verizon": "@vtext.com"}
EMAIL = os.environ.get("EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")


def send_message(
    carrier,
    message,
    PHONE_NUMBER=PHONE_NUMBER,
):
    recipient = PHONE_NUMBER + CARRIERS[carrier]
    auth = (EMAIL, APP_PASSWORD)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
    server.sendmail(auth[0], recipient, message)


def main():

    message = "check kar"
    carrier = "verizon"
    message = message

    send_message(carrier, message)


if __name__ == "__main__":
    main()
