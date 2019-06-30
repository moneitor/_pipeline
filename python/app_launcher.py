from general_functions import run_app , go_folder, create_folders
from houdini_set_env import houdini_env

"""
This file contains the paths to all the softwares
that are going to be launched from the interface
"""

#Software paths
hou_path = r'C:\Program Files\Side Effects Software\Houdini 17.5.258\bin\houdinifx.exe'
sublime_path = r'C:\Program Files\Sublime Text 3\sublime_text.exe'
visual_path = r'C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\devenv.exe'


create_folders(shot_number, temp_path)
go_folder(temp_path, 12, shot_number)
houdini_env(temp_path)

