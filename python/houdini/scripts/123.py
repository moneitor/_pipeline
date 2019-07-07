import hou

obj = hou.node("/obj")

#creates a Null
null = obj.createNode("null" , "Cam_control")

#create camera
def createCam(_null):
    cam = obj.createNode("cam", "shot_cam")
    res = {'resx': 1920 , 'resy': 1080}
    #set the camera parms
    cam.setParms(res)
    cam.setInput(0 , _null)
    cam.moveToGoodPosition()
    return cam


#Create the mantra node
out = hou.node("/out")

def createMantra(_cam):
    mantra = out.createNode("ifd", "mantra_shot")
    camParm = mantra.parm("camera")
    camParm.set(_cam.path())
    mantra.parm("vobject").set("")
    mantra.parm("alights").set("")
    mantra.setParms({"vm_renderengine": "pbrraytrace" , "trange": "normal"})

def main():
    cam = createCam(null)
    createMantra(cam)

main()