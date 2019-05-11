"""This is a simple web scrapper which scrapes prices of the e-commerce site "flipkart".
It sends user a message after the price reaches a certain amount set by user.
User should provide the complete flipkart link for the product to be watched.  """
import os
import time
import subprocess
from sys import platform
import requests
from bs4 import BeautifulSoup
# from plyer import notification
# def notify_windows(title,message):
#   """Function to get notifications for linux OS. """
#   notification.notify(title=title, message=message, app_icon=None, timeout=10)
def notify_linux(message):
    """Function to get notifications for linux OS. """
    subprocess.Popen(['notify-send', message])
    return
def notify_mac(title, text):
    """Function to get notifications for linux OS. """
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
def price_check(url, min_price):
    """Function to check price dropo below a certain amount after every 1800 secs.
    Enter the complete url followed by an integer valued price,
    below which the user will be notified.
    To enable notification for windows based systems please install plyer,
    and comment out the commented code in this entire document.
    """
    res = requests.get(url, timeout=5)
    content = BeautifulSoup(res.content, "html.parser")
    price_div = content.find('div', attrs={"class": "_3qQ9m1"}).text
    price = int((price_div.replace(",", ""))[1:])
    if price <= min_price:
        if platform == "darwin":
            notify_mac(TITLE, MESSAGE)
        elif platform == "linux":
            notify_linux(MESSAGE)
        # else:
        #     notify_windows(TITLE, MESSAGE)
        exit()
    else:
        print("Price still not below minimum price.Checking again after 30 mins")
        time.sleep(1800)
        price_check(URL, MIN_PRICE)
URL = input("Enter the complete link for the product to be monitered.\n")
MIN_PRICE = int(input("Enter the minimum price to get notified for price drop.\n"))
MESSAGE = "Price had dropped below the minimum price."
TITLE = "Price Drop Alert"
price_check(URL, MIN_PRICE)
