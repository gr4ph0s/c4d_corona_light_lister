import c4d
from ..Const import Const
from .JsonFunction import JsonFunction

const = Const()


class ConfigManagerCorona(JsonFunction):
    def createCoronaCheckBox(self, dialog):
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_ENABLE_VIEWPORT,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Enable Viewport")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_ENABLE_RENDER,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Enable Render")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_TYPE,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Light Type")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_AREA,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Light Shape")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SIZE_X,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Size X")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SIZE_Y,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Size Y")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SIZE_Z,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Size Z")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SEGMENTS,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Segments")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_DIRECTIONALITY,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Directionality")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_RADIUS,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Radius")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_RENDER_PERFECT,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Render Perfect")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_ANGLE,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Angle")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_LENGTH,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Lengh")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_BIDIRECTIONAL,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Bidirectional")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_COLOR,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Color")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_TEMP,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Temperature")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_MULT,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Multiplier")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_DIRECT,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Visible directly")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_REFLECT,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Visible reflect")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_REFRACT,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Visible refract")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SHADOW,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Occlude other lights")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_EDITOR,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Visible in Editor")
        dialog.AddCheckbox(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_LAYERS,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Layer")

        self.fillCoronaCheckBox(dialog)

    def fillCoronaCheckBox(self, dialog):
        self.jsonContent = self.loadJsonFile()
        self.coronaConfig = self.jsonContent["corona"]

        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_ENABLE_VIEWPORT, self.coronaConfig["EnableViewport"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_ENABLE_RENDER, self.coronaConfig["EnableRender"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_TYPE, self.coronaConfig["LightType"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_AREA, self.coronaConfig["LightShape"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SIZE_X, self.coronaConfig["SizeX"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SIZE_Y, self.coronaConfig["SizeY"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SIZE_Z, self.coronaConfig["SizeZ"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SEGMENTS, self.coronaConfig["Segments"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_DIRECTIONALITY, self.coronaConfig["Directionality"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_RADIUS, self.coronaConfig["Radius"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_RENDER_PERFECT, self.coronaConfig["RenderPerfect"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_ANGLE, self.coronaConfig["Angle"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_LENGTH, self.coronaConfig["Lengh"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_BIDIRECTIONAL, self.coronaConfig["Bidirectional"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_COLOR, self.coronaConfig["Color"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_TEMP, self.coronaConfig["Temperature"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_MULT, self.coronaConfig["Multiplier"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_DIRECT, self.coronaConfig["Visibledirectly"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_REFLECT, self.coronaConfig["Visiblereflect"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_REFRACT, self.coronaConfig["Visiblerefract"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SHADOW, self.coronaConfig["Occludeotherlights"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_EDITOR, self.coronaConfig["VisibleinEditor"])
        dialog.SetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_LAYERS, self.coronaConfig["Layer"])

    def generateCoronajson(self, dialog):
        corona = {}
        corona["EnableViewport"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_ENABLE_VIEWPORT)
        corona["EnableRender"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_ENABLE_RENDER)
        corona["LightType"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_TYPE)
        corona["LightShape"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_AREA)
        corona["SizeX"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SIZE_X)
        corona["SizeY"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SIZE_Y)
        corona["SizeZ"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SIZE_Z)
        corona["Segments"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SEGMENTS)
        corona["Directionality"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_DIRECTIONALITY)
        corona["Radius"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_RADIUS)
        corona["RenderPerfect"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_RENDER_PERFECT)
        corona["Angle"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_ANGLE)
        corona["Lengh"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_LENGTH)
        corona["Bidirectional"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_BIDIRECTIONAL)
        corona["Color"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_COLOR)
        corona["Temperature"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_TEMP)
        corona["Multiplier"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_MULT)
        corona["Visibledirectly"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_DIRECT)
        corona["Visiblereflect"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_REFLECT)
        corona["Visiblerefract"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_REFRACT)
        corona["Occludeotherlights"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SHADOW)
        corona["VisibleinEditor"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_EDITOR)
        corona["Layer"] = dialog.GetBool(const.LIGHT_LISTER_CORONA_OPTIONS_LIGHT_LAYERS)

        self.jsonContent["corona"] = corona