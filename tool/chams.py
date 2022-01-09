from util.getGameAddres import *
from util.getOffsets import *

import time


Chams_Status = False
Chams_Color = [255, 255, 255]


def Chams():
    while (Chams_Status):
        lPlayer = pm.read_int(client + dwLocalPlayer)

        if (lPlayer):
            mTeam = pm.read_int(lPlayer + m_iTeamNum)

            for i in range(1, 32):
                entity = pm.read_int(client + dwEntityList + i * 0x10)

                if (entity):
                    eTeam = pm.read_int(entity + m_iTeamNum)

                    if (eTeam != mTeam):
                        pm.write_int(entity +  m_clrRender, Chams_Color[0])
                        pm.write_int(entity +  m_clrRender + 0x1, Chams_Color[1])
                        pm.write_int(entity +  m_clrRender + 0x2, Chams_Color[2])
                        pm.write_int(entity +  m_clrRender + 0x3, 1)

        time.sleep(0.2)


def ChamsReset():
    lPlayer = pm.read_int(client + dwLocalPlayer)

    if (lPlayer):
        for i in range(1, 32):
            entity = pm.read_int(client + dwEntityList + i * 0x10)

            if (entity):
                pm.write_int(entity +  m_clrRender, 255)
                pm.write_int(entity +  m_clrRender + 0x1, 255)
                pm.write_int(entity +  m_clrRender + 0x2, 255)