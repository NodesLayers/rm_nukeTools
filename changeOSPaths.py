import nuke
import os

def changeOSPaths():

	for s in nuke.selectedNodes():
		
		file = s["file"].getValue()
		file = os.path.normpath(file)


		## WINDOWS
		if os.name == "nt":
			try:
				file = file.replace("\Volumes\FilmShare", "y:/")
				file = file.replace("/Volumes/FilmShare", "y:/")
				file = os.path.normpath(file)
				file = file.replace("\\", "/")
				s["file"].setValue(file)
			except:
				valueError
				nuke.message("Something went wrong :(")

		if os.name == "posix":
			try:
				file = file.replace("y:/","\Volumes\FilmShare")
				file = file.replace("y:\\","\Volumes\FilmShare")
				file = os.path.normpath(file)
				s["file"].setValue(file)
			except:
				valueError
				nuke.message("Something went wrong :(")

		print "Replaced path for "+str(s.name())+" with "+file
    
    

