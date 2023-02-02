##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import random
import datetime as dt
import csv
import pandas as pd

birthday_ppl = pd.read_csv("birthdays.csv")
birthday_names = []
now = dt.datetime.now()
day = now.day
month = now.month
for index,row in birthday_ppl.iterrows():
    if day == row['day'] and month == row['month']:
        birthday_names.append((row['name'],row['day'],row['month'],row['email']))

if len(birthday_names) != 0:
    for person in birthday_names:
        # letter_list = ["letter_1.txt","letter_2.txt","letter_3.txt"]
        my_email = "mufeez08@gmail.com"
        password = "tpwtquwjpsaoceiu"
        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt",'r+') as file:
            bday_letter_list = file.readlines()
            content = bday_letter_list.copy()
            content[0] = content[0].replace('[NAME]',person[0])
            msg = ''.join(content)

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=f"{person[3]}",
                    msg=f"Subject:HAPPY BIRTHDAY {person[0].upper()}!\n\n" + msg
                )










