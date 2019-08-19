from __future__ import print_function

import hou

# A minimal state handler implementation. 
class MyState(object):
    def __init__(self, state_name, scene_viewer):
        self.state_name = state_name
        self.scene_viewer = scene_viewer

    # Handler methods go here
    def onMouseEvent(self, kwargs):
        dev = kwargs["ui_event"].device()
        print("Mouse:", dev.mouseX(), dev.mouseY(), dev.isLeftButton())

# A registration entry-point
def createViewerStateTemplate():
    # Choose a name and label 
    state_name = "mystate"
    state_label = "My New State"
    category = hou.sopNodeTypeCategory()

    # Create the template
    template = hou.ViewerStateTemplate(state_name, state_label, category)
    template.bindFactory(MyState)

    # Other optional bindings will go here...

    # returns the 'mystate' template
    return template