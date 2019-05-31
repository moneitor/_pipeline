import os
import sys
import subprocess

def houdini_env(project_path):
    e = os.environ
    pwd = os.path.dirname(os.path.abspath(__file__))
    hfs = r'C:\Program Files\Side Effects Software\Houdini 17.0.352'
    e['HH'] = os.pathsep.join([os.path.join(hfs, 'houdini'), os.path.expanduser(r'~\Documents\houdini17.0')])
    e['HOUDINI_PATH'] = ';'.join([os.path.join(pwd, 'houdini'), e['HH'], e.get('HOUDINI_PATH', '')])
    e['JOB'] = project_path + "\\02_work\\fx\\01_houdini"



