from util.getGameAddres import *
from util.getOffsets import *

import time

GlowESP_HP_Status = False
GlowESP_HP_Color = [0, 0, 0]
GlowESP_HP_Line = 0.7


def GlowESP_HP():
    while (GlowESP_HP_Status):
        lPlayer = pm.read_int(client + dwLocalPlayer)
        
        if (lPlayer):
            glowManager = pm.read_int(client + dwGlowObjectManager)
            mTeam = pm.read_int(lPlayer + m_iTeamNum)

            for i in range(1, 31):
                entity = pm.read_int(client + dwEntityList + i * 0x10)

                if (entity):
                    eTeam = pm.read_int(entity + m_iTeamNum)

                    if (eTeam != mTeam):
                        HP = pm.read_int(entity + m_iHealth)
                        entityGlow = pm.read_int(entity + m_iGlowIndex)

                        if (HP > 70): GlowESP_HP_Color = [0.0, 1.0, 0.0]
                        if (HP < 70 and HP > 30): GlowESP_HP_Color = [1.0, 1.0, 0.0]
                        if (HP < 30): GlowESP_HP_Color = [1.0, 0.0, 0.0]

                        pm.write_float(glowManager + entityGlow * 0x38 + 0x8, GlowESP_HP_Color[0])
                        pm.write_float(glowManager + entityGlow * 0x38 + 0xC, GlowESP_HP_Color[1])
                        pm.write_float(glowManager + entityGlow * 0x38 + 0x10, GlowESP_HP_Color[2])
                        pm.write_float(glowManager + entityGlow * 0x38 + 0x14, GlowESP_HP_Line)

                        pm.write_bool(glowManager + entityGlow * 0x38 + 0x28, True)

        time.sleep(0.01)