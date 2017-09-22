## This tool changes the MAE_UNDISTORT and MAE_DISTORT nodes filepaths based on user input. 
## If no input into either or both it ignores and doesnt change anything on that node.

def changeDistortMaps():
    import nuke

    my_version = "v0.1"
    my_name = "MAE: Change (un)distort maps"

    nuke.message("This tool changes all the MAE Undistort & \nDistort groupnodes filepaths in the script.")
    p = nuke.Panel(my_name+" "+my_version)    
    p.addFilenameSearch('New Distort Map:',"")
    p.addFilenameSearch('New Undistort Map:',"")
    ret = p.show()

    new_distort = p.value("New Distort Map:")
    new_undistort = p.value("New Undistort Map:")

    if new_distort != "":
        for s in nuke.allNodes():
            node_name = s["name"].getValue()
            if node_name.find("MAE_DISTORT") != -1:
                s["file"].setValue(new_distort)
                print node_name+": SUCCESS"

    if new_undistort != "":
        for s in nuke.allNodes():
            node_name = s["name"].getValue()
            if node_name.find("MAE_UNDISTORT") != -1:
                s["file"].setValue(new_undistort)
                print node_name+": SUCCESS"
                

                
#changeDistortMaps()