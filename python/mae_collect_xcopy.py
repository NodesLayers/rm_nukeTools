import nuke
import os
import subprocess


## Save Current Script State
curScript = nuke.toNode("root").name()


## USER SETTINGS
my_version = "0.1"
export_path = "//ldn-fs1/projects/dng02_mae/client_io/out/_test"
export_folder_name = "<SEQ>_<SHOT>_export_<VERSION>"
new_folder_name = "E_<SEQ>_<SHOT>_<ELEMENT>_<DESCRIPTION>_<VERSION>"
new_file_name = "E_<SEQ>_<SHOT>_lgt_<ELEMENT>_<DESCRIPTION>_<VERSION>.%04d.<EXT>"


## Nukescript name
script_name = os.path.basename(nuke.root().name())
script_name = script_name.replace(".nk","")

## VARS
sequence = script_name.split("_")[0]
shot = script_name.split("_")[1]
script_version = script_name.split("_")[-1]
log = ""
log = log+"\nSequence: "+sequence+"\nShot: "+shot+"\nScript version: "+script_version




## PANEL
p = nuke.Panel('MAE Collect v'+my_version)    
p.addFilenameSearch('Export path:', export_path)
ret = p.show()

export_path = p.value("Export path:")

def formatFilepath(path):
        path = path.replace('"',"")
        path = "<Q>"+path+"<Q>"
        path = path.replace("<Q>",'"')
        path = path.replace("/","\\")
        path = path.replace("<SEQ>",sequence.lower())
        path = path.replace("<SHOT>",shot.lower())
        path = path.replace("<ELEMENT>",element_name)
        path = path.replace("<DESCRIPTION>",description)
        path = path.replace("<VERSION>",script_version.lower())
        path = path.replace("<EXT>",source_file_ext)
        return path

def findElementNameFromFile(element_name):
    side = ""
    if element_name.find("_L_") != -1:
        element_name = element_name+"_L"
        side = "L"
    if element_name.find("_C_") != -1:
        element_name = element_name+"_R"
        side = "C"
    if element_name.find("_R_") != -1:
        element_name = element_name+"_R"
        side = "R"
    element_name = element_name.split("_")[3]
    return element_name+side

def findDescriptionNameFromFile(des_path):
    des_path = des_path.replace("_L_","_")
    des_path = des_path.replace("_l_","_")
    des_path = des_path.replace("_R_","_")
    des_path = des_path.replace("_r_","_")
    des_path = des_path.split("_")[4]
    description = des_path
    return description



## PROCESS
print "\n\n---- MAE COLLECT v"+my_version+" ----\n"

for s in nuke.selectedNodes("Read"):
    if s["disable"].getValue() == 0:
        
        ## source Read node info
        node_name = s["name"].getValue()
        log = log+"\n\n\n\n------------\n"+node_name
        source_path = s["file"].getValue()
        source_file = os.path.basename(s["file"].getValue())
        source_file_ext = source_file.split(".")[-1]
        source_first_frame = str(int(s["first"].getValue()))
        source_last_frame = str(int(s["last"].getValue()))
        log = log+"\nRange: "+source_first_frame+"-"+source_last_frame

          
        ## Find element name and description
        element_name = findElementNameFromFile(source_file)
        description = findDescriptionNameFromFile(source_file)


        ## New File Path
        new_file_path = os.path.join(export_path,export_folder_name,new_folder_name,new_file_name)
        

        ## Set first framenumber to replace
        count = int(source_first_frame)

        ## Replace padding with framenumber
        while (int(count) != int(source_last_frame)+int(1)):
            file_to_copy = formatFilepath(source_path.replace("%04d",str(count)))
            new_file = formatFilepath(new_file_path.replace("%04d",str(count)))

            ## Create file_list and add it to the log
            file_list = "\nCopied and renamed: "+os.path.basename(file_to_copy)+" --> "+new_file
            log = log+"\n"+file_list

            ## Increase FrameNumber
            count = int(count)+1  

            ## START THE COPY AND OUTPUT RESULTS
            cmd = "cmd /c echo f | xcopy.exe "+file_to_copy+" "+new_file+" /Y"
            #print "\n"+cmd
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
#            for line in p.stdout:
#                print line
#                log = log+line
#            p.wait()
#            print p.returncode

    
        ## Update Read Node's File Path
        new_file_path = new_file_path.replace("\\","/")
        #s["file"].setValue(new_file_path)
        log = log+"\n\nUpdated Read node path"


            

        
## Abort on disabled node        
    else:
        print "\nSkipping "+node_name+" because it is disabled"


## LOG
nuke.message("Please see the script editor for the result of this collection.\nPressing okay will open the export folder.")
print log

## Save the export script
export_script_path = os.path.join(export_path,export_folder_name,sequence+"_"+shot+"_export_"+script_version+".nk")
nuke.scriptSaveAs(export_script_path)
nuke.undo()
nuke.scriptSaveAs(curScript)

## Open Explorer Window in export_path
try:
    cmd = "explorer.exe "+export_path.replace("/","\\")
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
except:
    pass