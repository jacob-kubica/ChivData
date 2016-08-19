'''
Created on Aug 18, 2016

@author: Jacob
'''
from cx_Freeze import setup, Executable

buildOptions = dict(include_files = ["Harambe's Chiv Data Cruncher/"]) #folder,relative path. Use tuple like in the single file to set a absolute path.

setup(
         name = "appname",
         version = "1.0",
         description = "description",
         author = "your name",
         options = dict(build_exe = buildOptions),
         executables = [Executable("Main.py")])