# Python 10 minute mail
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
`python3 minutemail.py`
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

""" Ouput:
iexrcerpc@emltmp.com
{
    'to_mail_orig': 'iexrcerpc@emltmp.com',
    'to_mail': 'iexrcerpc@emltmp.com',
    'text_source': 'text',
    'text': 'Some Content\r\n',
    'subject': 'Test',
    'ref': '59bu6khv8e0grt72o3rsnv3o7ffn8dn7',
    'received': '2019-10-14T18:08:55Z',
    'has_html': False,
    'from_mail': 'mike@gmail.com',
    'from_hdr': 'Mike',
    'decode_status': 0,
    'attached': []
}
"""
```
This scipt waits for an email from a specific address:
```
import minutemail

mailbox=minutemail.mailbox()
print(mailbox.email)                            # get the email-adress of the mailbox

while(True):
    result = mailbox.next()
    if(result["from_mail"]=="my@email.com"):    # if email is from specific adress
        print(result["text"])                   # print the content of the mail
        break                                   # and exit

```