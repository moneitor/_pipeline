import subprocess

# Software paths we are using to load the exe
hou_path = r'C:\Program Files\Side Effects Software\Houdini 17.5.258\bin\houdinifx.exe'
sublime_path = r'C:\Program Files\Sublime Text 3\sublime_text.exe'
visual_path = r'C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\devenv.exe'


def launcher_run_app(softpath):
    softpath.replace("\\", '/')
    subprocess.Popen(softpath)


launcher_run_app(sublime_path)