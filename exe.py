import cx_Freeze
import sys

base = None

if sys.platform == "win64":
    base = "win32GUI"
includes = ['config.csv','lisensing.py']
executables = [cx_Freeze.Executable("lisensing.py", base=base)]

cx_Freeze.setup(
    name = "anshi",
    option= {"build_exe":{"packages":["tkinter","xmltodict"],'includes':includes}},
    executables = executables
    )
