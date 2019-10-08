import os
import hou
import toolutils
import soptoolutils


##PUT THIS IN THE PYTHON POST RENDER SCRIPT TO SEND AN EMAIL ONCE THE RENDER IS FINISHED
import smtplib as s
import datetime as d

def sendMailto (email , password , nodeName):
    mymail = 'yourEmail@gmail.com'
    conn = s.SMTP("smtp.gmail.com" , 587)
    conn.ehlo()
    conn.starttls()
    conn.login(mymail , 'yourPassword')
    curentTime = d.datetime.now()
    conn.sendmail(mymail , mymail , 'Subject: The render of %s, is done at time: %s' %(nodeName , curentTime))

    conn.quit() 



###############################################################################################

###############################################################################################



def copyAndPaint():
    """Let you select a node in the screen
    press enter and then paint and this will create a scatter 
    that will create points using colors as density
    """
    v = toolutils.sceneViewer()
    sel = hou.selectedNodes()

    if sel:
        paint = toolutils.findChildNodeOfTypeWithParms(sel[0], 'paint', {'overridecd': 1})
        if paint:
            paint.setCurrent(True)
            v.enterCurrentNodeState()
            return

    scatter_geo = v.selectObjects("Please select objects to copy to: ",
                                  use_existing_selection=False,
                                  allowed_types=("geo",))

    source_geo = v.selectObjects("Please select source: ",
                                 use_existing_selection=False,
                                 allowed_types=("geo",))

    if not (scatter_geo and source_geo):
        return
    elif len(scatter_geo) > 1 or len(source_geo) > 1:
        hou.ui.displayMessage("Please select one geometry object")
        return
    scatter_geo = scatter_geo[0]
    source_geo = source_geo[0]

    geo = hou.node('/obj').createNode('geo', 'copy', run_init_scripts=False)
    merge_source = geo.createNode('object_merge', 'merge_source')
    merge_source.parm('objpath1').set(source_geo.path())
    merge_source.parm('xformtype').set(1)

    paint = soptoolutils.buildPaintNode(merge_source, None,
                                        parms={'overridecd': 1, 'cdname': 'density'},
                                        props={'attribdef': 0, 'fgcolor': 0.2, 'opacity': 0.3, 'radius': 0.5})
    paint.moveToGoodPosition()

    merge_scatter = geo.createNode('scatter', 'sourcePts')
    merge_scatter.setInput(0, paint)
    merge_scatter.parm('npts').set(10)
    merge_scatter.parm('usedensityattrib').set(1)
    merge_scatter.parm('densityattrib').set('Cd')
    merge_scatter.parm('forcetotal').set(0)
    merge_scatter.parm('densityscale').set(15)
    merge_scatter.moveToGoodPosition()

    merge_to_copy = geo.createNode('object_merge', 'merge_geo')
    merge_to_copy.parm('objpath1').set(scatter_geo.path())
    merge_to_copy.parm('xformtype').set(1)

    merge_copy = geo.createNode('copytopoints', 'copy')
    merge_copy.setInput(0, merge_to_copy)
    merge_copy.setInput(1, merge_scatter)
    merge_copy.moveToGoodPosition()
    merge_copy.setDisplayFlag(1)

    source_geo.setDisplayFlag(0)
    scatter_geo.setDisplayFlag(0)

    geo.layoutChildren()
    paint.setCurrent(True)
    v.enterCurrentNodeState()


###############################################################################################

###############################################################################################


##THIS FIND THE POSITION OF A POINT PROJECTED ON A LINE AND CREATE PRIMITIVES
import cProfile
import numpy as n

node = hou.pwd()
geo = node.geometry()


def point_line_intersection(centroid, p1, p2):

    a = p2.position() - p1.position()
    centp1 = centroid - p1.position()
    betha = n.dot(a, centp1) / a.length()
    anorm = a.normalized()
    anorm *= betha
    dist = anorm.length()
    intersect = p1.position() + anorm
    return intersect, dist


try:
    get_curve = node.inputs()[1].geometry()
except IndexError:
    raise hou.InvalidInput("Need second Input")

# add color and distance attributes
clr_attr = geo.addAttrib(hou.attribType.Point, "Cd", (0, 1, 0))
dist_attr = geo.addAttrib(hou.attribType.Prim, "dist", -1)
# create the groups
line_grp = geo.createPrimGroup("lines")
base_grp = geo.createPrimGroup("base")

for pr in geo.prims():
    for vert in pr.vertices():
        vert.point().setAttribValue(clr_attr, (1, 1, 1))
    base_grp.add(pr)

curve_pts = get_curve.iterPoints()

counter = 0.0
numPrims = float(len(geo.prims()))

with hou.InterruptableOperation("Creating primitives..") as oper:
    for prim in base_grp.prims():
        centroid = prim.positionAtInterior(0.5, 0.5, 0)
        intersect, dist = point_line_intersection(centroid, curve_pts[0], curve_pts[1])
        poly = geo.createPolygon()
        poly.setIsClosed(False)
        counter += 1
        percent = counter / numPrims
        for pos in [centroid, intersect]:
            point = geo.createPoint()
            point.setPosition(pos)
            poly.addVertex(point)
            line_grp.add(poly)
        oper.updateProgress(percent)




###############################################################################################

###############################################################################################



def solveForObjects(solver_data, new_dop_objects, existing_dop_objects, time, timestep):
    def findID(id):
        return solver_data.dopNetNode().simulation().objects()[id]

    for obj in new_dop_objects:
        obj.createSubData("MyImpactTime")
    for obj in existing_dop_objects:
        activeState = True
        doColor = False
        impactData = obj.findSubData("Impacts")
        objImpactTime = 0.0
        color = (0.0, 0.0, 0.0)
        if impactData:
            impactObjId = impactData.record("Impacts").field("otherobjid")
            if impactObjId == 1:
                activeState == False
                doColorize = True
                color = (1.0, 0.0, 0.0)
                objImpactTime = impactData.record("Impacts").field("time")

            else:
                box_obj = findID(impactObjId)
                if box_obj.findSubData("SolverParms/ActiveValue").options().field("active") == 1:
                    activeState = False
                    doColorize = True
                    color = (0, 0, 0)
                    objImpactTime = impactData.record("Impacts").field("time")
            obj.findSubData("SolverParms/ActiveValue").options().setField("active", activeState)
            obj.findSubData("MyImpactTime").options().setField("time", objImpactTime)
            '''
            if doColorize:
                with obj.editableGeometry() as g:
                    if not g.findPrimAttrib("Cd"):
                        g.addAttrib(hou.attribType.Prim, "Cd" , color)'''




###############################################################################################

###############################################################################################

# LOGGIN EXAMPLE

import logging
# Basic template for logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Basic template for logging but this one will save to a file in disk
logging.basicConfig(filename="testLoggin.txt", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

#This line is to disable any logging
logging.disable(logging.CRITICAL)


logging.debug("Start of program")


def factorial(n):
    logging.debug("Start of factorial")
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.critical("i is {} and total is {}".format(i, total))
    return total


print(factorial(5))


logging.debug("End of program")

