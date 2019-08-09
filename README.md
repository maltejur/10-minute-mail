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
`python3 10minmail.py`
<br><br>
It will then copy the resulting email to your clipboard
<br>
Any messages recieved will be printed to stdout.