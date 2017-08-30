import c4d

from ..Const import Const
from CreationFunction import CreationFunction

const = Const()

class CreationCorona(CreationFunction):
    def refresh_corona_light(self, dialog, list_lights):
        save_light = dialog.GetVisibleArea(const.GRP_TAB_CORONA_SCROLL_LIGHT)

        #Name
        self.create_edit_string(dialog, const.LIGHT_LISTER_CORONA_NAME,
                                "Name", const.OBJ, list_lights, True)

        try:
            current_light = dialog.GetVisibleArea(const.GRP_TAB_CORONA_SCROLL_LIGHT)
            decalage = save_light["x2"] - current_light["x2"]
            size_x = current_light["x2"] - current_light["x1"]
            if decalage > 0 and current_light["x1"] < size_x :
                decalage = 0 - decalage
            dialog.SetVisibleArea(const.GRP_TAB_CORONA_SCROLL_LIGHT,
                                  current_light["x1"] + decalage,
                                  current_light["y1"],
                                  current_light["x2"] + decalage,
                                  current_light["y2"]
                                  )
        except:
            pass




    def create_corona_light(self, dialog, config, light_list, layers):
        if not len(light_list):
            return


        dialog.ScrollGroupBegin(const.GRP_TAB_CORONA_SCROLL_NAME, c4d.BFH_LEFT | c4d.BFV_SCALEFIT, c4d.SCROLLGROUP_VERT | c4d.SCROLLGROUP_LEFT | c4d.SCROLLGROUP_AUTOVERT, 0, 0)
        if dialog.GroupBegin(const.GRP_TAB_CORONA_GRP, c4d.BFH_LEFT | c4d.BFV_SCALEFIT, 300, 200, "Corona"):
            dialog.GroupBorderSpace(0, 0, 10, 15)

            self.create_min_max_button(dialog, const.LIGHT_LISTER_CORONA_LIGHT_ORDER_GRP, const.LIGHT_LISTER_CORONA_LIGHT_ORDER_UP, const.LIGHT_LISTER_CORONA_LIGHT_ORDER_DOWN, light_list)

            #select
            self.create_button(dialog, const.LIGHT_LISTER_CORONA_SELECT,
                             "Select", "S", light_list)

            #Name
            self.create_edit_string(dialog, const.LIGHT_LISTER_CORONA_NAME,
                                  "Name", const.OBJ, light_list)

            self.create_enable(dialog, const.LIGHT_LISTER_CORONA_LIGHT_ENABLE, light_list)

        dialog.GroupEnd()
        dialog.GroupEnd()


        dialog.ScrollGroupBegin(const.GRP_TAB_CORONA_SCROLL_LIGHT, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, c4d.SCROLLGROUP_HORIZ | c4d.SCROLLGROUP_VERT, 0, 0)
        if dialog.GroupBegin(const.GRP_TAB_CORONA_GRP, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 300, 200, "Corona"):

            #visibility viewport
            if config["EnableViewport"]:
                buffer = [{"id": 2, "text": "Default"},
                          {"id": 0, "text": "On"},
                          {"id": 1, "text": "Off"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_CORONA_ENABLE_VIEWPORT,
                                       "Viewport", buffer, const.OBJ, light_list, c4d.ID_BASEOBJECT_VISIBILITY_EDITOR)

            #Visibility render
            if config["EnableRender"]:
                buffer = [{"id": 2, "text": "Default"},
                          {"id": 0, "text": "On"},
                          {"id": 1, "text": "Off"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_CORONA_ENABLE_RENDER,
                                       "Render", buffer, const.OBJ, light_list, c4d.ID_BASEOBJECT_VISIBILITY_RENDER)

            #Light color
            if config["Color"]:
                self.create_color_field(dialog, const.LIGHT_LISTER_CORONA_LIGHT_COLOR,
                                      "Color", const.OBJ, light_list, c4d.CORONA_LIGHT_COLOR)

            #Temp
            if config["Temperature"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_CORONA_LIGHT_TEMP,
                                    "Temp", const.INT_MODE, const.OBJ, light_list, c4d.CORONA_LIGHT_TEMPERATURE, 1000.0, 25000)

            #Light type
            if config["LightType"]:
                buffer = [{"id": 0, "text": "Area"},
                          {"id": 1, "text": "Sector"},
                          {"id": 2, "text": "Object"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_CORONA_LIGHT_TYPE,
                                       "Light Type", buffer, const.OBJ, light_list, c4d.CORONA_LIGHT_TYPE)

            if config["LightShape"]:
                self.create_cycle_button_corona(dialog, const.LIGHT_LISTER_CORONA_LIGHT_SHAPE,
                                                "Light Shape", light_list)

            #Size X
            if config["SizeX"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_CORONA_LIGHT_SIZE_X,
                                    "Size X", const.METER_MODE, const.OBJ, light_list, c4d.CORONA_LIGHT_SIZE_X, 0, 2147483647)

            #Size Y
            if config["SizeY"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Y,
                                    "Size Y", const.METER_MODE, const.OBJ, light_list, c4d.CORONA_LIGHT_SIZE_Y, 0, 2147483647)

            #Size Z
            if config["SizeZ"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Z,
                                    "Size Z", const.METER_MODE, const.OBJ, light_list, c4d.CORONA_LIGHT_SIZE_Z, 0, 2147483647)

            #Segments
            if config["Segments"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_CORONA_LIGHT_SEGMENTS,
                                    "Segments", const.INT_MODE, const.OBJ, light_list, c4d.CORONA_LIGHT_SEGMENTS, 3, 2147483647)

            #Directionality
            if config["Directionality"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_CORONA_LIGHT_DIRECTIONALITY,
                                    "Directionality", const.PERCENT_MODE, const.OBJ, light_list, c4d.CORONA_LIGHT_DIRECTIONALITY, 0.0, 100.0)

            #Radius
            if config["Radius"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_CORONA_LIGHT_RADIUS,
                                    "Radius", const.METER_MODE, const.OBJ, light_list, c4d.CORONA_LIGHT_RADIUS, 0, 2147483647)

            #Render perfect
            if config["RenderPerfect"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_CORONA_LIGHT_RENDER_PERFECT,
                                   "Render perfect", const.OBJ, light_list, c4d.CORONA_LIGHT_RENDER_PERFECT)

            #Angle
            if config["Angle"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_CORONA_LIGHT_ANGLE,
                                    "Angle", const.DEGREE_MODE, const.OBJ, light_list, c4d.CORONA_LIGHT_ANGLE, 0, 360)

            #Lengh
            if config["Lengh"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_CORONA_LIGHT_LENGTH,
                                    "Lengh", const.METER_MODE, const.OBJ, light_list, c4d.CORONA_LIGHT_LENGTH, 0, 2147483647)

            #Bidirectional
            if config["Bidirectional"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_CORONA_LIGHT_BIDIRECTIONAL,
                                   "Bidirectional", const.OBJ, light_list, c4d.CORONA_LIGHT_BIDIRECTIONAL)

            #Mult
            if config["Multiplier"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_CORONA_LIGHT_MULT,
                                    "Mult", const.INT_MODE, const.OBJ, light_list, c4d.CORONA_LIGHT_MULTIPLIER, 0.0, 9999)

            #Visible directly
            if config["Visibledirectly"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_CORONA_LIGHT_DIRECT,
                                   "Visible directly", const.OBJ, light_list, c4d.CORONA_LIGHT_VISIBLE_DIRECT)

            #Visible directly
            if config["Visiblereflect"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_CORONA_LIGHT_REFLECT,
                                   "Visible reflections", const.OBJ, light_list, c4d.CORONA_LIGHT_VISIBLE_REFLECT)

            #Visible directly
            if config["Visiblerefract"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_CORONA_LIGHT_REFRACT,
                                   "Visible refract", const.OBJ, light_list, c4d.CORONA_LIGHT_VISIBLE_REFRACT)

            #Visible directly
            if config["Occludeotherlights"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_CORONA_LIGHT_SHADOW,
                                   "Occlude other lights", const.OBJ, light_list, c4d.CORONA_LIGHT_VISIBLE_SHADOW)
            #Visible directly
            if config["VisibleinEditor"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_CORONA_LIGHT_EDITOR,
                                   "Visible in Editor", const.OBJ, light_list, c4d.CORONA_LIGHT_VISIBLE_EDITOR)

            #Layers
            if config["Layer"]:
                buffer = list()
                buffer.append({"id": 0, "text": "None"})
                for i in xrange(len(layers)):
                    buffer.append({"id": i+1, "text": layers[i].GetName()})

                self.create_cycle_button(dialog, const.LIGHT_LISTER_CORONA_LIGHT_LAYERS,
                                       "Layer", buffer, const.OBJ, light_list, layers=layers)

        dialog.GroupEnd()
        dialog.GroupEnd()

        self.disable_corona_data(dialog, light_list, layers)


    def disable_corona_data(self, dialog, light_list, layers):
        for i in xrange(len(light_list)):
            light_shape = dialog.GetLong(const.LIGHT_LISTER_CORONA_LIGHT_SHAPE + i + 2)
            #Rectangle
            if light_shape == 0:
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_X + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Y + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_DIRECTIONALITY + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_BIDIRECTIONAL + i + 2, True)

                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Z + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SEGMENTS + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_RADIUS + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_RENDER_PERFECT + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_ANGLE + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_LENGTH + i + 2, False)

            #Circle
            elif light_shape == 1:
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_RADIUS + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SEGMENTS + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_DIRECTIONALITY + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_BIDIRECTIONAL + i + 2, True)

                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_X + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Y + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Z + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_RENDER_PERFECT + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_ANGLE + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_LENGTH + i + 2, False)

            #Sphere Sector
            elif light_shape == 10:
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_ANGLE + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_RADIUS + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SEGMENTS + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_DIRECTIONALITY + i + 2, True)

                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_X + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Y + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Z + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_RENDER_PERFECT + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_LENGTH + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_BIDIRECTIONAL + i + 2, False)

            #Object Sphere
            elif light_shape == 20:
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_RADIUS + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SEGMENTS + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_RENDER_PERFECT + i + 2, True)

                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_X + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Y + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Z + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_DIRECTIONALITY + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_ANGLE + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_LENGTH + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_BIDIRECTIONAL + i + 2, False)

            #Object Cube
            elif light_shape == 21:
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_X + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Y + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Z + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_DIRECTIONALITY + i + 2, True)

                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SEGMENTS + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_RADIUS + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_RENDER_PERFECT + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_ANGLE + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_LENGTH + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_BIDIRECTIONAL + i + 2, False)

            #Object Cynlinder
            elif light_shape == 22:
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_RADIUS + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_LENGTH + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SEGMENTS + i + 2, True)

                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_X + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Y + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Z + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_DIRECTIONALITY + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_RENDER_PERFECT + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_ANGLE + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_BIDIRECTIONAL + i + 2, False)

            if not len(layers):
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_LAYERS + i + 2, False)
            else:
                dialog.Enable(const.LIGHT_LISTER_CORONA_LIGHT_LAYERS + i + 2, True)
