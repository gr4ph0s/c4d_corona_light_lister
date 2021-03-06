class Const(object):
    PLUGIN_ID           = 1039166
    PLUGIN_ID_TAG       = 1039167
    VERSION             = 1.2

    #===========================================================================================================#
    #                                                                                                           #
    #                                            LIGHT TAG ID                                                   #
    #                                                                                                           #
    #===========================================================================================================#
    TAG_ID_OCTANE = 1029526
    TAG_ID_ARNOLD = 1029989
    TAG_ID_VRAY = 1020441
    LIGHT_C4D_ID = 5102
    LIGHT_ID_REDSHIFT = 1036751
    LIGHT_ID_ARNOLD = 1030424
    LIGHT_ID_CORONA = 1032104

    STEP                = 202
    RENDER_STEP         = 10000

    CORONA_RENDER       = 5

    INT_MODE            = 0
    PERCENT_MODE        = 1
    METER_MODE          = 2
    FLOAT_MODE          = 3
    DEGREE_MODE         = 4

    TAG = 0
    OBJ = 1

    #===========================================================================================================#
    #                                                                                                           #
    #                                                   UI ID                                                   #
    #                                                                                                           #
    #===========================================================================================================#
    UI_BTN_OPTION = 100001
    UI_OPTION_END_OK = 100002
    UI_OPTION_END_CANCEL = 100003
    UI_OPTION_END = 100004

    GRP_MAIN = 100018
    GRP_TAB = 100019

    GRP_TAB_CORONA = 100040
    GRP_TAB_CORONA_SCROLL_NAME = 100041
    GRP_TAB_CORONA_SCROLL_LIGHT = 100042
    GRP_TAB_CORONA_SCROLL_OPT = 100043
    GRP_TAB_CORONA_GRP = 100044

    GRP_OPT_TAB_CORONA = 100083

    #Corona LightLister ID
    if bool(1):
        LIGHT_LISTER_CORONA_START                       = CORONA_RENDER * RENDER_STEP + STEP * 0
        LIGHT_LISTER_CORONA_SELECT                      = CORONA_RENDER * RENDER_STEP + STEP * 1
        LIGHT_LISTER_CORONA_ENABLE_VIEWPORT             = CORONA_RENDER * RENDER_STEP + STEP * 2
        LIGHT_LISTER_CORONA_ENABLE_RENDER               = CORONA_RENDER * RENDER_STEP + STEP * 3
        LIGHT_LISTER_CORONA_NAME                        = CORONA_RENDER * RENDER_STEP + STEP * 4
        LIGHT_LISTER_CORONA_LIGHT_TYPE                  = CORONA_RENDER * RENDER_STEP + STEP * 5
        LIGHT_LISTER_CORONA_LIGHT_SHAPE                 = CORONA_RENDER * RENDER_STEP + STEP * 6

        LIGHT_LISTER_CORONA_LIGHT_SIZE_X                = CORONA_RENDER * RENDER_STEP + STEP * 7
        LIGHT_LISTER_CORONA_LIGHT_SIZE_Y                = CORONA_RENDER * RENDER_STEP + STEP * 8
        LIGHT_LISTER_CORONA_LIGHT_SIZE_Z                = CORONA_RENDER * RENDER_STEP + STEP * 9
        LIGHT_LISTER_CORONA_LIGHT_SEGMENTS              = CORONA_RENDER * RENDER_STEP + STEP * 10
        LIGHT_LISTER_CORONA_LIGHT_DIRECTIONALITY        = CORONA_RENDER * RENDER_STEP + STEP * 11
        LIGHT_LISTER_CORONA_LIGHT_RADIUS                = CORONA_RENDER * RENDER_STEP + STEP * 12
        LIGHT_LISTER_CORONA_LIGHT_RENDER_PERFECT        = CORONA_RENDER * RENDER_STEP + STEP * 13
        LIGHT_LISTER_CORONA_LIGHT_ANGLE                 = CORONA_RENDER * RENDER_STEP + STEP * 14
        LIGHT_LISTER_CORONA_LIGHT_LENGTH                = CORONA_RENDER * RENDER_STEP + STEP * 15

        LIGHT_LISTER_CORONA_LIGHT_BIDIRECTIONAL         = CORONA_RENDER * RENDER_STEP + STEP * 16
        LIGHT_LISTER_CORONA_LIGHT_COLOR_ENABLE          = CORONA_RENDER * RENDER_STEP + STEP * 17
        LIGHT_LISTER_CORONA_LIGHT_COLOR                 = CORONA_RENDER * RENDER_STEP + STEP * 18
        LIGHT_LISTER_CORONA_LIGHT_TEMP_ENABLE           = CORONA_RENDER * RENDER_STEP + STEP * 19
        LIGHT_LISTER_CORONA_LIGHT_TEMP                  = CORONA_RENDER * RENDER_STEP + STEP * 20
        LIGHT_LISTER_CORONA_LIGHT_MULT                  = CORONA_RENDER * RENDER_STEP + STEP * 21
        LIGHT_LISTER_CORONA_LIGHT_DIRECT                = CORONA_RENDER * RENDER_STEP + STEP * 22
        LIGHT_LISTER_CORONA_LIGHT_REFLECT               = CORONA_RENDER * RENDER_STEP + STEP * 23
        LIGHT_LISTER_CORONA_LIGHT_REFRACT               = CORONA_RENDER * RENDER_STEP + STEP * 24
        LIGHT_LISTER_CORONA_LIGHT_SHADOW                = CORONA_RENDER * RENDER_STEP + STEP * 25
        LIGHT_LISTER_CORONA_LIGHT_EDITOR                = CORONA_RENDER * RENDER_STEP + STEP * 26
        LIGHT_LISTER_CORONA_LIGHT_LAYERS                = CORONA_RENDER * RENDER_STEP + STEP * 27

        LIGHT_LISTER_CORONA_LIGHT_ENABLE                = CORONA_RENDER * RENDER_STEP + STEP * 28
        LIGHT_LISTER_CORONA_LIGHT_ORDER_GRP             = CORONA_RENDER * RENDER_STEP + STEP * 29
        LIGHT_LISTER_CORONA_LIGHT_ORDER_UP              = CORONA_RENDER * RENDER_STEP + STEP * 30
        LIGHT_LISTER_CORONA_LIGHT_ORDER_DOWN            = CORONA_RENDER * RENDER_STEP + STEP * 31

        LIGHT_LISTER_CORONA_LIGHT_END                   = CORONA_RENDER * RENDER_STEP + STEP * 32

    #Corona Option LightLister ID
    if bool(1):
        LIGHT_LISTER_CORONA_OPTIONS_START                       = LIGHT_LISTER_CORONA_LIGHT_END + 1
        LIGHT_LISTER_CORONA_OPTIONS_SELECT                      = LIGHT_LISTER_CORONA_LIGHT_END + 2
        LIGHT_LISTER_CORONA_OPTIONS_ENABLE_VIEWPORT             = LIGHT_LISTER_CORONA_LIGHT_END + 3
        LIGHT_LISTER_CORONA_OPTIONS_ENABLE_RENDER               = LIGHT_LISTER_CORONA_LIGHT_END + 4
        LIGHT_LISTER_CORONA_OPTIONS_NAME                        = LIGHT_LISTER_CORONA_LIGHT_END + 5
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_TYPE                  = LIGHT_LISTER_CORONA_LIGHT_END + 6
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_AREA                  = LIGHT_LISTER_CORONA_LIGHT_END + 7

        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SIZE_X                = LIGHT_LISTER_CORONA_LIGHT_END + 8
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SIZE_Y                = LIGHT_LISTER_CORONA_LIGHT_END + 9
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SIZE_Z                = LIGHT_LISTER_CORONA_LIGHT_END + 10
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SEGMENTS              = LIGHT_LISTER_CORONA_LIGHT_END + 11
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_DIRECTIONALITY        = LIGHT_LISTER_CORONA_LIGHT_END + 12
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_RADIUS                = LIGHT_LISTER_CORONA_LIGHT_END + 13
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_RENDER_PERFECT        = LIGHT_LISTER_CORONA_LIGHT_END + 14
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_ANGLE                 = LIGHT_LISTER_CORONA_LIGHT_END + 15
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_LENGTH                 = LIGHT_LISTER_CORONA_LIGHT_END + 16

        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_BIDIRECTIONAL         = LIGHT_LISTER_CORONA_LIGHT_END + 17
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_COLOR_ENABLE          = LIGHT_LISTER_CORONA_LIGHT_END + 18
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_COLOR                 = LIGHT_LISTER_CORONA_LIGHT_END + 19
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_TEMP_ENABLE           = LIGHT_LISTER_CORONA_LIGHT_END + 20
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_TEMP                  = LIGHT_LISTER_CORONA_LIGHT_END + 21
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_MULT                  = LIGHT_LISTER_CORONA_LIGHT_END + 22
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_DIRECT                = LIGHT_LISTER_CORONA_LIGHT_END + 23
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_REFLECT               = LIGHT_LISTER_CORONA_LIGHT_END + 24
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_REFRACT               = LIGHT_LISTER_CORONA_LIGHT_END + 25
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_SHADOW                = LIGHT_LISTER_CORONA_LIGHT_END + 26
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_EDITOR                = LIGHT_LISTER_CORONA_LIGHT_END + 27
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_LAYERS                = LIGHT_LISTER_CORONA_LIGHT_END + 28
        LIGHT_LISTER_CORONA_OPTIONS_LIGHT_END                   = LIGHT_LISTER_CORONA_LIGHT_END + 29
