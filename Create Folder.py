import os
import datetime

today = datetime.date.today()
# folder_name = today.strftime('%Y-%m-%d')
folder_name = today.strftime('%Y%m%d')
os.mkdir(folder_name)