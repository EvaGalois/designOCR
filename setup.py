import sys
from cx_Freeze import setup, Executable

# 请将 'path_to_dll_folder' 替换为你的 "dll_files" 文件夹的路径，存放 PyQt5 的 DLL 文件
build_exe_options = {
    "packages": ["PyQt5", "fuzzywuzzy"],  # 包含的库
    "includes": ["PyQt5.QtCore", "PyQt5.QtGui", "PyQt5.QtWidgets", "keyboard"],  # 包含的 PyQt5 模块
    "excludes": [],
    "include_files": [("icon.ico", "icon.ico"),
                    ("ppocr", "ppocr"),
                    ("SimHei.ttf", "SimHei.ttf"),
                    ("vcomp140.dll", "vcomp140.dll"),
                    ("msvcp140.dll", "msvcp140.dll"),
                    ("ocr_false_detection.txt", "ocr_false_detection.txt")],
}

base = "Win32GUI"
# base = None

executables = [Executable("Galois_Verification.py", base=base, icon='icon.ico'), Executable("screenshot_tool.py", base=base, icon='icon.ico')]

setup(
    name="Galois's Content Verification",
    version="1.0",
    description="Galois's Content Verification",
    options={
        "build_exe": build_exe_options
    },
    executables=executables,
)
