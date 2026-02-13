import os


PLUGINDIR = os.path.dirname(__file__)
VENVNAME = "xdemvenv"
VENVFOLDER = os.path.join(PLUGINDIR, VENVNAME)
SUBPRCSFOLD = os.path.join(PLUGINDIR, "subprocess")


def xdempyexe():

    # Windows
    if os.name == "nt":
        xdempy = ...

    # Linux
    else :
        xdempy = os.path.join(PLUGINDIR, VENVNAME, "/bin/python")
    
    return xdempy


XDEMPY = xdempyexe()