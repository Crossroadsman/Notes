# --> the filename,
# e.g., settings.py
__file__   


# --> the full absolute path (including filename) of the specified file
# e.g., /home/<user>/<path>/<to>/<project>/<project_name>/settings.py
os.path.abspath( __file__ ) 

# --> full absolute path to the directory containing the specified file (or directory)
os.path.dirname( os.path.abspath( __file__ ))
