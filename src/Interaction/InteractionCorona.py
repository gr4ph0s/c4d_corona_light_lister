import c4d

from ..Const import Const
from InteractionFunction import InteractionFunction

const = Const()
ifc = InteractionFunction()

class InteractionCorona(InteractionFunction):
    def corona_interaction(self, dialog, doc, clicked_id, msg, light_list, layers):
        #Order
        self.order_interaction_up(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_ORDER_UP, clicked_id, light_list)
        self.order_interaction_down(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_ORDER_DOWN, clicked_id, light_list)

        #Select
        self.selection_interaction(doc, const.LIGHT_LISTER_CORONA_SELECT, clicked_id, msg, light_list)

        #Name
        self.name_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_NAME, clicked_id, light_list)

        #Viewport Change
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_ENABLE_VIEWPORT,
                              clicked_id, light_list, c4d.ID_BASEOBJECT_VISIBILITY_EDITOR)

        #Render Change
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_ENABLE_RENDER,
                              clicked_id, light_list, c4d.ID_BASEOBJECT_VISIBILITY_RENDER)

        #Name
        self.name_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_NAME, clicked_id, light_list)

        #Light Type
        self.long_interaction_type_corona(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_TYPE, clicked_id, light_list)

        #Light Shape
        self.long_interaction_shape_corona(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_SHAPE,
                                     clicked_id, light_list)

        #Size X
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_SIZE_X,
                               clicked_id, light_list, c4d.CORONA_LIGHT_SIZE_X)

        #Size Y
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Y,
                               clicked_id, light_list, c4d.CORONA_LIGHT_SIZE_Y)

        #Size Z
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_SIZE_Z,
                               clicked_id, light_list, c4d.CORONA_LIGHT_SIZE_Z)

        #Segments
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_SEGMENTS,
                              clicked_id, light_list, c4d.CORONA_LIGHT_SEGMENTS)

        #Directionality
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_DIRECTIONALITY,
                               clicked_id, light_list, c4d.CORONA_LIGHT_DIRECTIONALITY)

        #Radius
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_RADIUS,
                               clicked_id, light_list, c4d.CORONA_LIGHT_RADIUS)

        #Render Perfect
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_RENDER_PERFECT,
                              clicked_id, light_list, c4d.CORONA_LIGHT_RENDER_PERFECT)

        #Radius
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_ANGLE,
                               clicked_id, light_list, c4d.CORONA_LIGHT_ANGLE)

        #Radius
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_LENGTH,
                               clicked_id, light_list, c4d.CORONA_LIGHT_LENGTH)

        #bidirectional
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_BIDIRECTIONAL,
                              clicked_id, light_list, c4d.CORONA_LIGHT_BIDIRECTIONAL)

        #Light Color / temperature
        self.color_temp_corona_interaction(dialog, doc,
                                           const.LIGHT_LISTER_CORONA_LIGHT_COLOR,
                                           const.LIGHT_LISTER_CORONA_LIGHT_TEMP,
                                           clicked_id, light_list)

        #mult
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_MULT,
                              clicked_id, light_list, c4d.CORONA_LIGHT_MULTIPLIER)

        #Visible direct
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_DIRECT,
                              clicked_id, light_list, c4d.CORONA_LIGHT_VISIBLE_DIRECT)

        #Visible reflect
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_REFLECT,
                              clicked_id, light_list, c4d.CORONA_LIGHT_VISIBLE_REFLECT)

        #Visible refract
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_REFRACT,
                              clicked_id, light_list, c4d.CORONA_LIGHT_VISIBLE_REFRACT)

        #Occlude in shadow
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_SHADOW,
                              clicked_id, light_list, c4d.CORONA_LIGHT_VISIBLE_SHADOW)

        #Visible in edtior
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_EDITOR,
                              clicked_id, light_list, c4d.CORONA_LIGHT_VISIBLE_EDITOR)

        #layer
        self.layer_interaction(dialog, doc, const.LIGHT_LISTER_CORONA_LIGHT_LAYERS,
                               clicked_id, light_list, layers)

        self.disable_corona_data(dialog, light_list, layers, clicked_id)

    def disable_corona_data(self, dialog, light_list, layers, clicked_id):
        for i in xrange(len(light_list)):
            ui_id = const.LIGHT_LISTER_CORONA_LIGHT_SHAPE
            if not ui_id <= clicked_id < ui_id + const.STEP:
                light_type = dialog.GetLong(const.LIGHT_LISTER_CORONA_LIGHT_TYPE + i + 2)
                value = dialog.GetLong(const.LIGHT_LISTER_CORONA_LIGHT_SHAPE + i + 2)
                if light_type == 0:
                    dialog.FreeChildren(const.LIGHT_LISTER_CORONA_LIGHT_SHAPE + i + 2)
                    dialog.AddChild(const.LIGHT_LISTER_CORONA_LIGHT_SHAPE + i + 2, 0, "Rectangle")
                    dialog.AddChild(const.LIGHT_LISTER_CORONA_LIGHT_SHAPE + i + 2, 1, "Circle")

                elif light_type == 1:
                    dialog.FreeChildren(const.LIGHT_LISTER_CORONA_LIGHT_SHAPE + i + 2)
                    dialog.AddChild(const.LIGHT_LISTER_CORONA_LIGHT_SHAPE + i + 2, 10, "Sphere Sector")

                elif light_type == 2:
                    dialog.FreeChildren(const.LIGHT_LISTER_CORONA_LIGHT_SHAPE + i + 2)
                    dialog.AddChild(const.LIGHT_LISTER_CORONA_LIGHT_SHAPE + i + 2, 20, "Sphere")
                    dialog.AddChild(const.LIGHT_LISTER_CORONA_LIGHT_SHAPE + i + 2, 21, "Cube")
                    dialog.AddChild(const.LIGHT_LISTER_CORONA_LIGHT_SHAPE + i + 2, 22, "Cylinder")

                dialog.SetLong(const.LIGHT_LISTER_CORONA_LIGHT_SHAPE + i + 2, value)

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