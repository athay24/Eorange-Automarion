# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:34:27 2021

@author: athay
"""

#importing necessary libraries
import time
import smtplib, ssl
from selenium import webdriver
import bs4
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from datetime import datetime

product = 'Discover Disc 125'

password = input("Mail Password")

#sending email function
def send_email():
    port = 465  # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("reashedkamal@gmail.com", password)
        sender_email = "reashedkamal@gmail.com"
        receiver_email = ["athaykamal@gmail.com", "athaykamal1@gmail.com"]
        message = """\
        Subject: Eorange Live\n
        
        This message is sent from Python.
        Discover is live!! Hurry up.
        """
        server.sendmail(sender_email, receiver_email, message)

    
    
    
ua = UserAgent()

opts = Options()
opts.add_argument("user-agent"+ua.random)

driver = webdriver.Chrome()

#logging into Eorange
driver.get('https://www.eorange.shop/user/login')

user_name = input('Mail: ')
password = input('Password: ')


user_box = driver.find_element_by_xpath('//*[@id="username"]')
user_box.send_keys(user_name)
password_box = driver.find_element_by_xpath('//*[@id="password"]')
password_box.send_keys(password)

login_button = driver.find_element_by_xpath('//*[@id="register"]')
login_button.click()
circle = 0
status = []
while circle<60:
    #motorcycle link
    search_box = driver.find_element_by_xpath('//*[@id="app"]/header/div[3]/div/div[1]/div[2]/div/div/div[1]/form/input')
    search_box.send_keys(product)
    
    search_button = driver.find_element_by_xpath('//*[@id="app"]/header/div[3]/div/div[1]/div[2]/div/div/div[1]/form/button')
    search_button.click()
    
    #driver.get('https://www.eorange.shop/search?product=DISCOVER%20DISC%20125')
    html = driver.page_source
    soup = bs4.BeautifulSoup(html, 'html.parser')
    item_in_store = soup.find_all('li',class_='sold-out')
    now = datetime.now()
  
    current_time = now.strftime("%H:%M:%S")
    if 'sold-out' in html:
        status.append(' Stock-out ')
        status.append(current_time)
        print(circle, current_time, ' Stock-out')
    else:
        status.append(" Live ")
        status.append(current_time)
        print(circle, current_time, " Live")
    circle = circle+1
    time.sleep(120)
print(status)
