# 10minmail.py
### Just what *you* need
##### _to know to run this damn file._


This is a command-line python client which generates an email address that lasts 10 minutes. It is not traceable back to you. It is a wrapper on the WebSocket endpoint exposed by this [disposable e-mail service](https://dropmail.me/en/).

## Installing Dependencies
### Mac OSx
`sudo pip install --user websocket-client`
<br>
`sudo pip install --user pyperclip`
### Windows
`pip install websocket-client`
<br>
`pip install pyperclip`
## Usage
### Console
`python3 10minmail.py`
<br><br>
It will then copy the resulting email to your clipboard
<br>
Any messages recieved will be printed to stdout.
### Python script
```
import minutemail

mailbox=minutemail.mailbox()
print(mailbox.email)            # get the email-adress of the mailbox
while(True):
    print(mailbox.next())       # get mail in a raw form 
```
This scipt waits for an email from a specific address:
```
import minutemail
from json import loads

mailbox=minutemail.mailbox()
print(mailbox.email)                            # get the email-adress of the mailbox

while(True):
    result = loads(mailbox.next()[1:])
    if(result["from_mail"]=="my@email.com"):    # if email is from specific adress
        print(result["text"])                   # print the content of the mail
        break                                   # and exit

```