import smtplib as smtp
import datetime as dt
import pandas as pd

my_email = "#email"
password = "#appkey"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data =pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for(index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with open("email.txt") as email_file:
        contents = email_file.read()
        contents = contents.replace("[FULANO]", birthday_person["name"])

    with smtp.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="#emailadress",
            msg=f"Subject:Aniversario de {birthday_person['name']}!\n\n{contents}"
        )