import sys
from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\zhou.xu\\AppData\\Local\\Programs" \
                            "\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\zhou.xu\\AppData\\Local\\Programs" \
                            "\\Python\\Python36-32\\tcl\\tk8.6"

sys.argv.append("build")
buildOptions = dict(
    packages = [],
    excludes = [],
    include_files=["C:\\Users\\zhou.xu\\AppData\\Local\\Programs" \
                            "\\Python\\Python36-32\\DLLs\\tcl86t.dll",
                   "C:\\Users\\zhou.xu\\AppData\\Local\\Programs" \
                            "\\Python\\Python36-32\\DLLs\\tk86t.dll"]
)


filename = "cal_24_gui.py"
base = None
if sys.platform == "win32":
    base = "Win32GUI"
setup(
    name = "Circle",
    version = "1.0",
    options = dict(build_exe = buildOptions),
    description = "cx_Freeze Tkinter script",
    executables = [Executable(filename, base=base)])