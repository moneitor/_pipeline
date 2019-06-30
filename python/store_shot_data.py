import json

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

