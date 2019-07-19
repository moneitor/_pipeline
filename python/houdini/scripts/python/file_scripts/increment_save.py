import os
import hou


basename = hou.hipFile.basename()
path = hou.hipFile.path()

def return_list_files():
    """
    Return a list of all the files contained in the project folder
    """
    file_path = hou.hipFile.path().replace(hou.hipFile.basename() , "")
    dir_list = os.listdir(file_path)
    return dir_list, file_path


def return_version():
    """
    Return the maximum version contained in the folder
    """
    versions = []
    for _file in return_list_files()[0]:
        if _file.endswith(".hip"):
            version = _file.split(".")[0].split("_")[-1].split("R")[-1]
            versions.append(version)

    return max(versions)


def return_basename():
    current_version = return_version()
    new_version = int(current_version) + 1
    new_version_str = str(new_version)

    new_name1 = basename.split("VER{}".format(current_version))[0]    

    new_name2 = basename.split("VER{}".format(current_version))[-1]   
    

    new_name_total = new_name1 + "VER" + new_version_str + new_name2
    return new_name_total


def save_increment():
    file_path = return_list_files()[1]
    new_name = return_basename()

    new_path = file_path + "/" + new_name
    hou.hipFile.save(new_path, True)

    return new_path


save_increment()
