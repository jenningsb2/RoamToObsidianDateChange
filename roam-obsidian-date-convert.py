import os
from datetime import datetime, date
from dateutil.parser import *
# Insert yout path name here to your daily notes folder. I recommend temporarily dragging the folder to your desktop.

path = #'path name here'

#loops through all of the files in the folder above

for f in os.listdir(path):
    filename, fileext = os.path.splitext(f)
    try:
        #converts to YYYY-MM-DD format
        split_name = str(parse(filename))
    except ValueError as e:
        continue
    else:
        #splits and renames the files
        just_date = split_name.split(" ")
        format_date_name = (just_date[0] + fileext)
        os.rename(path + '/' + f, path + '/' + format_date_name)
