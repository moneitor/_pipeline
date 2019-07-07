import os

def return_app_path():
    temp_hou_path1 = r'C:\Program Files\Side Effects Software\Houdini 17.5.258\bin'
    temp_hou_path2 = r'C:\Program Files\Side Effects Software\Houdini 17.0.352\bin'
    hou_path = ""

    if os.path.exists(temp_hou_path1):
        hou_path = temp_hou_path1 + '\houdinifx.exe'
    else:
        if os.path.exists(temp_hou_path2):
            hou_path = temp_hou_path2 + '\houdinifx.exe'
        else:
            print("The houdini version requested is not installed")

    sublime_path = r'C:\Program Files\Sublime Text 3\sublime_text.exe'
    visual_path = r'C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\devenv.exe'

    return hou_path, sublime_path, visual_path





