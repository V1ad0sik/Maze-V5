from util.getOffsets import *

import datetime, ctypes

time = "Последнее обновление оффсетов: " + datetime.datetime.utcfromtimestamp(timestamp).strftime("%d.%m.%Y %H:%M")
ctypes.windll.user32.MessageBoxW(0, str(time), str("Информация."), 0)