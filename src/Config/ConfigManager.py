import c4d

from ..Const import Const
from .ConfigManagerCorona import ConfigManagerCorona

const = Const()

class ConfigManager(c4d.gui.GeDialog, ConfigManagerCorona):
    def __init__(self):
        self.jsonContent = self.loadJsonFile()
        self.coronaConfig = self.jsonContent["corona"]
        self.dataChanged = False

    def Command(self, id, msg):
        if id == const.UI_OPTION_END_OK:
            self.generateCoronajson(self)
            self.jsonContent = self.saveJsonFile(self.jsonContent)
            self.dataChanged = True
            self.Close()

        if id == const.UI_OPTION_END_CANCEL:
            self.Close()

        return True

    def CreateLayout(self):
        self.SetTitle('Config')
        #Redshift
        if self.GroupBegin(const.GRP_TAB_CORONA_GRP, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 1, 200, "Corona"):
            if self.ScrollGroupBegin(const.GRP_TAB_CORONA_SCROLL_OPT, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, c4d.SCROLLGROUP_VERT, 0, 0):
                if self.GroupBegin(const.GRP_OPT_TAB_CORONA, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 1, 200, "Corona"):
                    self.createCoronaCheckBox(self)
                self.GroupEnd()
            self.GroupEnd()
        self.GroupEnd()

        if self.GroupBegin(const.LIGHT_LISTER_CORONA_OPTIONS_START, c4d.BFH_CENTER | c4d.BFV_CENTER, 100, 100):
            self.GroupBorderSpace(30, 5, 0, 2)

            self.AddButton(const.UI_OPTION_END_OK, c4d.BFH_CENTER | c4d.BFV_TOP, 0, 20, "Ok ")
            self.AddButton(const.UI_OPTION_END_CANCEL, c4d.BFH_CENTER | c4d.BFV_TOP, 0, 20, "Cancel")

        self.GroupEnd()

        return True
