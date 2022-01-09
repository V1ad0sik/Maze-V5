from util.getGameAddres import *
from util.getOffsets import *

import time, keyboard


BHop_Status = False


def BHop():
    while (BHop_Status):
        lPlayer = pm.read_int(client + dwLocalPlayer)

        if (lPlayer):
            MoveFlag = pm.read_int(lPlayer + m_fFlags)

            if (MoveFlag == 257 or MoveFlag == 263):

                if keyboard.is_pressed("space"):
                    forceJump = client + dwForceJump

                    pm.write_int(forceJump, 5)
                    time.sleep(0.2)
                    pm.write_int(forceJump, 4)

        time.sleep(0.01)