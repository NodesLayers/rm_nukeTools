import nuke
import os



def setWriteNode():

	n = nuke.selectedNode()
	
	
	if nuke.root().name() == "Root":
		nuke.message("You need to save your script properly before continuing!")
		
	if n.Class() != "Write":
		nuke.message("This only works on Write nodes... duh...!")
		
		


	## Find sequence, shot & assetName from Nuke scriptName
	try:
		scriptInfo = os.path.basename(nuke.root().name()) #Nuke filename
		#scriptInfo = os.path.normcase(scriptInfo) #Lowercase + forward slash
		scriptInfo = str.split(scriptInfo,"_")
		# Set Script Variables
		sequence = str.upper(scriptInfo[0])
		print "Sequence is: "+sequence
		shot = scriptInfo[1]
		print "Shot is: "+shot
		assetName = scriptInfo[2]
		print "Asset name is: "+assetName
		taskName = scriptInfo[3]
		print "Task name is: "+taskName
	except:
		print "Couldn't find Sequence, Shot, Assetname and Taskname"


	#Set Basepath
	if os.name == "nt":
		basepath = "//192.168.50.10/FilmShare/"
	elif os.name == "posix":
		basepath = "/Volumes/FilmShare/"
	print "Basepath for this OS: "+basepath


	#Find scriptVersion
	scriptVersion = nuke.root().name()
	scriptVersion = str.split(scriptVersion,"_")
	scriptVersion = scriptVersion[-1]
	scriptVersion = str.split(scriptVersion,".")
	scriptVersion = scriptVersion[0]
	print "Found Nuke script version to be "+scriptVersion


	## PANEL
	p = nuke.Panel('Set Write Node')    
	p.addEnumerationPulldown('Show:', "RPO_01")
	p.addEnumerationPulldown('Vendor:', 'DD ILM')
	p.addEnumerationPulldown('Context:', 'shot library plate')
	p.addEnumerationPulldown('Layer Type:', 'GFX slapcomp_MOV slapcomp_EXR')
	p.addSingleLineInput('Layer:', '')
	p.addEnumerationPulldown('mergeOp:', 'over plus screen atop average color-burn color-dodge conjoint-over copy difference disjoint-over divide exclusion from geometric hard-light hypot in mask matte max min minus multiply out overlay soft-light stencil under xor')



	ret = p.show()




	## Set User Variables
	show = p.value("Show:")
	vendor = p.value("Vendor:")
	context = p.value("Context:")
	layerType = p.value("Layer Type:")
	layer = p.value("Layer:")
	mergeOp = p.value("mergeOp:")



	## Set WriteNode
	n = nuke.selectedNode()
	n = nuke.toNode(n.name())


	if context != "plate":	
		#### Basepath for Shotgun Export
		baseFolder = basepath+show+"/sequences/"+sequence+"/"+sequence+"_"+shot+"/aftereffects/__aep/__OUTPUT/export/"+sequence+"_"+shot+"_"+assetName+"_"+taskName+"_"+scriptVersion




	#### FILE PROFILES

	if vendor == "DD":
		if context == "shot":
			if layerType == "GFX":
				writeFile = baseFolder+"/"+layer+"/"+sequence+"_"+shot+"_"+assetName+"_"+taskName+"_layer_"+layer+"_"+mergeOp+"_"+scriptVersion+".%04d.exr"
			
			if layerType == "slapcomp_MOV":
				writeFile = baseFolder+"/_MOV/"+sequence+"_"+shot+"_"+assetName+"_"+taskName+"_slapcomp_"+scriptVersion+".mov"
				
			if layerType == "slapcomp_EXR":
				writeFile = baseFolder+"/_EXR/"+sequence+"_"+shot+"_"+assetName+"_"+taskName+"_slapcomp_"+scriptVersion+".%04d.exr"
				
		
        if context == "library":
            if layerType == "GFX":
                writeFile = basepath+show+"/assets/"+assetName+"/aftereffects/"+taskName+"/__aep/__OUTPUT/export/"
                writeFile = writeFile+assetName+"_"+taskName+"_"+scriptVersion+"/"+layer+"/library00gfx_"+assetName+"_"+taskName+"_slapcomp_"+scriptVersion+".#.exr"

            if layerType == "slapcomp_MOV":
                writeFile = basepath+show+"/assets/"+assetName+"/aftereffects/"+taskName+"/__aep/__OUTPUT/export/"
                writeFile = writeFile+assetName+"_"+taskName+"_"+scriptVersion+"/_MOV/library00gfx_"+assetName+"_"+taskName+"_slapcomp_"+scriptVersion+".mov"
                    
            if layerType == "slapcomp_EXR":
                writeFile = basepath+show+"/assets/"+assetName+"/aftereffects/"+taskName+"/__aep/__OUTPUT/export/"
                writeFile = writeFile+assetName+"_"+taskName+"_"+scriptVersion+"/_EXR/library00gfx_"+assetName+"_"+taskName+"_slapcomp_"+scriptVersion+".#.exr"
					
					
	if vendor == "ILM":
		if context == "shot":
			if layerType == "GFX":
				writeFile = baseFolder+"/"+sequence+shot+"/graphicsLayers/"+layer+"/"+sequence+"."+shot+"."+assetName+"."+taskName+".layer."+layer+"."+mergeOp+"."+scriptVersion+".%04d.exr"
			
			if layerType == "slapcomp_MOV":
				writeFile = baseFolder+"/"+sequence+shot+"/graphicsLayers/comped/"+sequence+"."+shot+"."+assetName+"."+taskName+".slapcomp."+scriptVersion+".mov"
				
			if layerType == "slapcomp_EXR":
				writeFile = baseFolder+"/"+sequence+shot+"/graphicsLayers/comped/"+sequence+"."+shot+"."+assetName+"."+taskName+".slapcomp."+scriptVersion+".%04d.exr"
				
		
		if context == "library":
			if layerType == "GFX":
				writeFile = basepath+show+"/assets/"+assetName+"/aftereffects/"+taskName+"/__aep/__OUTPUT/export/"
				writeFile = writeFile+assetName+"_"+taskName+"_"+scriptVersion+"/graphicsLayers/"+layer+"/"+sequence+shot+"."+assetName+"."+taskName+".layer."+layer+"."+mergeOp+".gfx."+scriptVersion+".%04d.exr"
				
			if layerType == "slapcomp_MOV":
				writeFile = basepath+show+"/assets/"+assetName+"/aftereffects/"+taskName+"/__aep/__OUTPUT/export/"
				writeFile = writeFile+assetName+"_"+taskName+"_"+scriptVersion+"/graphicsLayers/comped/"+sequence+shot+"."+assetName+"."+taskName+".gfx."+scriptVersion+".mov"
					
			if layerType == "slapcomp_EXR":
				writeFile = basepath+show+"/assets/"+assetName+"/aftereffects/"+taskName+"/__aep/__OUTPUT/export/"
				writeFile = writeFile+assetName+"_"+taskName+"_"+scriptVersion+"/graphicsLayers/comped/"+sequence+shot+"."+assetName+"."+taskName+".gfx."+scriptVersion+".#.exr"
					

	if context == "plate":
		##find topnode name
		n = nuke.selectedNode()
		topnode_name = nuke.tcl("full_name [topnode %s]" % n.name())
		topnode = nuke.toNode(topnode_name)
		print "Found Topnode to be "+topnode.name()
		writeFile = topnode["file"].getValue()
		print "Topnode file: "+writeFile
		writeFile = os.path.dirname(writeFile)
		writeFile = writeFile+".mov"
		n["file"].setValue(writeFile)
		print "Plate write filename: "+writeFile
	
	
	
	## Set writeFile
	n["file"].setValue(writeFile)


	## Codec/Data Profiles
	if (layerType == "GFX") or (layerType == "slapcomp_EXR"):
		n["file_type"].setValue("exr")
		n["datatype"].setValue("16 bit half")
		n["compression"].setValue("Zip (1 scanline)")


	if (layerType == "slapcomp_MOV") or (context == "plate"):
		n["file_type"].setValue("mov")
		n["meta_codec"].setValue("apcn")















