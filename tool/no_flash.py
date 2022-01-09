from util.getGameAddres import *
from util.getOffsets import *

import time


NoFlash_Status = True
NoFlash_Value = 0.0


def NoFlash():
    while (NoFlash_Status):
        lPlayer = pm.read_int(client + dwLocalPlayer)

        if (lPlayer):
            pm.write_float(lPlayer + m_flFlashMaxAlpha, NoFlash_Value)

        time.sleep(0.01)


def NoFlashReset():
    lPlayer = pm.read_int(client + dwLocalPlayer)

    if (lPlayer):
        pm.write_float(lPlayer + m_flFlashMaxAlpha, 255.0)

