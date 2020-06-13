import os
from datetime import datetime, date
from dateutil.parser import *

path = '/Users/baileyjennings/Desktop/Daily_Notes'
for f in os.listdir(path):
    filename, fileext = os.path.splitext(f)
    try:
        split_name = str(parse(filename))
    except ValueError as e:
        continue
    else:
        just_date = split_name.split(" ")
        format_date_name = (just_date[0] + fileext)
        os.rename(path + '/' + f, path + '/' + format_date_name)
