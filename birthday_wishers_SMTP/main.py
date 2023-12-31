import smtplib
import random
from datetime import datetime
import pandas

OWN_EMAIL = "OWN_EMAIL"
OWN_EMAIL_PASSWORD = "OWN_EMAIL_PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthday.csv")
birthdays_dict = {(data_row.month,data_row.day): data_row for (index,data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person.name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL,OWN_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=OWN_EMAIL,
            to_addrs=birthday_person.email,
            msg=f"Subject: Happy Birthday\n\n{contents}"
        )