import subprocess as sub
import os



def asset_folders():
    folders = {"01_Asset": {"Models": None,
                            "Shaders": None}}

    return folders


def design_folders():
    folders = {"02_Design": {"After_effects":None,
                             "Illustrator": None,
                             "Photoshop": None}}
    return folders

def reference():
    folders = {"03_reference": {"client": None,
                                "personal": None}}

    return folders

def sandbox():
    folders = {"04_Sandbox": {"Natalia": None,
                              "Hernan": None}}

    return folders


def shot(shot_number):
    folders = {"Shot_{}".format(shot_number): {"reference": {"footage": None,
                                                             "artWork": None},
                                               "publish": None,
                                               "work": {"anim": None,
                                                        "comp": None,
                                                        "fx":  {"Geo": None , "Textures": None, "Render": None, "Flipbooks": None,
                                                                "Abc": None, "Hda": None, "Simulation": None,
                                                                "Cameras": None},
                                                        "Lighting": None,
                                                        "Roto": None,
                                                        "RnD": None,
                                                        "Track": None}}}

    return folders



def make_dirs_from_dict(direct, current_dir='./'):
    for key, values in direct.items():
        pathFolder = os.path.join(current_dir, key)
        if not os.path.exists(pathFolder):
            os.mkdir(pathFolder)
            if type(values) == dict:
                make_dirs_from_dict(values, os.path.join(current_dir, key))


r = "C:\\Users\\Hernan\\Documents\\HERNAN\\_projects\\test_project_3\\Shot_10\\work\\fx"

def go_folder(project_path, houdini=0, shot_number=0):
    '''Set the project_path as the current working directory
    if the second argument is 1, then the path will be set to the
    houdini working directory'''
    if not houdini:
        os.chdir(project_path)
    else:
        os.chdir(project_path + '\\Shot_{}\\work\\fx'.format(shot_number))


def run_app(app_path):
    '''Run the app specified in the app_path'''
    app_path.replace("\\", '/')
    sub.Popen(app_path)


def create_folders(shot_num, path):
    make_dirs_from_dict(asset_folders(), path)
    make_dirs_from_dict(design_folders(), path)
    make_dirs_from_dict(reference(), path)
    make_dirs_from_dict(sandbox(), path)
    for i in range(0, int(shot_num)):
        make_dirs_from_dict(shot(i), path)
        print(i)

