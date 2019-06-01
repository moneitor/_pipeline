from general_functions import run_app , go_folder, create_folders
from houdini_set_env import houdini_env


#Software paths
hou_path = r'C:\Program Files\Side Effects Software\Houdini 17.0.352\bin\houdinifx.exe'
sublime_path = r'C:\Program Files\Sublime Text 3\sublime_text.exe'
visual_path = r'C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\devenv.exe'
temp_path = r'C:\Users\Hernan\Documents\HERNAN\_projects\test_project_3'
temp_path2 = r'C:\Users\monei\Documents\HERNAN\_projects\test_project_3'
shot_number = 12

create_folders(shot_number, temp_path2)
go_folder(temp_path2, 12, shot_number)
houdini_env(temp_path2)
run_app(hou_path)


