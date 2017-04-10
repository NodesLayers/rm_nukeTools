import os, nuke


def readInPlates():
    
    try:
        ## Find showPath
        curPath = os.path.dirname(nuke.root().name())
        curPath = os.path.splitunc(curPath)
        curPath = os.path.splitdrive(curPath[1])
        ## Create showPath
        mount = curPath[0]
        show = str.split(curPath[1], "/")[1]
        showPath = os.path.normpath(mount+"/"+show)    
    except:
        print "Couldn't find show path..."
     

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


    ##     Plate Folder
    plateFolder = showPath+"/source/plates/"+sequence+"/"+sequence+"_"+shot
    plateFolder = os.path.normpath(plateFolder)    


    ## Import all readable data
    for root, dirs, files in os.walk(plateFolder):
        for dir in dirs:
                readLabel = dir
                print readLabel
                dir = os.path.join(root, dir)
                files = nuke.getFileNameList(dir)
                for seq in files:
                    if seq != 'Thumbs.db' and seq != '' :
                        try:
                            frames, end = seq.split('-')
                            frames, start = frames.split(' ')
                            end = int(end)
                            start = int(start)
                            path = os.path.join(dir, frames)
                            path = path.replace("\\","/")
                            nodename = frames[:-9]
                            # print "nodename : %s" %(nodename)
                            # print "frames : %s" %(path)
                            # print "start : %s" %(start)
                            # print "end : %s"  %(end)
                            fileNode = nuke.nodes.Read(file="%s" %(path),name=nodename)
                            fileNode.knob("first").setValue(start)
                            fileNode.knob("last").setValue(end)
                            fileNode.knob("on_error").setValue(3)
                            fileNode.knob("label").setValue(readLabel)
                            fileNode.knob("note_font").setValue("bold")
                        except ValueError:
                            break