## MouseMover ##

Python application to move mouse when a person don't want to still on the system but also has to be active where the other application records mouse movements as active.

Install required libraries with `pip install -r requirements.txt`

A small GUI is creadted using Tkinter.
Default time for moving mouse is 1 minute.

* Create an _executable_ file for windows machine using `pyi-makespec move_mouse.py`
  * A spec file will be created. Edit the file add `('config.ini', '.')` under a.datas(). 
  * Under a.exe() edit console=False. Save the file
  * Then `pyinstaller move_mouse.spec`
