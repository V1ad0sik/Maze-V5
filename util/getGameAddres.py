import pymem, ctypes

import util.softExit as softExit


try:
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

except Exception as _except:
    ctypes.windll.user32.MessageBoxW(0, str(_except), str("Ошибка."), 0)
    softExit.pExit()