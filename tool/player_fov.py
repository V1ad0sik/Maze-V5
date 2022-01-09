from util.getGameAddres import *
from util.getOffsets import *

import time


PlayerFov_Status = False
PlayerFov_Value = 90


def PlayerFov():
    while (PlayerFov_Status):
        lPlayer = pm.read_int(client + dwLocalPlayer)

        if (lPlayer):
            pm.write_int(lPlayer + m_iDefaultFOV, PlayerFov_Value)

        time.sleep(0.05)


def PlayerFovReset():
    lPlayer = pm.read_int(client + dwLocalPlayer)

    if (lPlayer):
        pm.write_int(lPlayer + m_iDefaultFOV, 90)