from util.getGameAddres import *
from util.getOffsets import *

import time


GlowESP_Status = False
GlowESP_Color = [255, 255, 255]
GlowESP_Line = 0.7


def GlowESP():
    while (GlowESP_Status):
        lPlayer = pm.read_int(client + dwLocalPlayer)
        
        if (lPlayer):
            glowManager = pm.read_int(client + dwGlowObjectManager)
            mTeam = pm.read_int(lPlayer + m_iTeamNum)

            for i in range(1, 31):
                entity = pm.read_int(client + dwEntityList + i * 0x10)

                if (entity):
                    eTeam = pm.read_int(entity + m_iTeamNum)

                    if (eTeam != mTeam):
                        entityGlow = pm.read_int(entity + m_iGlowIndex)

                        pm.write_float(glowManager + entityGlow * 0x38 + 0x8, (GlowESP_Color[0] / 255))
                        pm.write_float(glowManager + entityGlow * 0x38 + 0xC, (GlowESP_Color[1] / 255))
                        pm.write_float(glowManager + entityGlow * 0x38 + 0x10, (GlowESP_Color[2] / 255))
                        pm.write_float(glowManager + entityGlow * 0x38 + 0x14, GlowESP_Line)

                        pm.write_bool(glowManager + entityGlow * 0x38 + 0x28, True)

        time.sleep(0.01)