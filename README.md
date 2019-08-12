## Writing a simple pipeline
I am trying to learn Python on my free time, and to do it I decided to 
create some simple tools that should help me speed up my workflow and
scene creation inside Houdini, and hopefully with time I will be able to
integrate more softwares withing it like Nuke and Maya.

The scripts might not be elegant and this is because I am fairly new to the 
language, but with time they will get better.

### Main elements 


### _pipeline/python/

All the .py files included here are used to create the project, all the metadata
and the folders related to your project, when you create a project it will create
a json file in the _projects folder containing the information of your project
and also will append the information of your shot to the projects_info_json in 
the _fxProjects folder, this is the ui:

![](images/project_manager.JPG)

### _pipeline/python/houdini/scripts/python/

All the Python files that will be loaded from Houdini will be included here, inside **file_scripts**
you will find tools to open and create new scenes, increase version, control all the mantra nodes at once
and I will be adding new tools weekly, this are some of them.




