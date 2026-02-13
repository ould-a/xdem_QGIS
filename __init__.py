import subprocess
import os
import sys
import pip

from .xdem_config import (PLUGINDIR,
                         VENVNAME,
                         VENVFOLDER,)


def classFactory(iface):

    from .xdem_plugin import XDemPlugin

    return XDemPlugin()


def setupxdem():

    if VENVNAME not in os.listdir(PLUGINDIR):

        # Windows
        if os.name == "nt":

            python_executable = os.path.join(sys.prefix, "python.exe")

            subprocess.check_call([
                python_executable,
                "-m",
                "pip",
                "install",
                "--target",
                venvfolder,
                "xdem"
            ])
        
        # Linux
        else:
            pip.main(["install", "--target", VENVFOLDER, "xdem"])

setupxdem()
