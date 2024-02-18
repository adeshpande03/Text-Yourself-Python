import smtplib
import os
from generateMessage import generateMessage

# https://medium.com/testingonprod/how-to-send-text-messages-with-python-for-free-a7c92816e1a4
CARRIERS = {
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
}
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

    carrier = "verizon"
    message = generateMessage()
    # print(len(message))
    print(message)

    send_message(carrier, message)


if __name__ == "__main__":
    main()
