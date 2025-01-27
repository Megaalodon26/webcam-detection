import smtplib
import filetype
from email.message import EmailMessage


def send_email(image_path):
        email_message = EmailMessage()
        email_message["Subject"] = "Security Alert"
        email_message.set_content("Person detected. See the attached image.")

        with open(image_path, "rb") as file:
            content = file.read()
        email_message.add_attachment(content, maintype="image", subtype=filetype.what(None, content))

        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login("None...@gmail.com", "None")
        gmail.sendmail(None, email_message.as_string())
        gmail.quit()


if __name__ == "__main__":
    send_email(image_path="images/74.png")

