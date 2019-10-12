#! C:\Program Files\Side Effects Software\Houdini 17.5.258\houdini\python2.7libs

import os
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)


import sys
import hou

TEMPLATE_SCENE = r"C:\Users\mo_no\Documents\HERNAN\LEARNING_PYTHON\HYTHON\templateScene.hip"

currentPath = os.path.dirname(__file__)
listdirs = [folder for folder in os.listdir(currentPath) if os.path.isdir(folder)]


# Open the houdini template scene and store it in a variable
hou.hipFile.load(TEMPLATE_SCENE)

# Name of the template file
hipName = os.path.basename(hou.hipFile.name())


# Copy the file in the shot directories
for folder in os.listdir(currentPath):

	shotPath = os.path.join(currentPath, folder)

	if os.path.isdir(shotPath):

		houdini_file_path = shotPath + "/" + folder + "_"  + hipName
		hou.hipFile.save(houdini_file_path)
		
		hou.hipFile.load(houdini_file_path)

		mantra_node = hou.node("/out/torus_test")

		mantra_node.parm("execute").pressButton()


