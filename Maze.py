from util.getGameAddres import *
from util.getOffsets import *
from util.softExit import*
from util.GUI import *

import tool.glow_esp as glow_esp
import tool.glow_esp_hp as glow_esp_hp
import tool.chams as chams
import tool.player_fov as player_fov
import tool.trigger_bot as trigger_bot
import tool.auto_pistol as auto_pistol
import tool.bunny_hop as bunny_hop
import tool.no_flash as no_flash
import tool.show_money as show_money
import tool.global_wh as global_wh
import tool.lastUp as lastUp

import sys

from PyQt5.QtWidgets import QColorDialog
from PIL import ImageColor
from threading import Thread


if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   ui = Widget()
   ui.show()

   def GlowESP_Start():
       if (ui.checkBox.isChecked()):
           glow_esp.GlowESP_Status = True
           Thread(target = glow_esp.GlowESP).start()

       else:
           glow_esp.GlowESP_Status = False


   def GlowESPGetColor():
       getColor = QColorDialog.getColor()

       cR = ImageColor.getcolor(getColor.name(), "RGB")[0]
       cG = ImageColor.getcolor(getColor.name(), "RGB")[1]
       cB = ImageColor.getcolor(getColor.name(), "RGB")[2]

       glow_esp.GlowESP_Color = [cR, cG, cB]
       
       ui.pushButton_2.setStyleSheet("QPushButton{background-color: rgb(" + str(cR) + "," + str(cG) + "," + str(cB) + "); border: none; border-radius: 3px;}")


   def GlowESP_SetLine():
       glow_esp.GlowESP_Line = float(ui.horizontalSlider.value() / 10)
       
       _translate = QtCore.QCoreApplication.translate
       ui.label_3.setText(_translate("Form", f"<html><head/><body><p><span style=\" color:#f5f6fa;\">{str(glow_esp.GlowESP_Line)}</span></p></body></html>"))


   def GlowESP_HP_Start():
       if (ui.checkBox_2.isChecked()):
           glow_esp_hp.GlowESP_HP_Status = True
           Thread(target = glow_esp_hp.GlowESP_HP).start()

       else:
           glow_esp_hp.GlowESP_HP_Status = False

 
   def GlowESP_HP_SetLine():
       glow_esp_hp.GlowESP_HP_Line = float(ui.horizontalSlider_2.value() / 10)

       _translate = QtCore.QCoreApplication.translate
       ui.label_4.setText(_translate("Form", f"<html><head/><body><p><span style=\" color:#f5f6fa;\">{str(glow_esp_hp.GlowESP_HP_Line)}</span></p></body></html>"))


   def Chams_Start():
       if (ui.checkBox_3.isChecked()):
           chams.Chams_Status = True
           Thread(target = chams.Chams).start()

       else:
           chams.Chams_Status = False
           chams.ChamsReset()


   def ChamsSetColor():
       getColor = QColorDialog.getColor()

       cR = ImageColor.getcolor(getColor.name(), "RGB")[0]
       cG = ImageColor.getcolor(getColor.name(), "RGB")[1]
       cB = ImageColor.getcolor(getColor.name(), "RGB")[2]

       chams.Chams_Color = [cR, cG, cB]
       
       ui.pushButton_3.setStyleSheet("QPushButton{background-color: rgb(" + str(cR) + "," + str(cG) + "," + str(cB) + "); border: none; border-radius: 3px;}")


   def PlayerFov_Start():
        if (ui.checkBox_5.isChecked()):
           player_fov.PlayerFov_Status = True
           Thread(target = player_fov.PlayerFov).start()

        else:
           player_fov.PlayerFov_Status = False
           player_fov.PlayerFovReset()


   def PlayerFov_SetValue():
       player_fov.PlayerFov_Value = ui.horizontalSlider_3.value()

       _translate = QtCore.QCoreApplication.translate
       ui.label_5.setText(_translate("Form", f"<html><head/><body><p><span style=\" color:#f5f6fa;\">{str(player_fov.PlayerFov_Value)}</span></p></body></html>"))


   def TriggerBot_Start():
       if (ui.checkBox_6.isChecked()):
           trigger_bot.TriggerBot_Status = True
           Thread(target = trigger_bot.TriggerBot).start()

       else:
           trigger_bot.TriggerBot_Status = False


   def TriggetBot_SetMouse():
       MouseList = {"M1": 1, "M2": 2, "M3": 3, "M4": 4, "M5": 5, "M6": 6}

       trigger_bot.TriggerBot_Mouse = MouseList[ui.comboBox.currentText()]


   def TriggetBot_SetValue():
       trigger_bot.TriggerBot_Delay = float(ui.horizontalSlider_4.value() / 10)

       _translate = QtCore.QCoreApplication.translate
       ui.label_7.setText(_translate("Form", f"<html><head/><body><p><span style=\" color:#f5f6fa;\">{str(trigger_bot.TriggerBot_Delay)}</span></p></body></html>"))


   def AutoPistol_Start():
       if (ui.checkBox_7.isChecked()):
           auto_pistol.AutoPistol_Status = True
           Thread(target = auto_pistol.AutoPistol).start()

       else:
           auto_pistol.AutoPistol_Status = False


   def BunnyHop_Start():
       if (ui.checkBox_8.isChecked()):
           bunny_hop.BHop_Status = True
           Thread(target = bunny_hop.BHop).start()

       else:
           bunny_hop.BHop_Status = False


   def NoFlash_Start():
       if (ui.checkBox_9.isChecked()):
           no_flash.NoFlash_Status = True
           Thread(target = no_flash.NoFlash).start()

       else:
           no_flash.NoFlash_Status = False
           no_flash.NoFlashReset()


   def NoFlash_SetValue():
       no_flash.NoFlash_Value = float(ui.horizontalSlider_5.value())

       _translate = QtCore.QCoreApplication.translate
       ui.label_9.setText(_translate("Form", f"<html><head/><body><p><span style=\" color:#f5f6fa;\">{str(int(no_flash.NoFlash_Value))}</span></p></body></html>"))


   ui.pushButton.clicked.connect(pExit)

   ui.checkBox.stateChanged.connect(GlowESP_Start)
   ui.pushButton_2.clicked.connect(GlowESPGetColor)
   ui.horizontalSlider.valueChanged.connect(GlowESP_SetLine)

   ui.checkBox_2.stateChanged.connect(GlowESP_HP_Start)
   ui.horizontalSlider_2.valueChanged.connect(GlowESP_HP_SetLine)

   ui.checkBox_3.stateChanged.connect(Chams_Start)
   ui.pushButton_3.clicked.connect(ChamsSetColor)

   ui.checkBox_4.stateChanged.connect(lambda: global_wh.GlobalWH())

   ui.checkBox_5.stateChanged.connect(PlayerFov_Start)
   ui.horizontalSlider_3.valueChanged.connect(PlayerFov_SetValue)

   ui.checkBox_6.stateChanged.connect(TriggerBot_Start)
   ui.comboBox.currentIndexChanged.connect(TriggetBot_SetMouse)
   ui.horizontalSlider_4.valueChanged.connect(TriggetBot_SetValue)

   ui.checkBox_7.stateChanged.connect(AutoPistol_Start)
   ui.checkBox_8.stateChanged.connect(BunnyHop_Start)

   ui.checkBox_9.stateChanged.connect(NoFlash_Start)
   ui.horizontalSlider_5.valueChanged.connect(NoFlash_SetValue)

   ui.checkBox_10.stateChanged.connect(show_money.ShowMoney)
   
   sys.exit(app.exec_())