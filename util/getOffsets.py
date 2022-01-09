import requests

offsetsList = requests.get("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json").json()

timestamp = offsetsList["timestamp"]
dwLocalPlayer = offsetsList["signatures"]["dwLocalPlayer"]
dwEntityList = offsetsList["signatures"]["dwEntityList"]
dwGlowObjectManager = offsetsList["signatures"]["dwGlowObjectManager"]
dwForceAttack = offsetsList["signatures"]["dwForceAttack"]
dwForceJump = offsetsList["signatures"]["dwForceJump"]


m_iTeamNum = offsetsList["netvars"]["m_iTeamNum"]
m_iHealth = offsetsList["netvars"]["m_iHealth"]
m_iGlowIndex = offsetsList["netvars"]["m_iGlowIndex"]
m_clrRender = offsetsList["netvars"]["m_clrRender"]
m_iDefaultFOV = offsetsList["netvars"]["m_iDefaultFOV"]
m_iCrosshairId = offsetsList["netvars"]["m_iCrosshairId"]
m_fFlags = offsetsList["netvars"]["m_fFlags"]
m_flFlashMaxAlpha = offsetsList["netvars"]["m_flFlashMaxAlpha"]