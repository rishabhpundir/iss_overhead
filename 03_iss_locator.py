import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 30.733315
MY_LONG = 76.779419
my_email = "mail123@gmail.com"
password = "1234567890"

def iss_is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if 25.0 <= iss_latitude <= 35.0 and 70.0 <= iss_longitude <= 80.0:
        return True

def its_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now <= sunrise or time_now >= sunset:
        return True


while True:
    time.sleep(60)
    if iss_is_overhead and its_night:
        with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs="thephoenixxperson@gmail.com", msg=f"Subject:ISS OVERHEAD\n\nISS is above your head. Get the fuck out & watch it!")





