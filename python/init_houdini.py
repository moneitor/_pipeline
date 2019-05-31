import hou

def init_nodes():
    obj_level = hou.node("/obj")
    obj_level.createNode("cam", "shot_cam")


