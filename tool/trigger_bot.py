from util.getGameAddres import *
from util.getOffsets import *
from util.getActiveWin import *

from win32api import GetKeyState

import time


TriggerBot_Status = False
TriggerBot_Delay = 0.3
TriggerBot_Mouse = 1


def TriggerBot():
    while (TriggerBot_Status):

        if (GetKeyState(TriggerBot_Mouse) == -127 or GetKeyState(TriggerBot_Mouse) == -128):
            lPlayer = pm.read_int(client + dwLocalPlayer)

            if (lPlayer and gameIsActive()):
                entityID = pm.read_int(lPlayer + m_iCrosshairId)
                entity = pm.read_int(client + dwEntityList + (entityID - 1) * 0x10)

                if (entity and entityID > 0 and entityID <= 32):
                    mTeam = pm.read_int(lPlayer + m_iTeamNum)
                    eTeam = pm.read_int(entity + m_iTeamNum)

                    if (eTeam != mTeam):
                        time.sleep(TriggerBot_Delay)
                        pm.write_int(client + dwForceAttack, 6)    
            
        time.sleep(0.01)