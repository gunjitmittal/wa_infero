import pywhatkit
import time
from keyboard import press
from datetime import datetime, timedelta

now = datetime.now()
now = now + timedelta(minutes=1)
pywhatkit.sendwhatmsg_to_group("Bn3CPQ66yOh9ewXVp93hMv","lorem ipsum",now.hour,now.minute,10,True)
press('enter')
