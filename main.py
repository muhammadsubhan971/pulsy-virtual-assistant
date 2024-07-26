import os
import playsound
import eel
from function.engine import *



playassistantsound()

eel.init('web')

os.system('start msedge.exe --app="http://localhost:8000/index1.html"')

eel.start('index1.html', mode=None, host='localhost', block=True)

