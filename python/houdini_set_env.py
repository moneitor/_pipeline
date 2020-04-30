import os
import sys
import subprocess

def houdini_env(project_path, hou_main_path, hou_doc_path, render_path, project_name, fps, resx, resy):
    e = os.environ
    pwd = os.path.dirname(os.path.abspath(__file__))     
    
    
    hfs = hou_main_path
    #e['HH'] = os.pathsep.join([os.path.expanduser(hou_doc_path), os.path.join(hfs, 'houdini')])
    #e['HH'] = 'C:/PROGRA~1/SIDEEF~1/HOUDIN~1.258/houdini'        
    e['HH'] = 'C:/PROGRA~1/SIDEEF~1/HOUDIN~1.416/houdini'    
    e['HOUDINI_PATH'] = ';'.join([os.path.join(pwd, 'houdini'), e['HH'], e.get('HOUDINI_PATH', '')])
    e['HOUDINI_TOOLBAR_PATH'] = ';'.join([e.get('HOUDINI_PATH', ''), e['HH'], os.path.join(pwd, 'houdini')])
    e['JOB'] = project_path + "\\02_work\\fx\\01_houdini"      
    e['HOUDINI_USER_PREF_DIR'] =  ';'.join(os.path.join(pwd, 'houdini__HVER__'))
    e['PROJECT_NAME'] = project_name
    e['PROJECT_PATH'] = project_path
    e['FPS'] = fps
    e['RESOLUTION_X'] = resx
    e['RESOLUTION_Y'] = resy
    e['solidangle_LICENSE'] = "5053@localhost"






    




