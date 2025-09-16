#LED TEST
import sys
import time
import datetime #importing the date and time library
import telepot  #importing telepot library
from telepot.loop import MessageLoop #library function to communicate with telegram bot
import RPi.GPIO as GPIO #importing GPIO library to use pins of GPIO pins of Raspberrypi
from time import sleep # to provide delays in program

red_led_pin=21
green_led_pin=20

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led_pin,GPIO.OUT)
GPIO.setup(green_led_pin,GPIO.OUT)

now = datetime.datetime.now() #Getting date and time

def handle(msg):
    chat_id=msg['chat']['id'] #receiving the message from telegram
    command=msg['text']   #getting text from the message

    print('Received:')
    print(command)

    #comparing message to send a reply according to it
    if command =='/hi':
        bot.sendMessage (chat_id, str("Hi! GHENT_LEDMATRIX"))
    elif command == '/time':
        bot.sendMessage (chat_id, str("Time: ") + str(now.hour) + str(":") + str(now.minute)+ str(":")+ str(now.second))
    elif command == '/date':
        bot.sendMessage (chat_id, str("Date: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))
    elif command == '/red_1':
        bot.sendMessage(chat_id, str("RED LED is ON"))
        GPIO.output(red_led_pin, True)
    elif command == '/red_0':
        bot.sendMessage(chat_id, str("RED LED is OFF"))
        GPIO.output(red_led_pin, False)
    elif command == '/green_1':
        bot.sendMessage(chat_id, str("Green LED is ON"))
        GPIO.output(green_led_pin, True)
    elif command == '/green_0':
        bot.sendMessage(chat_id, str("Green LED is OFF"))
        GPIO.output(green_led_pin, Fasle)

# insert your telegram token below
bot = telepot.Bot('741215043:AAF8rnuk1oGErCJd90ooHnKUKhtVgq2Lwo0')
print (bot.getMe())
# start listening to the telegram bot  and whenever a message is received the handle function is called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

while 1:
    sleep(10) 
