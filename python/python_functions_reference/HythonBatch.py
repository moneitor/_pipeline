#! C:\Program Files\Side Effects Software\Houdini 17.5.258\houdini\python2.7libs

import os
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Uncomment the next line to dissable logging
#logging.disable(logging.CRITICAL)


import sys
import hou

TEMPLATE_SCENE = r"C:\Users\mo_no\Documents\HERNAN\LEARNING_PYTHON\HYTHON\templateScene.hip"

thisFilePath = os.path.dirname(__file__)
listdirs = [folder for folder in os.listdir(thisFilePath) if os.path.isdir(folder)]


env = os.environ


VER = "v1"

#TODO: Implement the project Class
class Project(object):
	"""
	Class containing the current project
	"""
	def __init__(self, project_path="", template_scene_path=""):
		"""
		:shot_path: The path to the project
		:template_scene_path: The path to the template file that needs to be
			run in all the shots
		"""
		self.project_path = project_path
		self.template_scene_path = template_scene_path


	def project_shot_list(self):
		"""
		Returns a list containing all the shots
		"""
		pass



class Shot(object):	
	"""
	:project: is an instance of a Project class
	"""

	def __init__(self, Project):
		self.project = project


	def return_shot(self):
		pass

	#TODO: get_current_versio
	def get_current_version(self):
		"""
		Return current version as Integer		
		"""
		pass

	#TODO: increase_current_version
	def increase_current_version(self, filePath):
		"""
		Return a next version as Integer
		"""
		pass


# Copy the file in the shot directories
def save_to_folder_and_render(currentPath, template_scene, ver="1"):
	"""
	TODO: get a list with the actual shot folders, this is just a prototype
	Go through all the folders inside currentPath "shots"
	open the TEMPLATE_SCENE adjust and update nodes and then save a new
	file with the correct name on each shot folder
	"""

	# Open the houdini template scene and store it in a variable
	hou.hipFile.load(template_scene)

	# Name of the template file
	hipName = os.path.splitext(os.path.basename(hou.hipFile.name()))[0] 


	for folder in os.listdir(currentPath):

		shotPath = os.path.join(currentPath, folder)

		if os.path.isdir(shotPath) and folder!= "backup":
			logging.debug("Setting environment variables")		

			env["SHOT"] = folder

			logging.debug("Saving new houdini file into {}".format(folder))
			houdini_file_path = shotPath + "/" + folder + "_"  + hipName + "_" + ver + ".hip"
			hou.hipFile.save(houdini_file_path)
			
			logging.debug("Opening new scene in {} and executing commands".format(folder))
			hou.hipFile.load(houdini_file_path)
			mantra_node = hou.node("/out/torus_test")
			
			logging.debug("Rendering {}......".format(folder))
			mantra_node.parm("execute").pressButton()

			logging.debug("Finished process on {}, moving on to next folder".format(folder))




save_to_folder_and_render(thisFilePath, TEMPLATE_SCENE, VER)