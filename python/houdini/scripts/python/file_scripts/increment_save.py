import os
import hou


basename = hou.hipFile.basename()
path = hou.hipFile.path()

def return_list_files():
    """
    Return a list of all the files contained in the project folder
    """
    new_path = path.replace(basename , "")
    dir_list = os.listdir(new_path)
    return dir_list


def return_version():
    """
    Return the maximum version contained in the folder
    """
    versions = []
    for _file in return_list_files():
        version = _file.split(".")[0].split("_")[-1].split("R")[-1]
        versions.append(version)
    return max(versions)
