import nuke
import os
import subprocess

## USER SETTINGS
my_version = "0.1"
export_path = "//ldn-fs1/projects/dng02_mae/client_io/out/_test"
export_folder_name = "<SEQ>_<SHOT>_export_<VERSION>"
new_folder_name = "E_<SEQ>_<SHOT>_<ELEMENT>_<VERSION>"
new_file_name = "E_<SEQ>_<SHOT>_lgt_<ELEMENT>_<VERSION>.%04d.<EXT>"


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
        path = "<Q>"+path+"<Q>"
        path = path.replace("<Q>",'"')
        path = path.replace("/","\\")
        path = path.replace("<SEQ>",sequence.lower())
        path = path.replace("<SHOT>",shot.lower())
        path = path.replace("<VERSION>",script_version.lower())
        return path



## PROCESS
print "\n\n---- MAE COLLECT v"+my_version+" ----\n"

for s in nuke.selectedNodes("Read"):
    if s["disable"].getValue() == 0:
        
        ## source Read node info
        node_name = s["name"].getValue()
        log = log+"\n\n"+node_name
        source_file = s["file"].getValue()
        source_file_ext = source_file.split(".")[-1]
        source_first_frame = str(int(s["first"].getValue()))
        source_last_frame = str(int(s["last"].getValue()))
        log = log+"\nRange: "+source_first_frame+"-"+source_last_frame

        ## ELEMENT
        try:
            element = source_file.replace("%04d","")
            element = element.replace(".exr","")
            element = element.replace(".","")
            element = element.split("_")[3]
            #print "Element: "+element    
        except:
            #print "ERROR: Could not determine element name. Please follow the naming conventions!"
            log = log+"\nERROR: Could not determine element name. Please follow the naming conventions!"

            
        ## New File
        new_file = os.path.join(export_path,export_folder_name,new_folder_name,new_file_name)
        
        

        ## Set first framenumber to replace
        count = int(source_first_frame)

        ## Replace padding with framenumber
        while (int(count) != int(source_last_frame)+int(1)):
            file_to_copy = formatFilepath(source_file.replace("%04d",str(count)))
            new_file = formatFilepath(dest_file.replace("%04d",str(count)))

            count = int(count)+1
            


            ## START THE COPY AND OUTPUT RESULTS
            cmd = "cmd /c echo f | xcopy.exe "+file_to_copy+" "+new_file+" /Y"
            print cmd
    
            #p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            #print log+"\n"+files
    #        for line in p.stdout:
    #            print line
    #            log = log+line
    #        p.wait()
    #        print p.returncode

    
        ## Update Read Node's File Path
        new_file_path = new_file_path.replace("\\","/")
        s["file"].setValue(new_file_path)


            

        
## Abort on disabled node        
    else:
        print "\nSkipping "+node_name+" because it is disabled"


## LOG
nuke.message("Please see the script editor for the result of this collection.\nPressing okay will open the export folder.")
print log

## Open Explorer Window in export_path
try:
    cmd = "explorer.exe "+export_path.replace("/","\\")
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
except:
    pass