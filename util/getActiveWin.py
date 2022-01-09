from win32gui import GetWindowText, GetForegroundWindow

def gameIsActive():
    if GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive - Direct3D 9":
        return True

    return False