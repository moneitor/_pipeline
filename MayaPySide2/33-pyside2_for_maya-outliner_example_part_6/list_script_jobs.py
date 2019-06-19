import maya.cmds as cmds

jobs = cmds.scriptJob(listJobs=True)

for job in jobs:
    print(job)
