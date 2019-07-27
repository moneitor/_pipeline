import json
from datetime import datetime
import os


def store_data(path, shot_number=0, resolution=1920, FPS=24, Client_name="", Project_name="" ):

    """
    Stores a json file containing the data from the project
    """

    project_info = {"Client name": Client_name,
                    "Project name": Project_name,
                    "shot number": shot_number,
                    "resolution": resolution,
                    "FPS": FPS
    }

    with open(path + "\\project_Info.json", "w") as file:
        json.dump(project_info, file, indent=4)



def save_project_info(name="Project", path=""):
    """
    Stores the project information and name
    """
    info_list = []
    info_path = "C:/_fxProjects/_projects/projects_info.json"

    project_name = name
    project_path = path
    date = str(datetime.now())

    info = {
    "folder": os.path.basename(path),
    "project_name": project_name,
    "project_path": path,
    "date": date
    }
    

    if os.path.exists(info_path):
        with open(info_path , "r") as file:
            info_list = json.load(file)
            info_list.append(info)
    else:
        info_list.append(info)    


    with open(info_path , "w") as file:
        json.dump(info_list, file, indent=4)



def read_projects_info(path):
    info = ""
    with open(path, "r") as file:
        info = json.load(file)

    return info


def read_shot_info(path):
    info = ""
    with open(path, "r") as file:
        info = json.load(file)

    return info




    

    




