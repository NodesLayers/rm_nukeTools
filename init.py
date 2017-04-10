



nuke.pluginAddPath('./Python')
nuke.pluginAddPath('./T_GizmoMenus')
nuke.pluginAddPath('./Plugins')
nuke.pluginAddPath('./Luts')
nuke.pluginAddPath('./Icons')

######## Import Python Scripts
import CheckOutputPath


########KNOBDEFAULTS

nuke.knobDefault("EXPTool.mode", "0")
nuke.knobDefault("EXPTool.label", "[value mode]")
nuke.knobDefault("Grain2.seed", "[frame]")                                      # removes horrible pattern
nuke.knobDefault("Grain2.maskgrain", "0")                                      
nuke.knobDefault("Text.message", "frame [python '%04d' % nuke.frame()]")   # 4 padded frame number
nuke.knobDefault("Blur.channels","rgba")
nuke.knobDefault("Blur.crop","0")
nuke.knobDefault("Defocus.channels","rgba")
nuke.knobDefault("ZBlur.channels","rgba")
nuke.knobDefault("Read.before", "hold")
nuke.knobDefault("Read.after", "hold")
nuke.knobDefault("Roto.toolbar_autokey", "1")
nuke.knobDefault("Roto.output","rgba")
nuke.knobDefault("Roto.cliptype","no clip")
nuke.knobDefault("RotoPaint.toolbar_autokey", "1")
nuke.knobDefault("RotoPaint.crop","0")
nuke.knobDefault("RotoPaint.cliptype","no clip")
nuke.knobDefault("Write.beforeRender","CheckOutputPath.CheckOutputPath()")
nuke.knobDefault("Viewer.hide_input","1")



####FORMATS

nuke.addFormat("2104 1136 1.0 GITS_cropped_DELVERY_FORMAT_2K")
nuke.addFormat("2104 1184 1.0 GITS_CG_format_2K")
nuke.knobDefault("root.format", "GITS_CG_format_2K")






######terriortory LUTS


nuke.ViewerProcess.register("AlexaV3Rec709_standard", nuke.createNode,("Vectorfield", "vfield_file Y:/_nuke_global_setup/Luts/AlexaV3_EI0800_LogC2Video_Rec709_EE_nuke3d.cube colorspaceIn AlexaV3LogC"))

######terriortory


nuke.ViewerProcess.register("AlexaV3Rec709_GITS", nuke.createNode,("Vectorfield", "vfield_file Y:/_nuke_global_setup/Luts/GHOST_SHED_DAILIES_OT_V1_Rec709_EE.cube colorspaceIn AlexaV3LogC"))





