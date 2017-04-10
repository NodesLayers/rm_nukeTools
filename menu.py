
import sys
import nuke
import os


######Territory Deadline menus
print "Importing Deadline scripts..."
import DeadlineNukeClient
menubar = nuke.menu("Nuke")
tbmenu = menubar.addMenu("&Thinkbox")
tbmenu.addCommand("Submit Nuke To Deadline", DeadlineNukeClient.main, "F8")
try:
    if nuke.env[ 'studio' ]:
        import DeadlineNukeFrameServerClient
        tbmenu.addCommand("Reserve Frame Server Slaves", DeadlineNukeFrameServerClient.main, "")
except:
    pass



## Import Territory Functions (call them through tt.function()
import tt
    
######Territory Python Menu
print "Importing Territory Python menu..."
Territory_Python = nuke.menu('Nuke').addMenu('Territory_Python')

import NukeCollect
Territory_Python.addCommand ('Collect this comp', 'NukeCollect.collectThisComp()')

import readFromWrite
Territory_Python.addCommand ('Read from Write','readFromWrite.ReadFromWrite()','alt+R')

import motionBlurToggle
Territory_Python.addCommand ('motionBlurToggle', 'motionBlurToggle.mBlurToggle()', 'ctrl+alt+m')

import GrainDisable
Territory_Python.addCommand ('GrainDisable', 'GrainDisable.grainToggle()', 'ctrl+alt+g')

import WriteDisable
Territory_Python.addCommand ('WriteDisable', 'WriteDisable.writeToggle()', 'ctrl+alt+w')

import DefocusDisable
Territory_Python.addCommand ('DefocusDisable', 'DefocusDisable.defocusToggle()','ctrl+alt+d')

import bakeGizmos
Territory_Python.addCommand('bakeGizmos', 'bakeGizmos.bakeGizmos()')

import explodeandsum
Territory_Python.addCommand( 'oou_explodeandsum', 'explodeandsum.oou_explodeandsum()', 'ctrl+alt+e')

import newautoBackdrop
Territory_Python.addCommand( 'Colour Backdrop', 'newautoBackdrop.newautoBackdrop()', 'alt+b')

import setWriteNode
Territory_Python.addCommand( 'Set WriteNode', 'setWriteNode.setWriteNode()', 'alt+W')

import readAllSequences
Territory_Python.addCommand( 'Read all sequences from directory...', 'readAllSequences.readAllSequences()')

import changeOSPaths
Territory_Python.addCommand( 'Change OS Paths', 'changeOSPaths.changeOSPaths()')

import readInPlates
Territory_Python.addCommand( 'Read in plates', 'readInPlates.readInPlates()')

import importCameras
Territory_Python.addCommand( 'Import Camera(s)', 'importCameras.importCameras()')

import importGeo
Territory_Python.addCommand( 'Import Geo', 'importGeo.importGeo()')








######terriortory 3de plugins
print "Importing Territory 3DE plugins..."
nuke.menu("Nodes").addCommand("3DE4/LD_3DE4_Anamorphic_Standard_Degree_4", "nuke.createNode('LD_3DE4_Anamorphic_Standard_Degree_4')")
nuke.menu("Nodes").addCommand("3DE4/LD_3DE4_Anamorphic_Degree_6", "nuke.createNode('LD_3DE4_Anamorphic_Degree_6')")
nuke.menu("Nodes").addCommand("3DE4/LD_3DE4_Radial_Standard_Degree_4", "nuke.createNode('LD_3DE4_Radial_Standard_Degree_4')")
nuke.menu("Nodes").addCommand("3DE4/LD_3DE4_Radial_Fisheye_Degree_8", "nuke.createNode('LD_3DE4_Radial_Fisheye_Degree_8')")
nuke.menu("Nodes").addCommand("3DE4/LD_3DE_Classic_LD_Model", "nuke.createNode('LD_3DE_Classic_LD_Model')")





def newViewerRange12():
  # Get the node that is the current viewer
  v = nuke.activeViewer().node()
  # Get the first and last frames from the project settings
  firstFrame = nuke.Root()['first_frame'].value()
  lastFrame = nuke.Root()['last_frame'].value()
  # get a string for the new range and set this on the viewer
  newRange = str(int(firstFrame)+12) + '-' + str(int(lastFrame) - 12)
  v['frame_range_lock'].setValue(True)
  v['frame_range'].setValue(newRange)


def newViewerRange8():
  # Get the node that is the current viewer
  v = nuke.activeViewer().node()
  # Get the first and last frames from the project settings
  firstFrame = nuke.Root()['first_frame'].value()
  lastFrame = nuke.Root()['last_frame'].value()
  # get a string for the new range and set this on the viewer
  newRange = str(int(firstFrame)+8) + '-' + str(int(lastFrame) - 8)
  v['frame_range_lock'].setValue(True)
  v['frame_range'].setValue(newRange)



nuke.menu('Nuke').addCommand('Viewer/Viewer Handles - 12f',
"newViewerRange12()")
nuke.menu('Nuke').addCommand('Viewer/Viewer Handles - 8f',
"newViewerRange8()")




