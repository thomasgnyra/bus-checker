import selenium
import time
from time import sleep
from selenium import webdriver
import twilio
from twilio.rest import Client
import sys

m = 0

while m < 999999999:

    driver = webdriver.Chrome()
    driver.get("https://reservation.pc.gc.ca/Yoho-LakeO'Hara?Calendar")


    from selenium.webdriver.support.ui import Select

    select = Select(driver.find_element_by_id('selResType'))
    select.select_by_visible_text("Day Use (Guided Hikes, Lake O’Hara Bus, Georgian Bay Islands Ferry)")

    select = Select(driver.find_element_by_id('selPartySize'))
    select.select_by_visible_text("1")

    driver.get("https://reservation.pc.gc.ca/Yoho-LakeO'Hara?Calendar")

    
    n=1

    while n < 12:

    #coutn howmanyy images
        images = driver.find_elements_by_tag_name("img")

        imglist = []

        for image in images:
            looper = image.get_attribute('src')

            imglist.append(looper)

            unavail_camp = imglist.count("https://reservation.pc.gc.ca/Images/unavailable_icon20x20.png")
            avail_camp = imglist.count("https://reservation.pc.gc.ca/Images/available_icon20x20.png")

    #if loop to count how many images
        if avail_camp >= 2:
            print("nice")
            account_sid = 'AC4f9f14df6054b82a33c8943fb7e5903a'
            auth_token = '3994734a121cc9dc6114aebe85f72b66'
            client = Client(account_sid, auth_token)

            message = client.messages \
            .create(
            body='Hey, check the site',
            from_='+12897961065',
            to='+15878899917'
            )

            driver.quit()
            sys.exit()
            
        elif avail_camp <= 1:
            print("nope")

        driver.find_element_by_link_text("Next 2 Weeks - >>").click()
        n=n+1

    driver.quit()

    sleep(300)
    m=m+1
