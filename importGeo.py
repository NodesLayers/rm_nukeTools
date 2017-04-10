import nuke
import os

def importGeo():

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
            geoPath = os.path.join(drive, "\\", showName, "source\cameras\\" ,sequence, sequence+"_"+shot)
            geoPath = os.path.normpath(geoPath)
            print "geoPath: "+geoPath
            
            flist = []

            ## For each file in the listed directory, check the ext and if it matches, go further and import
            for f in os.listdir(geoPath):
                ext = os.path.splitext(f)[-1].lower()
                if (ext == ".abc") or (ext == ".obj") or (ext == ".fbx"):
                    print f

                    flist.append(f)
        
        except:
            print "Error: An error occured while creating a list of geo(s)..."
            pass
 

        ## Select and import geo
        try:
            ## PANEL
            p = nuke.Panel('Select Geo')
            p.addEnumerationPulldown('Geo:', flist)
            p.show()
        
        
            selectedGeo = p.value("Geo:")
            selectedGeo = selectedGeo.replace("'", "")
            selectedGeo = selectedGeo.replace("[", "")
            selectedGeo = selectedGeo.replace("]", "")
            selectedGeo = selectedGeo.replace(",", "")
        
        
            ## create geo filepath
            filePath = os.path.join(geoPath, selectedGeo)
            filePath = os.path.normpath(filePath)
            filePath = filePath.replace("\\", "/")
            print filePath
            
            
            ## Create ReadGeo2 node and load geo filepath
            c = nuke.createNode("ReadGeo2")    
            c["file"].setValue(filePath)
            c["label"].setValue(selectedGeo)
            
            
            ## Deselect node before creating new one (so they don't connect)
            for each in nuke.allNodes():
                each.knob("selected").setValue(False) 
        
        except:
            print "Error: An error occured while importing the geo..."
            pass
        

    
    except:
        pass


#importGeo()