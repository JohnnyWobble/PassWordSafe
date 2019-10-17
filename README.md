# PassWordSafe
 This will save your passwords in an ultra-mega secure way, it uses premier technoloy such as the patent pending `*.passwords` file type to store your passwords safely. They won't even have and app to open it!
 
 ## Requirements
This just uses `cryptography` so that is an easy `pip install cryptography` and you are set to go!
(Also uses python 3.7)

## Usage
I would suggest on linux adding this to your home folder or just like `Documents/`. On windows I guess you could put it in your user file. This does contain a shebang for a universal python(3.7) install but you could always do `python3 PassWordSafe`, if you do have a vitual env you will need to change the shebang. As a side note this clears your screen to stop people from reading your passwords, but the screen clear doesn't work on the PyCharm run window, so you should only run it in the terminal. It will say `TERM environment variable not set.` if you are running it in PyCharm, it is not a fatal error but it is annoying. 
