import nuke

def readReload():

    try:
        for n in nuke.allNodes("Read"):
            n["reload"].execute()
            print "readReload: Reloaded all read nodes"
    except:
        print "readReload: Something went wrong"
        

        
#readReload()