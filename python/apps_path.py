import os

def return_app_path():
    # TODO apply this to the hou_set_env.py
    temp_hou_main_path1 = r'C:\Program Files\Side Effects Software\Houdini 18.0.416'
    temp_hou_main_path2 = r'C:\Program Files\Side Effects Software\Houdini 17.5.258'
    hou_main_path = ""
    
    temp_hou_doc_path1 = r'~\Documents\houdini18.0'
    temp_hou_doc_path2 = r'~\Documents\houdini17.5'
    hou_doc_path = ""

    temp_hou_path1 = r'C:\Program Files\Side Effects Software\Houdini 18.0.416\bin'
    temp_hou_path2 = r'C:\Program Files\Side Effects Software\Houdini 17.5.258\bin'
    hou_path = ""

    if os.path.exists(temp_hou_path1):
        hou_path = temp_hou_path1 + r'\houdinifx.exe'
        hou_main_path = temp_hou_main_path1
        hou_doc_path = temp_hou_path1
    else:
        if os.path.exists(temp_hou_path2):
            hou_path = temp_hou_path2 + r'\houdinifx.exe'
            hou_main_path = temp_hou_main_path2
            hou_doc_path = temp_hou_path2
        else:
            print("The houdini version requested is not installed")

    sublime_path = r'C:\Program Files\Sublime Text 3\sublime_text.exe'
    visual_path = r'C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\devenv.exe'
    nuke_path = r'C:\Program Files\Nuke11.3v4\Nuke11.3.exe'


    return hou_path, hou_main_path, hou_doc_path, sublime_path, visual_path, nuke_path





