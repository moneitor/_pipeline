from __future__ import with_statement

import os
import re
import shutil
import string
import tempfile
import zipfile

import threading

import hou
import hutil.json
import assetdownload
import digitalassetsupport
import sas.inspectasset
import sas.localassets
import webbrowser

def installPackage(shelf_name, shelf_pkg_path, install_path):
    """ Installs the shelf package, 'shelf_pkg_path', into
        the given installation directory. This removes previously installed
        packages with the same shelf name.  Returns the final installation
        path for the shelf package.  Returns the empty string on failure. """

    install_path = os.path.join(install_path, shelf_name)
    shelf_pkg_filename = os.path.basename(shelf_pkg_path)

    # Clean-up previous shelf installation if one exists.
    if os.path.exists(install_path):
        # Uninstall old shelf OTLs.
        loaded_otls = hou.hda.loadedFiles()
        norm_loaded_otls = []
        for i in range( len(loaded_otls) ):
            norm_loaded_otls.append( normalizePath(loaded_otls[i]) )
        shelf_otls = findShelfOTLFiles(install_path)
        for shelf_otl in shelf_otls:
            shelf_otl = normalizePath(shelf_otl)
            if shelf_otl in norm_loaded_otls:
                hou.hda.uninstallFile(shelf_otl)

        # Remove all installation files from dist.
        shutil.rmtree(install_path, ignore_errors=True)

    # Recursively create the installation directory that will hold 
    # the shelf contents.
    os.makedirs(install_path)

    is_supported_archive = assetdownload.isSupportedArchive(shelf_pkg_filename)
    if is_supported_archive:
        # Unpackage the contents of the zip file into the install directory.
        assetdownload.extractArchive(shelf_pkg_path, install_path)
    else:
        # Copy the shelf package file into the install directory.
        shutil.copy(shelf_pkg_path, install_path)

    return install_path

def downloadAndInstallPackage(shelf_name, shelf_url, install_path,
                              tmp_path=None):
    """ Downloads the shelf package from 'shelf_url' and installs it
        into the given installation directory.  Returns the final install
        path of the shelf package.  Returns the empty string on failure. """

    # First, attempt to download the shelf package.
    # Store the package in a temporary directory.
    if tmp_path is None:
        tmp_path = tempfile.tempdir()
    tmp_path = os.path.join(tmp_path, shelf_name + ".shelf")
    if os.path.exists(tmp_path) != True:
        os.makedirs(tmp_path)
    dl_file_path = assetdownload.downloadFile(shelf_url, tmp_path)
    if dl_file_path == "":
        return ""

    # Ok, we successfully downloaded the package into a temporary location.
    # Now install the package into our installation path.
    final_path = installPackage(shelf_name, dl_file_path, install_path)
    if final_path == "":
        return ""

    # Clean-up.  Remove the temporary downloaded package file and its
    # containing folder.
    os.remove(dl_file_path)
    shutil.rmtree(tmp_path)

    return final_path

def normalizePath(path):
    """ Normalizes the given file path by replacing backward slashes
        with forward slashes.  This function is useful when comparing
        file paths. """
    return path.replace("\\", "/")

def findFilesByExtension(dir, file_ext):
    """ Recursively searches in 'dir' and returns a list of all the files
        found in the directory tree that match the given file extension.
        Does not search in hidden directories or 'backup' directories. """
    files = []

    exclude_pattern = os.environ.get('HOUDINI_SHELF_EXCLUDE_DIRS_PATTERN', None)
    if exclude_pattern is not None:
        exclude_pattern = re.compile(exclude_pattern)
    search_dirs = [ dir ]
    while len(search_dirs) > 0:
        cur_dir = search_dirs.pop()
        if os.path.exists(cur_dir) != True or os.path.isdir(cur_dir) != True:
            continue

        # List directory contents.
        cur_files = os.listdir(cur_dir)
        for cur_file in cur_files:
            # Ignore 'backup' directories and files.
            # Ignore hidden directories and files.
            if cur_file == "backup" or cur_file.startswith("."):
                continue
	    # Ignore exclude patterns
            if exclude_pattern is not None and exclude_pattern.match(cur_file):
                continue

            full_path = os.path.join(cur_dir, cur_file)
            # If we have a subdirectory, then add it to our search
            # directory list.
            if os.path.isdir(full_path):
                search_dirs.append(full_path)
            # If the regular file has the matching file extension,
            # then add it to our result list.
            elif os.path.isfile(full_path) and full_path.endswith(file_ext):
                files.append(normalizePath(full_path))

    return files


def findShelfFiles(shelf_install_dir, shelf_extensions=None):
    """ Recursively searches in 'shelf_install_dir' and returns a list
        of shelf files found in the directory tree.  Does not search
        in hidden directories or 'backup' directories. """
    shelf_files = []
    if shelf_extensions is None:
        shelf_files = findFilesByExtension(shelf_install_dir, ".shelf")
    else:
        for ext in shelf_extensions:
            shelf_files.extend(findFilesByExtension(shelf_install_dir, ext))
    return shelf_files


def findShelfOTLFiles(shelf_install_dir):
    """ Recursively searches in 'shelf_install_dir' and returns a list
        of shelf files found in the directory tree.  Does not search
        in hidden directories or 'backup' directories. """
    otl_files = []
    for ext in digitalassetsupport.digitalAssetExtensions():
        otl_files.extend(findFilesByExtension(shelf_install_dir, ext))

    return otl_files


def chooseAndOpenAudioFile():
    """ Chooses and loads a soundtrack file, and sets up the Audio Panel 
        parameters to play the audio durng animation playback or playbar 
        scrubbing. """
    # first ask for the name of the audio file to use as a soundtrack    
    file_name = hou.ui.selectFile( title = 'choose the audio file',
                               pattern = '*.wav, *.aiff',
                               collapse_sequences = False,
                               multiple_select = False )
    if file_name != "":
        # set the playbar's realtime mode so that the sound plays at the 
        # natural pase during playback; otherwise it sounds too squiky
        hou.playbar.setRealTime( True )

        # now set the parameters in the audio panel; these parameters will
        # set the playback mode that will allow the sound to be played
        hou.audio.setAudioFileName( file_name )
        hou.audio.useTimeLineMode()
        hou.audio.useAudioFile()


def populateShelfFromJSON():
    """ Load the list of shelf tools corresponding to Orbolt assets
        and populate them in the shelf.
        """
    _ensure_toolbar_dir_exists()

    if not os.path.exists(_shelf_tool_assets_info_file()) or \
            not hou.isUIAvailable() : # no need to populate in non-graphical version
        return
        
    json_assets = hutil.json.object_from_json_data(
        hutil.json.utf8LoadFromFile(_shelf_tool_assets_info_file()))
    shelves = hou.shelves.shelves()
    tools = hou.shelves.tools()

    # Populate the shelf with assets from the JSON file. If the asset tool 
    # is already present in the shelf tools then we update its data. 
    # Otherwise, we create a tool for the asset. If the default toolbar for 
    # that tool doesn't exist, we also create it.
    for asset in json_assets:

        # If the tool is already defined, update it.
        if tools.has_key(asset['node_type_name']):
            tool = tools[asset['node_type_name']]
            tool_file_path = tool.filePath()

            if os.path.exists(tool_file_path) \
                and not os.access(tool_file_path, os.W_OK):
                # Shelf file is unwritable so tool cannot be updated.
                continue

            tool.setData(icon=asset['icon_name'],
                help=asset['help'],
                help_url=asset['help_url'])
            tool.setLabel(asset['label'])

        elif hou.shelves.isToolDeleted(asset['node_type_name']):
            # The tool has been deleted by the user, so don't bother
            # adding it again.
            return
        else:
            # We need to find the shelf the tool goes in.
            matching_shelf = None
            need_to_set_tools = False
            for shelf_name, shelf in shelves.items():
                if asset['shelf_name'] == shelf_name:
                    matching_shelf = shelf
                    need_to_set_tools = all([tool.name() != asset['node_type_name']
                                             for tool in shelf.tools()])
                    break

            # Need to add to a shelf. Has one already been created?
            if matching_shelf is None:
                # Create that shelf.
                matching_shelf = hou.shelves.newShelf(name=asset['shelf_name'])
                need_to_set_tools = True

            new_tool = hou.shelves._newAssetTool(
                name=asset['node_type_name'],
                label=asset['label'],
                icon=asset['icon_name'],
                help=asset['help'],
                help_url=asset['help_url'])

            if need_to_set_tools:
                matching_shelf.setTools(matching_shelf.tools() + (new_tool,))


def installOrboltAsset(kwargs, node_name, url):
    """ Script that Houdini calls when clicking on a shelf tool that
        corresponds to an Orbolt asset. We can either direct the user
        to the asset store if it the asset has not been installed yet
        or install it in the viewport.
        """
    asset_info = sas.localassets._find_asset_entry(node_name)
    
    if asset_info is None:
        # Direct the user towards Orbolt so he/she can download the asset
        webbrowser.open(url)
    else:
        # Install the asset in the viewport

        abrowser = sas.localassets._find_or_create_asset_browser_pane_tab(
            False) # do not set focus on the browser pane

        abrowser.installRequiredDefinitionsForNodeTypeName(
                asset_info['node_type_name'])
        otl_path = sas.localassets._otl_file_path(asset_info['node_type_name'])
        otl_defs = hou.hda.definitionsInFile(otl_path)
        for otl_def in otl_defs:
            # alternative: digitalassetsupport.create_instance(otl_def.nodeType())
            # alternative: import objecttoolutils\n
            #              objecttoolutils.genericTool(kwargs, ...)
            library = otl_def.nodeType().category().name().lower() + "toolutils"
            command = "import " + library + "\n" +\
                      library + ".genericTool(kwargs, " +\
                      "otl_def.nodeType().name())"
            exec command

def _ensure_toolbar_dir_exists():
    toolbar_dir = hou.homeHoudiniDirectory() + "/toolbar"
    hutil.file.ensureDirExists(toolbar_dir)

def _shelf_tool_assets_info_file():
    return hou.homeHoudiniDirectory() + "/toolbar/shelf_tool_assets.json"
