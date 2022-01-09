from util.getGameAddres import *
from util.getOffsets import *
from util.getActiveWin import *

import time

from win32api import GetKeyState


AutoPistol_Status = False


def AutoPistol():
    while (AutoPistol_Status):
        if GetKeyState(1) == -127 or GetKeyState(1) == -128:

            lPlayer = pm.read_int(client + dwLocalPlayer)

            if (lPlayer and gameIsActive()):
                pm.write_int(client + dwForceAttack, 6)

        time.sleep(0.02)