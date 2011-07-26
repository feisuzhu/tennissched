# Requires wxPython.  This sample demonstrates:
#
# - single file exe using wxPython as GUI.

from distutils.core import setup
import py2exe
import sys

# If run without args, build executables, in quiet mode.
if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        # for the versioninfo resources
        self.version = "1.0.0.0"
        self.company_name = "Proton"
        self.copyright = "Licensed under GNU GPL"
        self.name = "Match Scheduling"

################################################################
# A program using wxPython

# The manifest will be inserted as resource into test_wx.exe.  This
# gives the controls the Windows XP appearance (if run on XP ;-)
#
# Another option would be to store it in a file named
# test_wx.exe.manifest, and copy it with the data_files option into
# the dist-dir.
#

main = Target(
    # used for the versioninfo resource
    description = "Match Scheduling",

    # what to build
    script = "main.py",
    icon_resources = [(1, "appicon.ico")],
    dest_base = "main")

################################################################

setup(
    options = {"py2exe": {"compressed": 1,
                          "optimize": 2,
                          "ascii": 1,
			  "packages" : ["encodings"],
			  "dll_excludes": ["MSVCP90.dll"],
                          "bundle_files": 1}},
    zipfile = None,
    windows = [main],
    )
