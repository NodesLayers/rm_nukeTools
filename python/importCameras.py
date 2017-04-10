import nuke
import os

def importCameras():

    try:
        ## nukePath
        nukePath = os.path.dirname(nuke.root().name())
        nukePath = os.path.normpath(nukePath)
        print "nukePath: "+nukePath

        ## nukeScriptName
        nukeScriptName = os.path.basename(nuke.root().name())
        print "nukeScriptName: "+nukeScriptName

        ## drive & showName
        try:
            showPath = os.path.splitdrive(nukePath)
            drive = showPath[0]
            showName = showPath[1]
            showName = str.split(showName, "\\")[1]
            print "Drive: "+drive
            print "showName: "+showName
        except:
            print "Error: drive and showName not found.."
            pass

        ## sequence
        try:
            sequence = str.split(nukeScriptName, "_")[0]
            print "sequence: "+sequence
        except:
            print "Error: sequence not found..."

        ## shot
        try:
            shot = str.split(nukeScriptName, "_")[1]
            print "shot: "+shot
        except:
            print "Error: shot not found..."

        ## camPath
        try:
            camPath = os.path.join(drive, "\\", showName, "source\cameras\\" ,sequence, sequence+"_"+shot)
            camPath = os.path.normpath(camPath)
            print "camPath: "+camPath
            
            flist = []

            ## For each file in the listed directory, check the ext and if it matches, go further and import
            for f in os.listdir(camPath):
                ext = os.path.splitext(f)[-1].lower()
                if ext == ".abc":
                    print f

                    flist.append(f)
        
        except:
            print "Error: An error occured while creating a list of camera(s)..."
            pass
 

        ## Select and import Cam
        try:
            ## PANEL
            p = nuke.Panel('Select Camera')
            p.addEnumerationPulldown('Camera:', flist)
            p.show()
        
        
            selectedCam = p.value("Camera:")
            selectedCam = selectedCam.replace("'", "")
            selectedCam = selectedCam.replace("[", "")
            selectedCam = selectedCam.replace("]", "")
            selectedCam = selectedCam.replace(",", "")
        
        
            ## create camera filepath
            filePath = os.path.join(camPath, selectedCam)
            filePath = os.path.normpath(filePath)
            filePath = filePath.replace("\\", "/")
            print filePath
            
            
            ## Create Camera2 node and load camPath
            c = nuke.createNode("Camera2")
        
            c["read_from_file"].setValue(True)            
            c["file"].setValue(filePath)
            c["label"].setValue(selectedCam)
            
            
            ## Deselect node before creating new one (so they don't connect)
            for each in nuke.allNodes():
                each.knob("selected").setValue(False) 
        
        except:
            print "Error: An error occured while importing the camera..."
            pass
        

    
    except:
        pass



#importCameras()